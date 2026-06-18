
from PIL import Image, ImageOps

img = Image.open(r'C:\Users\Man Bhalodiya\Desktop\t-1648985762-marwadi-university-mu-rajkot-rajkot.jpeg')
padded = ImageOps.expand(img, border=20, fill='black')

padded.show()
