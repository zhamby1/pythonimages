from PIL import Image
from PIL import ImageFilter

image = Image.open('flower_blurred.jpg')
image.filter(ImageFilter.BLUR)
image.save("flower_blurred2.jpg")
image.show()
