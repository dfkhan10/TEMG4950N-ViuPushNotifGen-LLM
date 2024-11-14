import os
from PIL import Image

# #Version1: Return a list of paths of thumbnails
# def retrieve_thumbnail(data_idx, path):

#     """
#     Search for PNG files in the specified folder that contain data_idx in their names.

#     Parameters:
#     - data_idx (str): The EXTERNAL_SERIES_ID to search for in the filenames.
#     - path (str): The path to the folder containing the thumbnails.

#     Returns:
#     - list: A list of paths to the matching PNG files.
#     """

#     matching_files = []

#     # Ensure the path exists
#     if not os.path.exists(path):
#         print("The specified path does not exist.")
#         return matching_files

#     # Iterate over all files in the specified directory
#     for filename in os.listdir(path):
#         # Check if the file is a PNG and contains data_idx in its name
#         if filename.endswith('.png') and (data_idx in filename):
#             # Construct the full file path
#             full_path = os.path.join(path, filename)
#             matching_files.append(full_path)

#     return matching_files

#Version2: Return a list of pngs
def retrieve_thumbnail(data_idx, path):

    """
    Search for PNG files in the specified folder that contain data_idx in their names.

    Parameters:
    - data_idx (str): The EXTERNAL_SERIES_ID to search for in the filenames.
    - path (str): The path to the folder containing the thumbnails.

    Returns:
    - list: A list of PNG files.
    """

    matching_images = []

    # Ensure the path exists
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return matching_images

    # Iterate over all files in the specified directory
    for filename in os.listdir(path):
        # Check if the file is a PNG and contains data_idx in its name
        if filename.endswith('.png') and (data_idx in filename):
            # Construct the full file path
            full_path = os.path.join(path, filename)
            try:
                # Open the image and append it to the list
                img = Image.open(full_path)
                matching_images.append(img)
            except Exception as e:
                print(f"Error opening image {full_path}: {e}")

    return matching_images




