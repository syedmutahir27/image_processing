from PIL import Image,ImageFilter

img = Image .open('pokedex/pikachu.jpg')
filtered_image = img.filter(ImageFilter.SMOOTH)
resize  = filtered_image.resize((300,300))
resize.save("resize.png",'png')
resize.show()