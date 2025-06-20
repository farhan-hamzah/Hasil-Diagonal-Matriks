import numpy as np
row = int(input())
data = []
for i in range(row):
    baris = list(map(int, input().split()))
    data.append(baris)
matriks = np.array(data)
hasil1 = np.trace(matriks)
hasil = 0
for i in range(row):
    j = row - 1 - i  # Kolom pada diagonal samping kiri
    hasil += matriks[i][j]
print(hasil+hasil1)

