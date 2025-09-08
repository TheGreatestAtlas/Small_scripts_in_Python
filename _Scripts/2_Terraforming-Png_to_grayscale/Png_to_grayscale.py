from PIL import Image

def convert_png_to_bmp(input_path, output_path):
    """
    Converts a PNG image to BMP in 8-bit grayscale and sets the resolution to 72 DPI.
    """
    try:
        with Image.open(input_path) as img:
          
            gray_img = img.convert('L')

            gray_img.save(output_path, format='BMP', dpi=(72, 72))

            print(f"The file has been successfully saved as {output_path} in 8-bit grayscale and 72 DPI. ")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

inputfilename = str(input("Enter the name of the input file in .png format: "))
outputfilename = str(input("Enter the name of the output file in .bmp format: "))

convert_png_to_bmp(inputfilename, outputfilename)
