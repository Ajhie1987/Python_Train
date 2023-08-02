import numpy as np

matrik_a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

matrik_b = np.array([
    [3,2,1],
    [6,5,4],
    [9,8,7]
])

tambah = matrik_a + matrik_b
kurang = matrik_a - matrik_b
kali = matrik_a*matrik_b
bagi = matrik_a/matrik_b
balik = matrik_a.transpose()

print("hasil tambah matrik")
print(tambah)
print("hasil kurang matrik")
print(kurang)
print("hasil kali matrik")
print(kali)
print("hasil bagi matrik")
print(bagi)
print("hasil balik matrik")
print(balik)