import os
import shutil
from mutagen import File
import json

def scan_directory(directory):
    """
    Scans the given directory for music files and returns a list of file paths.
    """
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp3', '.wav', '.flac')):
                music_files.append(os.path.join(root, file))
    return music_files

def extract_metadata(file_path):
    """
    Extracts metadata from the given music file.
    This is a placeholder function. In a real application, you would use a library like mutagen or eyed3.
    """
    # Placeholder metadata extraction
    metadata = {
        'title': os.path.splitext(os.path.basename(file_path))[0],
        'artist': 'Unknown Artist',
        'album': 'Unknown Album',
        'genre': 'Unknown Genre',
        'year': 'Unknown Year'
    }
    return metadata

def organize_music_files(music_files, output_directory):
    """
    Organizes music files into folders based on their metadata.
    """
    for file_path in music_files:
        metadata = extract_metadata(file_path)
        artist_folder = os.path.join(output_directory, metadata['artist'])
        album_folder = os.path.join(artist_folder, metadata['album'])

        # Create directories if they don't exist
        os.makedirs(album_folder, exist_ok=True)

        # Move the file to the new location
        shutil.move(file_path, os.path.join(album_folder, os.path.basename(file_path)))
        
def save_metadata(music_files, output_directory):
    """
    Saves the metadata of the music files to a JSON file.
    """
    metadata_list = []
    for file_path in music_files:
        metadata = extract_metadata(file_path)
        metadata['file_path'] = file_path
        metadata_list.append(metadata)

    with open(os.path.join(output_directory, 'metadata.json'), 'w') as f:
        json.dump(metadata_list, f, indent=4)
        
def main():
    input_directory = input("Enter the path of the directory to scan for music files: ")
    output_directory = input("Enter the path of the directory to organize music files into: ")

    # Scan for music files
    music_files = scan_directory(input_directory)
    print(f"Found {len(music_files)} music files.")

    # Organize music files
    organize_music_files(music_files, output_directory)
    print("Music files organized successfully.")

    # Save metadata
    save_metadata(music_files, output_directory)
    print("Metadata saved successfully.")
    
if __name__ == "__main__":
    main()