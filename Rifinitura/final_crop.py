import os
import sys
import warnings
from wand.image import Image

warnings.filterwarnings('ignore', message='unknown field with tag')
warnings.filterwarnings('ignore', message='.*', category=UserWarning, module='wand.*')

def crop_image(image_path, output_dir, sides, trim_pixels):
    with Image(filename=image_path) as img:
        original_width, original_height = img.width, img.height
        left, top, right, bottom = 0, 0, original_width, original_height

        for side, trim in zip(sides, trim_pixels):
            if side == 'top':
                top += trim
            elif side == 'bottom':
                bottom -= trim
            elif side == 'left':
                left += trim
            elif side == 'right':
                right -= trim

        img.crop(left, top, right, bottom)
        filename = os.path.basename(image_path)
        new_filename = f"cropped_{filename}"
        output_file_path = os.path.join(output_dir, new_filename)
        img.save(filename=output_file_path)
        print(f"Image saved as {output_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python my_image_cutter.py <path_to_image_or_directory> <output_path> <sides> <trim_pixels>")
        sys.exit(1)
    
    input_path, output_path, sides_str, trim_pixels = sys.argv[1:]
    sides = sides_str.split(',')
    trim_pixels = [int(p.strip()) for p in trim_pixels.split(',')]
    if os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            file_path = os.path.join(input_path, filename)
            if os.path.isfile(file_path):
                crop_image(file_path, output_path, sides, trim_pixels)
    elif os.path.isfile(input_path):
        crop_image(input_path, output_path, sides, trim_pixels)
    else:
        print(f"Error: {input_path} is neither a file nor a directory")
        sys.exit(1)

#python3 bin/demo/cut_magia.py to_be_cropped/ ./ "right,left" 5
#source ~/myenv/bin/activate
#identify -format "%wx%h %x x %y DPI\n" 0002.tif
