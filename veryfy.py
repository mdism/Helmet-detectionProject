# from pathlib import Path
# import os
# import shutil

# found_images = 0
# not_found_images = 0
# total_scanned_images = 0
# moved_files = 0
# new_image_folder = "./NewImages"
# folder_path = Path("./labels")

# for file_path in folder_path.iterdir():
#     if file_path.is_file():
#         total_scanned_images += 1
#         filename = file_path.stem  # Directly extract the stem (filename without extension)
        
#         # Use glob to find matching images
#         image_path = Path("./images") / f"{filename}.png"
#         # image_files = list(image_path.glob("*"))


#         if Path.exists(image_path):
#             found_images += 1
#             shutil.move(str(image_path), new_image_folder)
#             moved_files += 1
#             # for image_file in image_files:
#         else:
#             not_found_images += 1
#             print(f"Image not found for {filename}")

# print(f"{total_scanned_images=}")
# print(f"{found_images=}")
# print(f"{not_found_images=}")
# print(f"{moved_files=}")


# import os

# # Specify the directory containing the files
# directory = './images'

# # Loop through each file in the directory
# counter = 0
# for filename in os.listdir(directory):
#     counter+=1
#     # Split the file name into name and extension
#     name, ext = os.path.splitext(filename)
#     # Create the new name (you can customize this part)
#     new_name = f"image_{counter}{ext}"
#     # Construct the full old and new file paths
#     old_file = os.path.join(directory, filename)
#     new_file = os.path.join(directory, new_name)
#     # Rename the file
#     os.rename(old_file, new_file)

# print("Files have been renamed successfully.")

import os

def rename_files_in_directory(parent_directory):
    for folder in ['no', 'with']:
        folder_path = os.path.join(parent_directory, folder)
        for filename in os.listdir(folder_path):
            name, ext = os.path.splitext(filename)
            new_name = f"{folder}_{name}{ext}"
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(parent_directory, new_name)
            )
            print(f"Renamed {filename} to {new_name}")
            # if filename.endswith(".png"):
            #     # Create new name by prepending folder name
            #     new_name = f"{folder}_{filename}"

# Replace with the path to your parent directory
parent_directory = './images'
rename_files_in_directory(parent_directory)

