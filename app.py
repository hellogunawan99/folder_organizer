import os
import shutil

# Path to your download folder
download_folder = '/Users/gunawan/Downloads'

# Dictionary to map file extensions to folder names
extension_folder_mapping = {
    'txt': 'TextFiles',
    'pdf': 'PDFs',
    'jpg': 'Images',
    'png': 'Images png',
    'gif': 'Images gif',
    'mp4': 'Videos',
    'mp3': 'Music',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'docx': 'Documents doc',
    'xlsx': 'Documents excel',
    'pptx': 'Documents ppt',
}


def organize_folder(download_folder):
    for filename in os.listdir(download_folder):
        src = os.path.join(download_folder, filename)
        if os.path.isfile(src):
            # Get the file extension
            _, extension = os.path.splitext(filename)
            # Remove the dot and convert to lowercase
            extension = extension[1:].lower()
            if extension in extension_folder_mapping:
                destination_folder = os.path.join(
                    download_folder, extension_folder_mapping[extension])
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                dest = os.path.join(destination_folder, filename)
                shutil.move(src, dest)


if __name__ == "__main__":
    organize_folder(download_folder)
