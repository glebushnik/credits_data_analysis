import pandas as pd
import re

# Загрузка данных из CSV-файла в DataFrame
df = pd.read_csv('Dannye_o_kreditnoy_istorii_klientov.csv')

# Установка параметра отображения всех столбцов
pd.set_option('display.max_columns', None)

# Вывод первых 5 строк
# print(df.head())

print(df.describe())
