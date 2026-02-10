import pypdf

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = pypdf.pdfFileReader(pdfFileObj)

print(pdfReader.numPages)