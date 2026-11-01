import os

def file_organizer():
    mapping = {
        '.pdf' : 'PDFs',
        '.jpg' : "Images",
        '.png' : "Images",
        '.bmp' : "Images",
        '.gif' : "Images",
        '.mov' : "Movies",
        '.mp4' : "Movies",
        '.mp3' : "Sound" ,
        '.txt' : "Text Documents",
        '.zip' : "Archives",
    }

    while True:
        target_directory = input("Please enter the target directory to reorganize (or type 'exit'):\n ").strip().strip('"\'')

        if target_directory.lower() in ['exit', 'quit']:
            print("Exiting organizer.")
            return

        try:
            if not os.path.exists(target_directory):
                print(f"Unable to locate the filepath {target_directory}. Please try again.\n")
                continue
            if not os.path.isdir(target_directory):
                print(f"{target_directory} is a file, not a folder.\n")
                continue

            os.listdir(target_directory)

            clean_path = os.path.abspath(target_directory)

            print(f"Successfully located filepath {clean_path}\n")
            
            break
        
        except PermissionError:
            print("Unable to access the directory due to a permission error from Windows.\n")
        except OSError as e:
            print(f"Invalid Windows path format. {e.strerror}.\n")

        
    print("Folders initialized, ready to organize files.")

    moved_files = 0

    for item_name in os.listdir(clean_path):
        current_file_path = os.path.join(clean_path, item_name)

        if os.path.isfile(current_file_path):
            _, file_extension = os.path.splitext(item_name)
            file_extension = file_extension.lower()

            if file_extension in mapping:
                destination_folder_name = mapping[file_extension]
                destination_folder_path = os.path.join(clean_path, destination_folder_name)

                if not os.path.exists(destination_folder_path):
                    try:
                        os.makedirs(destination_folder_path, exist_ok=True)
                        print("Created folders as necessary.")
                    except Exception as e:
                        print(f"Could not create folder {e}")
                        continue

                new_filepath = os.path.join(destination_folder_path, item_name)
                
                try:
                    os.rename(current_file_path, new_filepath)
                    print(f"Movded {item_name} to {destination_folder_name}.")
                    moved_files += 1
                except Exception as e:
                    print(f"Could not move {item_name}. {e}")
            else:
                print(f"Skipped untracked extension: {item_name}.")

    print(f"Done! Moved {moved_files} into their target folders.")


if __name__ == "__main__":
    file_organizer()