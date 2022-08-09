from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
# filtered_img.save("grey.png", 'png')
# print(dir(img))
# filtered_img.show()
# resize = filtered_img.resize((300, 300))
# resize.save("ResizedPikachu", 'png')
crooked = filtered_img.rotate(180)
crooked.save("crookedpikachu.png", 'png')
