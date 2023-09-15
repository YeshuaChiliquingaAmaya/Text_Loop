from PIL import Image

def scale_image(image, new_width=300):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def grayscale_image(image):
    return image.convert('L')

def map_pixels_to_ascii(image, range_width=260/6):
    ascii_str = ' '
    ascii_chars = "Oo:./ "
    for pixel_value in image.getdata():
        ascii_str += ascii_chars[int(pixel_value // range_width)]
    return ascii_str

def convert_image_to_ascii(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    image = scale_image(image)
    image = grayscale_image(image)

    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"
    return ascii_img

# Corrige la ruta de la imagen sin comillas adicionales
ascii_image = convert_image_to_ascii(r'C:\Users\yeshu\OneDrive\Escritorio\Joke\prueba.png')

print(ascii_image)

with open('ascii_image.txt', 'w') as f:
    f.write(ascii_image)
