#!/usr/bin/env python
from docx import Document

doc = Document()
p = doc.add_paragraph("You will be hacked !")
doc.save("resume.docx")
