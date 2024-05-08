from PIL import Image,ImageFilter

image = Image.open('D:\\python_study\\python_100days\\days_15\\beautiful.jpg')
image.show()
image.filter(ImageFilter.CONTOUR).show()