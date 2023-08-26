from PIL import Image

im = Image.open(("Name of your image file"))
print(im.size)
newsize = im.resize(("Select Size. Example '1920, 1080'"))
newsize.show()
