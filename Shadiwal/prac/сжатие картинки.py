from PIL import Image
image_path = "C:\\Users\\shmel\\OneDrive\\Рабочий стол\\sripts_python\\Shadiwal\\prac\\gun3.png"

img = Image.open(image_path)
# изменяем размер
new_image = img.resize((60, 180))
new_image.show()
# сохранение картинки
new_image.save("C:\\Users\\shmel\\OneDrive\\Рабочий стол\\sripts_python\\Shadiwal\\prac\\gun3.png")