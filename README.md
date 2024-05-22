# CutCV2

#### Rifinitura bordo scuro ImageMagick

###### Prerequisites - Python 3.x: The script is compatible with Python 3. Ensure Python 3 is installed on your system.

# Image Cropper Tool
**`final_crop.py`** is a Python script designed for cropping images.




#### Usage
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

``` bash
python final_crop.py example.jpg ./ "top" 10
python final_crop.py /path/to/images /path/to/output "bottom" 20
python final_crop.py example.jpg ./ "top,bottom" 10,20
python final_crop.py /path/to/image.jpg /path/to/output top,bottom,left,right 10,15,5,20

```

###### The output is formatted to show the width and height in pixels followed by the horizontal and vertical DPI
``` bash
identify -format "%wx%h %x x %y DPI\n" exampleimage.tif
``` 

#### Prerequisites, ensure you have the following installed:

- ImageMagick: This is a dependency for Wand, used for image manipulation.
- Wand: A Python library that provides the bindings for ImageMagick.

#### Installation

#### Step 1: Install ImageMagick

``` bash
sudo apt-get install imagemagick
```

#### Step 2: Install Wand
``` bash
pip install wand
```

#### Troubleshooting

``` bash
python -c "import wand"
```

#### License
final_crop.py and final_cv2.py is released under the MIT License. This license allows free use, modification, and distribution, with the only requirement being to include the original license and copyright notice in any copy of the software/source code.



# Final CV2: Image Border Analysis Tool

**final_cv2.py** is designed to analyze the borders of grayscale images to detect the intensity of lighting and sort images into categorized folders based on their border lighting conditions.

#### Prerequisites, ensure you have the following installed:

- OpenCV (cv2): A library used for computer vision and image processing.
- NumPy: Essential for numerical operations on image arrays.

## Installation

### Install OpenCV
Run the following command:

``` bash
pip install opencv-python-headless
```

### Install NumPy

``` bash
pip install numpy
```


#### Imports and Dependencies
- cv2: This is the OpenCV library used for image processing.
- numpy: Used for numerical operations on arrays.
- sys: To interact with the system (used here for command-line arguments).
- os: To interact with the operating system, particularly for file and directory operations.
- glob: To find all the pathname matching a specified pattern.
- shutil: Used for high-level file operations, such as copying files.

#### Usage
It requires a single argument from the command line: the path to the directory containing the images to be processed.

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
Verify that both OpenCV and NumPy are correctly installed by running:
``` bash
python -c "import cv2; import numpy"
```

#### License
final_crop.py and final_cv2.py is released under the MIT License. This license allows free use, modification, and distribution, with the only requirement being to include the original license and copyright notice in any copy of the software/source code.



## Ambiente di Sviluppo

Server `mw-pvebk.bncf.lan` IP `192.168.8.19` Utente `barone`


# Virtual Env

Using a virtual environment in Python development, such as through commands like source ~/venv/bin/activate or source ~/myenv/bin/activate, is a widely adopted practice. Here’s why developers use virtual environments and the benefits they offer:

Reason for Using Virtual Environments

Ensures consistency across development, testing, and production environments, reducing the "works on my machine" problem where code runs well in one environment but has issues in another due to differences in package versions.

With virtual environments, you can easily add, update, or remove packages without risking the integrity of other projects or the system-wide Python installation.

When working in a team, virtual environments ensure that all developers work with the same setup, making it easier to share code and minimize conflicts. Typically, a requirements.txt file is used alongside the virtual environment to keep track of the project's dependencies.

Virtual environments allow users to install new packages and manage existing ones without needing administrative access. This is especially useful in shared or managed computing environments.

Creating and Activating a Virtual Environment


Install the virtualenv Package (if it’s not installed):

``` bash
pip install virtualenv
```
Create a Virtual Environment:

You can create a virtual environment using the following command:
``` bash
python -m venv ~/myenv
```
This command creates a new directory (myenv) in your home directory containing the virtual environment.
Activate the Virtual Environment:

To activate the virtual environment on a Unix or macOS system, use:
``` bash
source ~/myenv/bin/activate
```

Deactivate:

Once you are done working within the virtual environment, you can deactivate it using:
``` bash
deactivate
```
