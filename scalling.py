
import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("foto.jpg")

if img is None:
    print("Gambar tidak ditemukan!")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Scaling faktor 0.5 (memperkecil)
hasil_05 = cv2.resize(
    img,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv2.INTER_LINEAR
)

# Scaling faktor 2 (memperbesar)
hasil_2 = cv2.resize(
    img,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_LINEAR
)

# Menampilkan informasi ukuran
print("Ukuran gambar asli:", img.shape)
print("Ukuran scaling 0.5:", hasil_05.shape)
print("Ukuran scaling 2:", hasil_2.shape)

# Menampilkan gambar
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(hasil_05)
plt.title("Scaling 0.5")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(hasil_2)
plt.title("Scaling 2")
plt.axis("off")

plt.tight_layout()
plt.show()
