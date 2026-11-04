
import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("foto.jpg")

if img is None:
    print("Gambar tidak ditemukan!")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

tinggi, lebar = img.shape[:2]

# Menentukan titik pusat
pusat = (lebar // 2, tinggi // 2)

# Rotasi 45 derajat
M45 = cv2.getRotationMatrix2D(pusat, 45, 1.0)
hasil_45 = cv2.warpAffine(img, M45, (lebar, tinggi))

# Rotasi 90 derajat
M90 = cv2.getRotationMatrix2D(pusat, 90, 1.0)
hasil_90 = cv2.warpAffine(img, M90, (lebar, tinggi))

# Rotasi 180 derajat
M180 = cv2.getRotationMatrix2D(pusat, 180, 1.0)
hasil_180 = cv2.warpAffine(img, M180, (lebar, tinggi))

# Menampilkan seluruh hasil
plt.figure(figsize=(15, 8))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(hasil_45)
plt.title("Rotasi 45 Derajat")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(hasil_90)
plt.title("Rotasi 90 Derajat")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(hasil_180)
plt.title("Rotasi 180 Derajat")
plt.axis("off")

plt.tight_layout()
plt.show()
