import os
import os.path

def CreateFolderIfDoesntExist(merged_pdfs_folder_path):
    if not os.path.isdir(merged_pdfs_folder_path):
        os.mkdir(merged_pdfs_folder_path)


def GetParentDirectoryFromFilePath(file_path):
    dir_name = os.path.dirname(file_path)
    return dir_name