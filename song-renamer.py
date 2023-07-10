import os
import re

def rename_music_files(folder_path, patterns_to_delete, symbols_to_remove, show=True, rename=True):
    song_counter = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            song_counter += 1
            new_filename = filename

            # Remove symbols
            for symbol in symbols_to_remove:
                new_filename = new_filename.replace(symbol, "")

            # Delete patterns
            for pattern in patterns_to_delete:
                new_filename = re.sub(pattern, "", new_filename)

             # Capitalize each word
            new_filename = ' '.join(word.capitalize() for word in new_filename.split())

            # Remove extra spaces
            new_filename = re.sub(r"\s+(?=\.)", "", new_filename.strip())
            new_filename = re.sub(r"\s+", " ", new_filename)

            if (show and not new_filename == filename):
                print(f"[{filename}] => [{new_filename}]")

            # Rename the file
            if rename:
                try:
                    if new_filename != filename:
                        old_file_path = os.path.join(folder_path, filename)
                        new_file_path = os.path.join(folder_path, new_filename)
                        os.rename(old_file_path, new_file_path)
                        print(f"Renamed '{filename}' to '{new_filename}'")
                except FileExistsError:
                    song_counter -= 1 if song_counter >= 0 else 0
                    print("------------ Song already exists detected")
    
    print(f"(To)Rename-able songs: {song_counter}")

# Define the folder path
folder_path = "C:/Users/JRV/Desktop/Ipod"

# Define the regex patterns to delete and symbols to remove
patterns_to_delete = [
    r"\s+\[.*\]",
    r"\(.*\)",
    "X2Download.app - ",
]
symbols_to_remove = [
    "_"
]

# Call the function to rename the music files
rename_music_files(folder_path, patterns_to_delete, symbols_to_remove)
