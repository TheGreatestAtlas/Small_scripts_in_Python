from PIL import Image
import sys

def apply_border(bitmap_path, border_path, output_path):
    """
    Applies a border to a bitmap while preserving the parameters of the input image.
    """
    try:
        # Open the bitmap and read its parameters
        bitmap = Image.open(bitmap_path)
        original_format = bitmap.format
        original_mode = bitmap.mode
        original_size = bitmap.size

        # Convert bitmap to RGBA for operations (restore at the end)
        bitmap = bitmap.convert("RGBA")

        # Open the frame and adjust the size
        border = Image.open(border_path).convert("RGBA")
        border = border.resize(original_size)

        # Applying a border to a bitmap
        result = Image.alpha_composite(bitmap, border)

        # Convert the result to the original mode (if possible)
        if original_mode != "RGBA":
            result = result.convert(original_mode)

        # Save the resulting image in its original format
        result.save(output_path, format=original_format)
        print(f"The image was saved in: {output_path}")

    except Exception as e:
        print(f"An error has occurred: {e}")

# Example of use
try:
    bitmap_path = sys.argv[1]
    border_path = sys.argv[2]
    output_path = sys.argv[3]
except:
    bitmap_path = str(input("Provide the path to the bitmap file: "))  # Specify the path to the bitmap file
    border_path = str(input("Provide the path to the file with the border: "))  # Specify the path to the file with the border
    output_path = str(input("Specify the path to the output file: "))  # Specify the path to the output file

apply_border(bitmap_path, border_path, output_path)
