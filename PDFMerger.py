#python 3.6.5
import easygui
import PyPDF2
import sys
import PDFToolsModule
from easygui.boxes.derived_boxes import msgbox
import os

def Main():
    request_Text = "Enter Name For Resulting PDF File"
    window_Title = "PDF Merger"
    result_pdf_Name = easygui.enterbox(request_Text, window_Title, str())

    if not result_pdf_Name:
        sys.exit()

    pdf_path = "Anything but empty string to allow inital entrance into while loop" 
    pdf_paths = []
    default_file_open_path = f"C:\\Users\\{os.getlogin()}\\Documents\\"

    #If user hits cancel on dialog box then stop requesting.
    while pdf_path:
        pdf_path = easygui.fileopenbox(msg="", title="Choose a PDF File", default=default_file_open_path)

        if pdf_path:
            default_file_open_path = PDFToolsModule.GetParentDirectoryFromFilePath(pdf_path) + "\\" #set default directory to where last file was choosen.
            pdf_paths.append(pdf_path)

    merged_pdfs_folder_path = f"C:\\Users\\{os.getlogin()}\\Desktop\\Merged PDFs\\"
    PDFToolsModule.CreateFolderIfDoesntExist(merged_pdfs_folder_path)

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


