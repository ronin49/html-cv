#!/usr/bin/python3
import pdfkit
pdfkit.from_url('http://0.0.0.0:8000/html-cv/cv.html', 'out.pdf')
