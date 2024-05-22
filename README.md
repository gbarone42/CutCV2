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

# Final CV2: Image Border Analysis Tool

**final_cv2.py** is designed to analyze the borders of grayscale images to detect the intensity of lighting and sort images into categorized folders based on their border lighting conditions.


#### Usage
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
Border Analysis: Analyzes the left and right 100-pixel wide borders of each image to determine the average pixel intensity, based on the intensity analysis, images are classified and moved to specific folders:
Images with both borders darker than a set threshold are moved to a '@Non_Legato' folder.
Images with one border significantly lighter are moved to either '@Right_Legato' or '@Left_Legato' folder.


#### Troubleshooting
Verify that both OpenCV and NumPy are correctly installed by running:
``` bash
python -c "import cv2; import numpy"
```

#### Prerequisites, ensure you have the following installed:

- OpenCV (cv2): A library used for computer vision and image processing.
- NumPy: Essential for numerical operations on image arrays.


#### Install OpenCV and NumPy

``` bash
pip install opencv-python-headless
pip install numpy
```

#### License
final_crop.py and final_cv2.py is released under the MIT License. This license allows free use, modification, and distribution, with the only requirement being to include the original license and copyright notice in any copy of the software/source code.



## Ambiente di Sviluppo

Server `mw-pvebk.bncf.lan` IP `192.168.8.19` Utente `barone`

# Virtual Env
Reason for Using Virtual Environments
Ensures consistency across development, testing, and production environments, reducing the "works on my machine" problem where code runs well in one environment but has issues in another due to differences in package versions.
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
