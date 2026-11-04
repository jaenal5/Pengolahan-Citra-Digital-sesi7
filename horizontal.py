import cv2 
import matplotlib.pyplot as plt

# membaca gambar 
img = cv2.imread("foto.jpg")

if img is None:
    print("Gambar tidak ditemukan!")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# horizontal flip (membalik kiri ke kanan)
horizontal = cv2.flip(img, 1)

# vertical flip (membalik atas ke bawah)
vertical = cv2.flip(img, 0)

# menampilkan hasil
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(horizontal)
plt.title("Hosrizontal Flip")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(vertical)
plt.title("Vertical Flip")
plt.axis("off")

plt.tight_layout()
plt.show()