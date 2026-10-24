from pypdf import PdfReader
from pypdf import PdfReader
import pdfplumber
import pymupdf

Book = PdfReader('SmallBook.pdf')
#print(len(Book.pages)) # Lenth of the Pdf
page1 = Book.pages[7]#page8
#print(page1.extract_text())#reading one page

#Now we will Print All of the Pages

#for i in range(len(Book.pages)):
#    page = Book.pages[i]
#    print(page.extract_text())

# Now we will find out the image in page

#for i in page1.images: # i is an image Object
#    with open(i.name, 'wb') as img: # I am wrting an image(binary)
#        img.write(i.data)
#        print(f"Extracted: {i.name}")


# Now we will Print the tables(if any) in the Pdf

with pdfplumber.open('smallbook.pdf') as book:
    for i in book.pages:
        print(i.extract_tables())