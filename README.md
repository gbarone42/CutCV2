# CutCV2

#### Rifinitura bordo scuro

# Final Crop : Image Cropper Tool

**`final_crop.py`** is a versatile Python script designed for cropping images. Utilizing the Wand library, a Python binding for ImageMagick, this tool enables precise cropping from any of the four sides (top, bottom, left, right) of an image. The script can handle individual files or process an entire directory of images, making it suitable for both single edits and batch processing tasks.

#### Prerequisites
Before using `final_crop.py`, ensure you have the following installed:

- Python 3.x: The script is compatible with Python 3. Ensure Python 3 is installed on your system.
- ImageMagick: This is a dependency for Wand, used for image manipulation.
- Wand: A Python library that provides the bindings for ImageMagick.

#### Installation

#### Step 1: Install ImageMagick
ImageMagick must be installed first since it is required by the Wand library. Installation instructions vary based on the operating system:

For Ubuntu/Debian:
``` bash
sudo apt-get install imagemagick
```
For other operating systems:
Please refer to the ImageMagick documentation for installation instructions.

#### Step 2: Install Wand
After installing ImageMagick, install Wand using pip:
``` bash
pip install wand
```

#### Usage
final_crop.py is designed to be straightforward and user-friendly. The following details how to use the script:

#### Command Format

``` bash
python final_crop.py <path_to_image_or_directory> <output_path> <sides> <trim_pixels>
```





#### Arguments:

- <path_to_image_or_directory>: The file path to an image or a directory containing images.
- <output_path>: The directory where cropped images will be stored.
- <sides>: Comma-separated list of sides from which to crop the image. Valid options include 'top', 'bottom', 'left', 'right'.
- <trim_pixels>: The number of pixels to trim from each specified side.

#### Examples
Cropping a Single Image
To crop 10 pixels from the top of example.jpg and save the cropped image in the current directory:

``` bash
python final_crop.py example.jpg ./ "top" 10
```

``` bash
python final_crop.py /path/to/images /path/to/output "bottom" 20
```



#### Troubleshooting
Check ImageMagick Installation: Ensure that ImageMagick is correctly installed and accessible in your system's PATH.
Verify Wand Installation: Confirm that Wand is installed correctly by running:

``` bash
python -c "import wand"
```








# 
# Final CV2: Image Border Analysis Tool

**final_cv2.py** is an advanced Python script designed to analyze the borders of grayscale images to detect the intensity of lighting and sort images into categorized folders based on their border lighting conditions. This script is particularly useful for processing large volumes of images where automated sorting can save substantial time and effort.

## Prerequisites
Before using `final_cv2.py`, ensure you have the following installed:

- Python 3.x: The script is compatible with Python 3.
- OpenCV (cv2): A library used for computer vision and image processing.
- NumPy: Essential for numerical operations on image arrays.

## Installation
### Step 1: Install Python 3
Ensure Python 3 is installed on your system. It can be installed from the official Python website or via a package manager on Linux.

### Step 2: Install OpenCV
OpenCV can be installed using pip. Run the following command:

``` bash
pip install opencv-python-headless
```

#### Step 3: Install NumPy
NumPy can also be installed via pip if it's not already installed:
``` bash
pip install numpy
```

#### Usage
final_cv2.py is designed to be user-friendly and can be executed from the command line. It requires a single argument: the path to the directory containing the images to be processed.

#### Command Format
``` bash
python final_cv2.py <path_to_folder>
```

#### Arguments:
<path_to_folder>: The directory path where the TIFF images are located.

#### Example
To process images in a directory named 'to_be_cropped':
``` bash
python3 bin/demo/final_cv2.py to_be_cropped
```

#### How It Works
Image Loading: The script loads each image in the specified directory as a grayscale image using OpenCV.
Border Analysis: Analyzes the left and right 100-pixel wide borders of each image to determine the average pixel intensity.
Classification and Sorting: Based on the intensity analysis, images are classified and moved to specific folders:
Images with both borders darker than a set threshold are moved to a 'uniform' folder.
Images with one border significantly lighter are moved to either 'left' or 'right' folders.

#### Directory Structure
Upon execution, final_cv2.py creates three folders within the specified directory:

@Left_Legato
@Right_Legato
@Non_Legato
Images are sorted into these directories based on the analysis results.

#### Troubleshooting
Ensure Dependencies Are Installed: Verify that both OpenCV and NumPy are correctly installed by running:
``` bash
python -c "import cv2; import numpy"
```


#### License
final_crop.py and final_cv2.py is released under the MIT License. This license allows free use, modification, and distribution, with the only requirement being to include the original license and copyright notice in any copy of the software/source code.



## Ambiente di Sviluppo

Server `mw-pvebk.bncf.lan` IP `192.168.8.19` Utente `barone`
