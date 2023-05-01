from PIL import Image
import os


def decoding_an_image(path):
    # Open the image
    if os.path.exists(path):
        img = Image.open(path)
        width = img.width
        height = img.height

        my_string = ''.join([chr(row) for column in range(0, width) for row in range(0, height)
                            if img.getpixel((column, row)) == 1])

        return my_string
    else:
        print("Wrong path!")


if __name__ == "__main__":
    print(decoding_an_image('code1.png'))
