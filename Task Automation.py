
#                                                    Programmed by: Jaweria Khan
#                                                    CodeAlpha Python Programming 
#                                                    Task 4: Task Automation (file organization) 

import os
import shutil
import json

LOG_FILE = "file_organizer_log.json"

def organize_files(folder_path):
    """
    Organizes files in the given folder by their file extensions.
    Creates subfolders for each file type and moves files accordingly.
    Logs the original file paths for undo functionality.
    """
    
    try:
        if not os.path.exists(folder_path):
            print("The specified folder does not exist.")
            return False

        log_data = {}

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isdir(file_path):
                continue

            file_extension = os.path.splitext(file_name)[1][1:].lower()
            if not file_extension:
                file_extension = "others"

            subfolder_path = os.path.join(folder_path, file_extension)
            os.makedirs(subfolder_path, exist_ok=True)

            destination_path = os.path.join(subfolder_path, file_name)
            log_data[destination_path] = file_path
            shutil.move(file_path, destination_path)

        with open(LOG_FILE, "w") as log_file:
            json.dump(log_data, log_file, indent=4)

        print(f"Files in '{folder_path}' have been organized successfully!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def undo_organization():
    """
    Reverts the file organization using the log file.
    Moves files back to their original locations and deletes empty subfolders.
    """

    try:
        if not os.path.exists(LOG_FILE):
            print(f"No log file found. Make sure you've organized files before attempting to undo.")
            return

        with open(LOG_FILE, "r") as log_file:
            log_data = json.load(log_file)

        # Track subfolders to potentially delete them
        subfolders_to_check = set()

        for dest_path, original_path in log_data.items():
            if os.path.exists(dest_path):
                os.makedirs(os.path.dirname(original_path), exist_ok=True)
                shutil.move(dest_path, original_path)
                subfolders_to_check.add(os.path.dirname(dest_path))  # Add the subfolder for cleanup
            else:
                print(f"File '{dest_path}' is missing and cannot be moved back.")

        # Delete empty subfolders
        for subfolder in subfolders_to_check:
            try:
                if os.path.exists(subfolder) and not os.listdir(subfolder):
                    os.rmdir(subfolder)
                    print(f"Deleted empty folder: {subfolder}")
            except Exception as e:
                print(f"Could not delete folder '{subfolder}': {e}")

        os.remove(LOG_FILE)
        print("File organization has been undone successfully!")
    except Exception as e:
        print(f"An error occurred during undo: {e}")


if __name__ == "__main__":
    print("Welcome to the File Organizer!")

    while True:
        print("\nMain Menu:")
        print("1. Organize files in a folder")
        print("2. Undo the last organization")
        print("3. Exit the program")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            folder_to_organize = input("Enter the folder path to organize files: ").strip()
            success = organize_files(folder_to_organize)

            if success:
                while True:
                    undo_choice = input("\nDo you want to undo the organization? (yes/no): ").strip().lower()
                    if undo_choice == "yes":
                        undo_organization()
                        break
                    elif undo_choice == "no":
                        print("Files remain organized. Exiting to the main menu.")
                        break
                    else:
                        print("Invalid input. Please type 'yes' or 'no'.")
        elif choice == "2":
            undo_organization()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
