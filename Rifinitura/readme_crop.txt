Final Crop
final_crop.py is a versatile Python script designed for cropping images. Utilizing the Wand library, a Python binding for ImageMagick, this tool enables precise cropping from any of the four sides (top, bottom, left, right) of an image. The script can handle individual files or process an entire directory of images, making it suitable for both single edits and batch processing tasks.

Prerequisites
Before using final_crop.py, ensure you have the following installed:

Python 3.x: The script is compatible with Python 3. Ensure Python 3 is installed on your system.
ImageMagick: This is a dependency for Wand, used for image manipulation.
Wand: A Python library that provides the bindings for ImageMagick.
Installation
Step 1: Install ImageMagick
ImageMagick must be installed first since it is required by the Wand library. Installation instructions vary based on the operating system:

For Ubuntu/Debian:
bash
Copy code
sudo apt-get install imagemagick
For other operating systems:
Please refer to the ImageMagick documentation for installation instructions.

Step 2: Install Wand
After installing ImageMagick, install Wand using pip:

bash
Copy code
pip install wand
Usage
final_crop.py is designed to be straightforward and user-friendly. The following details how to use the script:

Command Format
bash
Copy code
python final_crop.py <path_to_image_or_directory> <output_path> <sides> <trim_pixels>
Arguments:
<path_to_image_or_directory>: The file path to an image or a directory containing images.
<output_path>: The directory where cropped images will be stored.
<sides>: Comma-separated list of sides from which to crop the image. Valid options include 'top', 'bottom', 'left', 'right'.
<trim_pixels>: The number of pixels to trim from each specified side.
Examples
Cropping a Single Image
To crop 10 pixels from the top of example.jpg and save the cropped image in the current directory:

bash
Copy code
python final_crop.py example.jpg ./ "top" 10
Processing Multiple Images in a Directory
To crop 20 pixels from the bottom of each image in /path/to/images and save them in /path/to/output:

bash
Copy code
python final_crop.py /path/to/images /path/to/output "bottom" 20
Troubleshooting
Check ImageMagick Installation: Ensure that ImageMagick is correctly installed and accessible in your system's PATH.
Verify Wand Installation: Confirm that Wand is installed correctly by running:
bash
Copy code
python -c "import wand"
License
final_crop.py is released under the MIT License. This license allows free use, modification, and distribution, with the only requirement being to include the original license and copyright notice in any copy of the software/source code.

For detailed license terms, see the LICENSE file.

This README provides comprehensive guidance on installation, usage, and troubleshooting, tailored to be useful for both beginners and experienced users alike. If you have any additional features or specific configurations you would like detailed in this document, feel free to let me know!