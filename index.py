import subprocess
import webview
import threading
import io
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory, send_file
import zipfile
import pandas as pd
from gmft.pdf_bindings import PyPDFium2Document
from gmft.auto import AutoTableDetector, AutoTableFormatter
import tempfile
import os

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def serve_home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

detector = AutoTableDetector()
formatter = AutoTableFormatter()

def ingest_pdf(pdf_path):
    doc = PyPDFium2Document(pdf_path)
    tables = []
    for page in doc:
        tables += detector.extract(page)
    return tables, doc

def preprocess_pdf_with_ocr(input_pdf_path, output_pdf_path):
    """
    Preprocess PDF with OCR using ocrmypdf.
    """
    try:
        command = ["ocrmypdf", "--redo-ocr", input_pdf_path, output_pdf_path]
        subprocess.run(command, check=True)
        return output_pdf_path
    except subprocess.CalledProcessError as e:
        return None
    except FileNotFoundError:
        return None

@app.route('/api/extract-tables-ocr', methods=['POST'])
def extract_tables_with_ocr():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided."}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400

    with tempfile.TemporaryDirectory() as temp_dir:
        input_pdf_path = os.path.join(temp_dir, file.filename)
        output_pdf_path = os.path.join(temp_dir, "ocr_" + file.filename)
        file.save(input_pdf_path)

        ocr_processed_pdf = preprocess_pdf_with_ocr(input_pdf_path, output_pdf_path)
        if not ocr_processed_pdf:
            return jsonify({"error": "OCR processing failed."}), 500

        try:
            tables, doc = ingest_pdf(ocr_processed_pdf)

            if tables:
                ft = formatter.extract(tables[0])
                df = ft.df() 
                json_data = df[df.columns.tolist()].to_dict(orient="records")

                return jsonify({"tables": json_data})
            else:
                return jsonify({"message": "No tables found in the OCR-processed PDF."})
        except Exception as e:
            return jsonify({"error": f"Failed to extract tables: {str(e)}"}), 500
        
    doc.close()

@app.route('/api/extract-tables', methods=['POST'])
def extract_tables():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided."}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400

    use_ocr = request.form.get("useOCR") == "true"

    with tempfile.TemporaryDirectory() as temp_dir:
        pdf_path = os.path.join(temp_dir, file.filename)
        file.save(pdf_path)

        if use_ocr:
            output_pdf_path = os.path.join(temp_dir, "ocr_" + file.filename)
            pdf_path = preprocess_pdf_with_ocr(pdf_path, output_pdf_path) or pdf_path

        try:
            tables, doc = ingest_pdf(pdf_path)
            if not tables:
                return jsonify({"message": "No tables found in the PDF."})

            all_tables = []

            for table in tables:
                df = formatter.extract(table).df()

                ordered_columns = list(df.columns)  
                table_data = df[ordered_columns].to_dict(orient="records")  

                all_tables.append({
                    "headers": ordered_columns,  
                    "table_data": table_data     
                })
            doc.close()
            return jsonify({"success": True, "tables": all_tables})

        except Exception as e:
            doc.close()
            return jsonify({"error": f"Failed to extract tables: {str(e)}"}), 500

def get_downloads_folder():
    """Get the default Downloads folder based on the OS."""
    if os.name == "nt":  # Windows
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    else:  # macOS/Linux
        return os.path.join(os.path.expanduser("~"), "Downloads")

@app.route("/api/export-csv", methods=["POST"])
def export_csv():
    """Generate multiple CSVs and save automatically to Downloads."""
    data = request.json
    if not data or "tables" not in data:
        return jsonify({"error": "Invalid request format"}), 400

    downloads_folder = get_downloads_folder()
    zip_filename = "tables.zip"
    zip_path = os.path.join(downloads_folder, zip_filename)

    # Create a ZIP file in memory
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for idx, table in enumerate(data["tables"]):
            df = pd.DataFrame(table["table_data"])
            header_mappings = table["header_mappings"]

            updated_headers = {
                col: header_mappings[col] if col in header_mappings and header_mappings[col] else col
                for col in df.columns
            }
            df.rename(columns=updated_headers, inplace=True)

            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)

            # Write CSV data to ZIP file
            zipf.writestr(f"table_{idx+1}.csv", csv_buffer.getvalue())

    return jsonify({"message": "File saved successfully!", "file_path": zip_path})


# @app.route('/api/export-csv', methods=['POST'])
# def export_csv():
#     data = request.json
#     if not data or 'tables' not in data:
#         return jsonify({"error": "Invalid request format"}), 400

#     exported_files = {}

#     for idx, table in enumerate(data["tables"]):
#         df = pd.DataFrame(table["table_data"])
#         header_mappings = table["header_mappings"]

#         updated_headers = {col: header_mappings[col] if col in header_mappings and header_mappings[col] else col for col in df.columns}
#         df.rename(columns=updated_headers, inplace=True)

#         csv_buffer = io.StringIO()
#         df.to_csv(csv_buffer, index=False)

#         exported_files[f"table_{idx+1}.csv"] = csv_buffer.getvalue()

#     return jsonify({"csv_files": exported_files})


def start_flask():
    app.run(host="127.0.0.1", port=5000, debug=False)

if __name__ == "__main__":
    threading.Thread(target=start_flask, daemon=True).start()

    webview.create_window("COINS PDF Extractor", "http://127.0.0.1:5000")
    webview.start(debug=True)
