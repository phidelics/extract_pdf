## import libraries
from PyPDF2 import PdfReader
## pass the arg to variable
reader = PdfReader('file.pdf')

page = reader.pages[0]
text = page.extract_text()
### print the content
print(text)