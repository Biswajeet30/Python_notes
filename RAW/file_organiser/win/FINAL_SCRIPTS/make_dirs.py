import os

working_directory = r"E:\sorted Youtube vids 2023_2024\2024"

folder_names_list = [
    "Bharat_other_GP",
    "Bharat_social_engineering_politics",
    "Bharat_Spiritual_culture",
    "Bharat_tech",
    "miscellaneous"
]

def make_folders_files(target_path):
    """
    make files or folders in a desired path.

    Parameters:
    - target_path (str): The path to the target folder.

    """
    # Print current working directory
    directory_whoami = os.getcwd()
    print("Current Working Directory:", directory_whoami)

    # Make folders
    for new_folder_name in folder_names_list:
        os.makedirs(os.path.join(target_path, new_folder_name), mode=0o755, exist_ok=True)

def main():
    make_folders_files(target_path=working_directory)
    print(os.listdir(working_directory))

if __name__ == "__main__":
    main()
