import pyttsx3
import PyPDF2
book = open('ob.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(11, pages):
    pages = pdfReader.getPage(11)
    text = pages.extractText()
    speaker.say(text)
    speaker.runAndWait()

