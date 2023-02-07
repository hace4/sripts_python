from PIL import Image
image_path = "C:\\Users\\chels\\Desktop\\Прак срак\\gun.png"

img = Image.open(image_path)
# изменяем размер
new_image = img.resize((120, 24))
new_image.show()
# сохранение картинки
new_image.save("C:\\Users\\chels\\Desktop\\Прак срак\\gun1.png")