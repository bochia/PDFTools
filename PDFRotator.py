import PyPDF2
import easygui
import PDFToolsModule
from easygui.boxes.derived_boxes import msgbox
import os

def Main():
    request_Text = "Enter Name For Resulting PDF File"
    window_Title = "PDF Rotator"
    result_pdf_Name = easygui.enterbox(request_Text, window_Title, str())

    in_file_path = pdf_path = easygui.fileopenbox()

    pdf_in = open(in_file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    NINTY_DEGREES = 90
    HUNDRED_EIGHTY_DEGREES = 180
    TWO_HUNDRED_SEVENTY_DEGREES = 270
    THREE_HUNDRED_SIXTY_DEGREES = 360

    pageNumberRotationPair = {
        1:HUNDRED_EIGHTY_DEGREES,
        2:NINTY_DEGREES
    }

    for pagenum in range(len(pageNumberRotationPair.keys())):
        pagenum
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(pageNumberRotationPair[pagenum + 1])
        pdf_writer.addPage(page)

        merged_pdfs_folder_path = f"C:\\Users\\{os.getlogin()}\\Desktop\\Merged PDFs\\"
        PDFToolsModule.CreateFolderIfDoesntExist(merged_pdfs_folder_path)
        result_pdf_path = f"{merged_pdfs_folder_path}{result_pdf_Name}.pdf"

    pdf_out = open(result_pdf_path, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()

try:
    Main()
except Exception as e:
    msgbox(f"EXCEPTION: {e}")