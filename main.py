import os

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
        ".rtf", ".txt", ".csv", ".md", ".epub", ".tex"
    ],
}
def define_filetype(filename: str) -> str:
    """

    Args:
        filename: name of the file

    Returns:
        type of the file
    """

def sort_files(path: str):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:


def main():
    pass



if __name__ == "__main__":
    main()