import os

def CreateFolderIfDoesntExist(merged_pdfs_folder_path):
    if not os.path.isdir(merged_pdfs_folder_path):
        os.mkdir(merged_pdfs_folder_path)