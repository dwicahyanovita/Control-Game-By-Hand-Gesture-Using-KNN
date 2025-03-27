# Control Game By Hand Gesture Using KNN

## 📌 Overview
Proyek ini menggunakan **MediaPipe** untuk mendeteksi gerakan tangan dan **K-Nearest Neighbors (KNN)** sebagai model klasifikasi untuk mengenali gerakan tangan yang digunakan dalam mengontrol permainan menggunakan keyboard.

Dengan menggunakan **hand landmarks** yang dideteksi oleh **MediaPipe Hands**, program ini akan mengonversi gerakan tangan menjadi tombol keyboard, seperti:
- **Up (Lompat)** → ⬆️ (panah atas)
- **Down (Rolling)** → ⬇️ (panah bawah)
- **Left (Kiri)** → ⬅️ (panah kiri)
- **Right (Kanan)** → ➡️ (panah kanan)

## 🔧 Requirements
Pastikan Anda memiliki **Python 3.7+** dan menginstal dependensi berikut:
```bash
pip install opencv-python mediapipe pandas numpy scikit-learn pyautogui
```

## 📂 Dataset
Gunakan dataset **hand_coordinate.csv** yang berisi koordinat tangan dari MediaPipe serta label gerakannya.
Struktur dataset:
```
user, sex, frame, hand, distance, x1, y1, z1, ..., x21, y21, z21, label
```
Kolom **user, sex, frame, hand, distance** akan dihapus karena tidak diperlukan dalam proses klasifikasi.

## 🚀 How to Run
1. Pastikan dataset `hand_coordinate.csv` tersedia di direktori yang sama dengan skrip.
2. Jalankan program dengan perintah:
   ```bash
   python main.py
   ```
3. Program akan membuka kamera dan menampilkan deteksi tangan secara real-time.
4. Lakukan gerakan tangan untuk mengontrol permainan!
5. Tekan `q` untuk keluar dari aplikasi.

## 🖥️ Features
✅ Menggunakan **MediaPipe** untuk mendeteksi tangan secara real-time.  
✅ Menggunakan **KNN** sebagai model klasifikasi gerakan tangan.  
✅ Mengontrol game dengan gerakan tangan tanpa perlu perangkat tambahan.  
✅ Dapat digunakan untuk berbagai aplikasi seperti **game** atau **navigasi aplikasi**.

## ⚙️ Code Structure
```
Control-Game-By-Hand-Gesture-Using-KNN/
│── hand_coordinate.csv  # Dataset koordinat tangan
│── main.py              # Script utama untuk deteksi dan kontrol
│── README.md            # Dokumentasi proyek ini
```



---
Dibuat dengan ❤️ oleh vnyhc

