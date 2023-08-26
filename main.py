from PIL import Image

im = Image.open(("wallpaper.jpg"))
print(im.size)
newsize = im.resize((1080, 1920))
newsize.show()