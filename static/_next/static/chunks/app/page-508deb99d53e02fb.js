(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[931],{2154:function(e,t,a){Promise.resolve().then(a.bind(a,3561))},3561:function(e,t,a){"use strict";a.r(t),a.d(t,{default:function(){return b}});var n=a(9268),l=a(6006),r=a(1649),i=a(4240),s=a(7095),o=a(8235),c=a(2171),d=a(9454),h=a(5857),u=a(5911),x=a(3334),f=a(536),p=a(9861),j=a(9715);function b(){let[e,t]=(0,l.useState)(null),[a,b]=(0,l.useState)(!1),[m,Z]=(0,l.useState)([]),[g,v]=(0,l.useState)({}),[y,C]=(0,l.useState)(0),[S,w]=(0,l.useState)(!1),k=["placeholder1","placeholder2","placeholder3"],[D,P]=(0,l.useState)(null),[E,O]=(0,l.useState)(!1),T=e=>{e.target.files&&e.target.files[0]&&t(e.target.files[0])},_="http://127.0.0.1:5000",F=async t=>{if(t.preventDefault(),!e){alert("Please select a file before uploading.");return}let a=new FormData;a.append("file",e),a.append("useOCR",S.toString());try{let e=await fetch("".concat(_,"/api/extract-tables"),{method:"POST",body:a}),t=await e.json();if(!t.success){alert("Failed to extract tables.");return}Z(t.tables),v(t.tables.reduce((e,t,a)=>(e[a]=t.headers.reduce((e,t)=>(e[t]="",e),{}),e),{})),b(!0)}catch(e){console.error("Error extracting tables:",e)}},N=(e,t)=>{v(a=>({...a,[y]:{...a[y],[e]:t}}))},W=()=>{y<m.length-1&&C(y+1)},R=()=>{y>0&&C(y-1)},A=async e=>{e.preventDefault();try{let e=m.map((e,t)=>{let a=e.headers,n=e.table_data.map(e=>{let t={};return a.forEach(a=>{t[a]=e[a]}),t});return{headers:a,table_data:n,header_mappings:g[t]}}),t=await fetch("".concat(_,"/api/export-csv"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({tables:e})});if(!t.ok)throw Error("Failed to download CSVs");let a=await t.json();b(!1),P(a.file_path),O(!0)}catch(e){console.error("Error exporting CSVs:",e)}},V=()=>{t(null),b(!1),Z([]),v({}),C(0),w(!1),P(null),O(!1)};return(0,n.jsxs)(r.Z,{display:"flex",flexDirection:"column",alignItems:"center",minHeight:"100vh",bgcolor:"#f5f5f5",children:[(0,n.jsx)(i.Z,{variant:"h3",gutterBottom:!0,children:"COINS PDF EXTRACTOR"}),!a&&!E&&(0,n.jsx)(s.Z,{sx:{maxWidth:600,width:"100%"},children:(0,n.jsx)(o.Z,{children:(0,n.jsxs)("form",{onSubmit:F,children:[(0,n.jsxs)(r.Z,{mb:2,children:[(0,n.jsx)(i.Z,{variant:"body1",children:"Select a PDF file:"}),(0,n.jsx)(c.Z,{type:"file",fullWidth:!0,onChange:T,inputProps:{accept:".pdf"}})]}),(0,n.jsx)(d.Z,{control:(0,n.jsx)(h.Z,{checked:S,onChange:()=>w(!S)}),label:"Run OCR on PDF before extraction"}),(0,n.jsx)(r.Z,{display:"flex",justifyContent:"center",mt:2,children:(0,n.jsx)(u.Z,{variant:"contained",color:"primary",type:"submit",children:"Extract Tables"})})]})})}),a&&m.length>0&&!E&&(0,n.jsx)(s.Z,{sx:{maxWidth:600,width:"100%",mt:4},children:(0,n.jsxs)(o.Z,{children:[(0,n.jsxs)(i.Z,{variant:"h4",children:["Table ",y+1," of ",m.length]}),m[y].headers.map(e=>(0,n.jsxs)(x.Z,{fullWidth:!0,sx:{my:2},children:[(0,n.jsx)(f.Z,{children:e}),(0,n.jsxs)(p.Z,{value:g[y][e]||"",onChange:t=>N(e,t.target.value),children:[(0,n.jsx)(j.Z,{value:"",children:"(Keep Original)"}),k.map(e=>(0,n.jsx)(j.Z,{value:e,children:e},e))]})]},e)),(0,n.jsxs)(r.Z,{display:"flex",justifyContent:"space-between",mt:2,children:[(0,n.jsx)(u.Z,{variant:"outlined",onClick:R,disabled:0===y,children:"Previous Table"}),(0,n.jsx)(u.Z,{variant:"contained",onClick:W,disabled:y===m.length-1,children:"Next Table"})]}),y===m.length-1&&(0,n.jsxs)(r.Z,{display:"flex",flexDirection:"column",alignItems:"center",mt:4,children:[(0,n.jsx)(u.Z,{variant:"contained",color:"primary",sx:{mb:2},onClick:e=>A(e),children:"Export All Tables as CSV"}),(0,n.jsx)(u.Z,{variant:"outlined",color:"secondary",onClick:V,children:"Submit Another PDF"})]})]})}),!a&&E&&D&&(0,n.jsx)(s.Z,{sx:{maxWidth:600,width:"100%",mt:4},children:(0,n.jsxs)(o.Z,{children:[(0,n.jsx)(i.Z,{variant:"h3",gutterBottom:!0,children:"Download Complete"}),(0,n.jsx)(i.Z,{variant:"h5",children:"Your CSV file has been saved to:"}),(0,n.jsx)(i.Z,{variant:"body1",sx:{mt:2,fontWeight:"bold",wordBreak:"break-all"},children:D}),(0,n.jsx)(u.Z,{variant:"outlined",color:"secondary",onClick:V,children:"Submit Another PDF"})]})})]})}}},function(e){e.O(0,[863,667,139,744],function(){return e(e.s=2154)}),_N_E=e.O()}]);