import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'DejaVu Sans'

print("=" * 60)
print("ЗАДАНИЕ 1: ГЕНЕРАЦИЯ ДАННЫХ")
print("=" * 60)

np.random.seed(42)

data = np.random.randint(-10000, 10001, 1000)

series = pd.Series(data)

print(f"Сгенерировано {len(series)} чисел")
print(f"Первые 10 значений Series:\n{series.head(10)}")
print(f"Тип данных: {series.dtype}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: РАСЧЕТ СТАНДАРТНЫХ ЧИСЛОВЫХ ХАРАКТЕРИСТИК")
print("=" * 60)

min_value = series.min()
print(f"1. Минимальное значение: {min_value}")

max_value = series.max()
print(f"2. Максимальное значение: {max_value}")

sum_value = series.sum()
print(f"3. Сумма всех значений: {sum_value}")

duplicates_count = series.duplicated().sum()
print(f"4. Количество повторяющихся значений: {duplicates_count}")

std_value = series.std()
print(f"5. Среднеквадратическое отклонение: {std_value:.4f}")

print(f"\nДополнительные характеристики:")
print(f"Среднее значение: {series.mean():.4f}")
print(f"Медиана: {series.median()}")
print(f"Количество уникальных значений: {series.nunique()}")


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: ВИЗУАЛИЗАЦИЯ ДАННЫХ")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(series.head(100).index, series.head(100).values,
             color='blue', linewidth=1, marker='o', markersize=2)
axes[0].set_title('Линейный график (первые 100 значений)', fontsize=12)
axes[0].set_xlabel('Индекс')
axes[0].set_ylabel('Значение')
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=0, color='black', linestyle='-', linewidth=0.5)

rounded_data = np.round(series.values / 100) * 100
axes[1].hist(rounded_data, bins=30, color='green', edgecolor='black', alpha=0.7)
axes[1].set_title('Гистограмма распределения значений (с округлением до сотен)', fontsize=12)
axes[1].set_xlabel('Значения (округленные до сотен)')
axes[1].set_ylabel('Частота')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('visualization_1.png', dpi=150, bbox_inches='tight')
plt.show()

print("Графики сохранены в файл 'visualization_1.png'")


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: ФОРМИРОВАНИЕ DATAFRAME")
print("=" * 60)

df = pd.DataFrame({
    'Исходные_данные': series
})

df['Сортировка_по_возрастанию'] = df['Исходные_данные'].sort_values().values

df['Сортировка_по_убыванию'] = df['Исходные_данные'].sort_values(ascending=False).values

print(f"Создан DataFrame размером {df.shape}")
print(f"\nПервые 10 строк DataFrame:")
print(df.head(10))

print(f"\nИнформация о DataFrame:")
print(df.info())


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: ВИЗУАЛИЗАЦИЯ ОТСОРТИРОВАННЫХ ДАННЫХ")
print("=" * 60)

plt.figure(figsize=(12, 6))

plt.plot(df['Сортировка_по_возрастанию'].values,
         color='red', linewidth=1.5, label='Сортировка по возрастанию')

plt.plot(df['Сортировка_по_убыванию'].values,
         color='blue', linewidth=1.5, label='Сортировка по убыванию')

plt.title('Сравнение отсортированных значений (возрастание vs убывание)', fontsize=14)
plt.xlabel('Индекс после сортировки')
plt.ylabel('Значение')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.savefig('visualization_2.png', dpi=150, bbox_inches='tight')
plt.show()

print("График сохранен в файл 'visualization_2.png'")


print("\n" + "=" * 60)
print("ИТОГОВАЯ СТАТИСТИКА")
print("=" * 60)

print(f"\nОсновные характеристики Series:")
print(f"  - Количество элементов: {len(series)}")
print(f"  - Минимальное значение: {min_value}")
print(f"  - Максимальное значение: {max_value}")
print(f"  - Сумма всех значений: {sum_value}")
print(f"  - Среднее значение: {series.mean():.4f}")
print(f"  - Медиана: {series.median()}")
print(f"  - Среднеквадратическое отклонение: {std_value:.4f}")
print(f"  - Количество повторяющихся значений: {duplicates_count}")
print(f"  - Количество уникальных значений: {series.nunique()}")

print("\n" + "=" * 60)
print("ВЫПОЛНЕНИЕ ВСЕХ ЗАДАНИЙ ЗАВЕРШЕНО!")
print("=" * 60)