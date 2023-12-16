from PIL import Image

img = Image.open("lib_pillow/image_test.jpg")

# displaying image
# img.show()

# basic cmds
print(img.filename)  # lib_pillow/pexels-fallgregg-10395309.jpg
print(img.size)  # (2075, 3130)
print(img.format)  # JPEG
print(img.mode)  # RGB

# resizing image
# resized_img = img.resize((250, 300))
# resized_img.show()

# resizing image with percentage
resized_img = img.resize((round(img.width * 0.5), round(img.height * 0.5)))
resized_img.show()
print(resized_img.size)
