import cv2
import numpy as np
import sys
import os
import glob
import shutil  # For moving files

def detect_border_width(border, darkness_threshold):
    count = 0
    for i in range(border.shape[1]):
        if np.mean(border[:, i]) < darkness_threshold:
            count += 1
        else:
            break
    return count

def analyze_borders(image_path, output_folders, darkness_threshold=50, crop_threshold=20):
    print(f"Analyzing image: {image_path}")
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Failed to load:", image_path)
        return

    # Parameters for the scan
    scan_depth = 100

    # Extract borders
    left_border = image[:, :scan_depth]
    right_border = image[:, -scan_depth:]

    # Calculate the average intensity of each border
    left_intensity = np.mean(left_border)
    right_intensity = np.mean(right_border)

    # Determine if there's a particularly light side
    intensities = [left_intensity, right_intensity]
    sides = ['Left', 'Right']
    if min(intensities) < darkness_threshold:
        if left_intensity < darkness_threshold and right_intensity < darkness_threshold:
            destination_folder = output_folders['uniform']
            print(f"{os.path.basename(image_path)}: Both sides uniformly dark.")
        else:
            lightest_side = sides[np.argmax(intensities)]
            destination_folder = output_folders[lightest_side.lower()]
            print(f"{os.path.basename(image_path)}: Lightest side is {lightest_side}.")
    else:
        lightest_side = sides[np.argmax(intensities)]
        destination_folder = output_folders[lightest_side.lower()]
        print(f"{os.path.basename(image_path)}: Lightest side is {lightest_side}.")

    # Copy the file to the appropriate folder
    shutil.copy(image_path, destination_folder)

def process_folder(folder_path):
    output_folders = {
        'left': os.path.join(folder_path, "@Left_Legato"),
        'right': os.path.join(folder_path, "@Right_Legato"),
        'uniform': os.path.join(folder_path, "@Non_Legato")
    }

    # Create directories for each category
    for folder in output_folders.values():
        os.makedirs(folder, exist_ok=True)

    images = glob.glob(os.path.join(folder_path, "*.tif"))
    if not images:
        print("No images found. Check the file extension and path.")
        return
    
    for image_path in images:
        analyze_borders(image_path, output_folders)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py path_to_folder")
        sys.exit(1)
    path = sys.argv[1]
    if os.path.isdir(path):
        process_folder(path)
    else:
        print("Invalid path provided. Please provide a directory path.")
        sys.exit(1)

		#python3 bin/demo/2cv2.py to_be_cropped
		#source ~/myenv/bin/activate