from PIL import Image

img = Image.open("Images/case (1).png")
area = (60, 60, 760, 520)
cropped_img = img.crop(area)
cropped_img.show()