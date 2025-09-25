import os
import shutil

# Необходимо иметь список всех возможных расширений и то, к какой директории они бы принадлежали
# Создавать всю структуру папок сразу же? Или создавать по мере появления новых файлов?

EXTENSIONS = {
    "Images":[
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".heic", ".heif",
        ".raw", ".cr2", ".nef", ".arw", ".orf", ".rw2", ".svg",
    ],
    "Videos":[
        ".mp4", ".mkv", ".avi", ".mov", ".wmv",
        ".flv", ".webm", ".m4v", ".mpg", ".mpeg", ".3gp",
    ],
    "Documents":[
        ".pdf", ".doc", ".docx", ".xls", ".xlsx",
        ".ppt", ".pptx", ".odt", ".ods", ".odp",
        ".rtf", ".txt", ".csv", ".md", ".epub", ".tex",
    ],
}

def create_main_files(path):
    """

    Args:
        path: path to the directory

    Returns:
        None
    """
    if os.path.isdir(path):
        for key in EXTENSIONS.keys():
            dir_path = os.path.join(path, key)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

def define_filetype(filename: str) -> str:
    """

    Args:
        filename: name of the file

    Returns:
        type of the file
    """
    filetype = '.' + filename.split('.')[-1]
    for key, value in EXTENSIONS.items():
        if filetype in value:
            return key
    return "Other"

def sort_files(path: str):
    for dirpath, dirnames, filenames in os.walk(path):
        dirnames.clear()
        for filename in filenames:
            filetype = define_filetype(filename)
            if filetype != "Other":
                shutil.move(os.path.join(dirpath, filename), os.path.join(path, filetype))


def main():
    path = "/home/ilukssa/Documents/Test"
    create_main_files(path)
    sort_files(path)


if __name__ == "__main__":
    main()