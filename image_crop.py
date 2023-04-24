from PIL import Image
image = Image.open('flower.jpg')
image.show()
image_cropped = image.crop((40,40,40,40))
image.show()
print(image.size)
