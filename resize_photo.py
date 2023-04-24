from PIL import Image


image = Image.open('flower_blurred.jpg')
width, height = image.size
resized_image = image.resize((400,800))
resized_image.show()
resized_image.save("resized_flower.jpg")
