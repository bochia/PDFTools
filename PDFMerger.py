import easygui
import PyPDF2
import sys
import os

from easygui.boxes.derived_boxes import msgbox

def GetPDFFileName():
    request_Text = "Enter Name For Resulting PDF File"
    window_Title = "PDF Merger"
    resulting_pdf_name = easygui.enterbox(request_Text, window_Title, str())
    return resulting_pdf_name

def CreateFolder(merged_pdfs_folder_path):
    if not os.path.isdir(merged_pdfs_folder_path):
        os.mkdir(merged_pdfs_folder_path)

def Main():
    # Main
    result_pdf_Name = GetPDFFileName()

    if not result_pdf_Name:
        sys.exit()

    pdf_path = "Anything but empty string"
    pdf_paths = []

    #If user hits cancel on dialog box then stop requesting.
    while pdf_path:
        pdf_path = easygui.fileopenbox()

        if pdf_path:
            pdf_paths.append(pdf_path)

    merged_pdfs_folder_path = f"C:\\Users\\{os.getlogin()}\\Desktop\\Merged PDFs\\"
    CreateFolder(merged_pdfs_folder_path)

    result_pdf_path = f"{merged_pdfs_folder_path}{result_pdf_Name}.pdf"

    pdf_merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_paths:
        pdf_merger.append(pdf)

    pdf_merger.write(result_pdf_path)
    pdf_merger.close()

    msgbox(f"Merged PDF can be found on 'Merged PDFs' folder on the desktop: {merged_pdfs_folder_path}")

try:
    Main()
except Exception as e:
    msgbox(f"EXCEPTION: {e}")


