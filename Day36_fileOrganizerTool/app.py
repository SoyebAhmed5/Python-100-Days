import os
import shutil

def create_directory(path):
    folders = ["Images", "Documents", "Videos", "Music", "Archives", "Others"]
    for folder in folders:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_file(file_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file_path, destination_folder)
    
def get_folder_for_file(file_name):
    extension = os.path.splitext(file_name)[1].lower()
    if extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
        return "Images"
    elif extension in ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx']:
        return "Documents"
    elif extension in ['.mp4', '.avi', '.mov', '.mkv']:
        return "Videos"
    elif extension in ['.mp3', '.wav', '.flac']:
        return "Music"
    elif extension in ['.zip', '.rar', '.tar', '.gz']:
        return "Archives"
    else:
        return "Others"
    
def organize_files_in_directory(directory):
    create_directory(directory)
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            folder_name = get_folder_for_file(item)
            destination_folder = os.path.join(directory, folder_name)
            move_file(item_path, destination_folder)
            
def main():
    directory = input("Enter the path of the directory to organize: ")
    if os.path.exists(directory) and os.path.isdir(directory):
        organize_files_in_directory(directory)
        print("Files have been organized successfully.")
    else:
        print("The provided path is not a valid directory.")
        
if __name__ == "__main__":
    main()