from PIL import Image


def decoding_an_image(path):
    # Open the image
    try:
        img = Image.open(path)
    except:
        print("Wrong path!")
        return
    width = img.width
    height = img.height

    my_string = ''
    # Goes over all pixels
    for i in range(0, width):
        for j in range(0, height):
            # Check if pixel is black
            if img.getpixel((i, j)) == 1:
                # Convert the line number of black pixel to character by ASCII value
                my_string += chr(j)

    return my_string


print(decoding_an_image('code.png'))
