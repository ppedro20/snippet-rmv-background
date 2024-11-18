from rembg import remove
from PIL import Image

url = Image.open('photos/IMG_0996.jpg')
output = remove(url)
output.save('output.png')