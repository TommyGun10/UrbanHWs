import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# 'Requeses' Вызываем API изображений кошек и котов
req = requests.get("https://api.thecatapi.com/v1/images/search?limit=10")
print(req.text)


# 'Pandas' Создание DataFrame с помощью Pandas
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print(df)


# 'Numpy' создаем матрицу с помощью NumPy
matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix)


# 'Matplotlib' Создаем график с помощью matplotlib
vals = [50, 30, 10, 8, 2]
labels = ["Меллстрой", "Моргенштерн", "Мухаммед Али", "Леонардо да Винчи", "Фридрих Ницше"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Статистика узнаваимости известных личностей в России")
plt.show()


# 'Pillow' Создаем пустое изображение с зеленым фоном с помощью Pillow
im = Image.new('RGB', (500, 300), (122, 193, 27))
draw = ImageDraw.Draw(im)
im.show()







