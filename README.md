# Control Game By Hand Gesture Using KNN

## 📌 Overview
<img width="600" alt="image" src="https://github.com/user-attachments/assets/9afd9cdc-35ac-40f1-9907-23f6702cfdfe" />


Proyek ini menggunakan **MediaPipe** untuk mendeteksi gerakan tangan dan **K-Nearest Neighbors (KNN)** sebagai model klasifikasi untuk mengenali gerakan tangan yang digunakan dalam mengontrol permainan menggunakan keyboard.

Dengan menggunakan **hand landmarks** yang dideteksi oleh **MediaPipe Hands**, program ini akan mengonversi gerakan tangan menjadi tombol keyboard, seperti:
- **Up (Lompat)** → ⬆️ (panah atas)
- **Down (Rolling)** → ⬇️ (panah bawah)
- **Left (Kiri)** → ⬅️ (panah kiri)
- **Right (Kanan)** → ➡️ (panah kanan)
<img width="306" alt="image" src="https://github.com/user-attachments/assets/c900edd3-0f1f-4301-92a4-1b041a03ac25" />

## 🔧 Requirements
Pastikan Anda memiliki **Python 3.7+** dan menginstal dependensi berikut:
```bash
pip install opencv-python mediapipe pandas numpy scikit-learn pyautogui
```


## 🚀 How to Run
1. Pastikan dataset `hand_coordinate.csv` tersedia di direktori yang sama dengan skrip.
2. Jalankan program dengan perintah:
   ```bash
   python control_game_knn.py
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
│── control_game_knn.py              # Script utama untuk deteksi dan kontrol
│── README.md            # Dokumentasi proyek ini
```



---
Dibuat dengan ❤️ oleh vnyhc and team

