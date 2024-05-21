Final CV2: Image Border Analysis Tool
final_cv2.py is an advanced Python script designed to analyze the borders of grayscale images to detect the intensity of lighting and sort images into categorized folders based on their border lighting conditions. This script is particularly useful for processing large volumes of images where automated sorting can save substantial time and effort.

Prerequisites
Before using final_cv2.py, ensure you have the following installed:

Python 3.x: The script is compatible with Python 3.
OpenCV (cv2): A library used for computer vision and image processing.
NumPy: Essential for numerical operations on image arrays.
Installation
Step 1: Install Python 3
Ensure Python 3 is installed on your system. It can be installed from the official Python website or via a package manager on Linux.

Step 2: Install OpenCV
OpenCV can be installed using pip. Run the following command:

bash
Copy code
pip install opencv-python-headless
Step 3: Install NumPy
NumPy can also be installed via pip if it's not already installed:

bash
Copy code
pip install numpy
Usage
final_cv2.py is designed to be user-friendly and can be executed from the command line. It requires a single argument: the path to the directory containing the images to be processed.

Command Format
bash
Copy code
python final_cv2.py <path_to_folder>
Arguments:
<path_to_folder>: The directory path where the TIFF images are located.
Example
To process images in a directory named 'to_be_cropped':

bash
Copy code
python3 bin/demo/final_cv2.py to_be_cropped
How It Works
Image Loading: The script loads each image in the specified directory as a grayscale image using OpenCV.
Border Analysis: Analyzes the left and right 100-pixel wide borders of each image to determine the average pixel intensity.
Classification and Sorting: Based on the intensity analysis, images are classified and moved to specific folders:
Images with both borders darker than a set threshold are moved to a 'uniform' folder.
Images with one border significantly lighter are moved to either 'left' or 'right' folders.
Directory Structure
Upon execution, final_cv2.py creates three folders within the specified directory:

@Left_Legato
@Right_Legato
@Non_Legato
Images are sorted into these directories based on the analysis results.

Troubleshooting
Ensure Dependencies Are Installed: Verify that both OpenCV and NumPy are correctly installed by running python -c "import cv2; import numpy".
Check Image Path: Ensure the specified path contains TIFF images and is correctly typed in the command.
License
final_cv2.py is released under the MIT License. This license permits free use, modification, and distribution, under the condition that the original license and copyright notice are included with any substantial portion of the software.

For the full license text, refer to the LICENSE file included with the source code.