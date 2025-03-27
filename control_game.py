import cv2
import mediapipe as mp
import pandas as pd
import numpy as np
import pyautogui
from sklearn.neighbors import KNeighborsClassifier

# Peta label menjadi nama gerakan
gesture_map = {
    'no_action': "No_Action",
    'up': "Lompat",
    'down': "Rolling",
    'left': "Kiri",
    'right': "Kanan",
}

# Membaca dataset CSV
data = pd.read_csv('hand_coordinate.csv')

# Menghapus kolom yang tidak diperlukan
columns_to_ignore = ['user', 'sex', 'frame', 'hand', 'distance']
data = data.drop(columns=columns_to_ignore, errors='ignore')

# Memisahkan fitur (X) dan label (y)
X = data.drop('label', axis=1).values
y = data['label'].values

# Membuat dan melatih model KNN
model = KNeighborsClassifier(n_neighbors=5, weights='distance')
model.fit(X, y)

# Konfigurasi MediaPipe Hands untuk deteksi tangan
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Membuka kamera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Konversi frame ke RGB untuk diproses oleh MediaPipe
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Mengambil koordinat landmark tangan
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            # Mengubah daftar koordinat menjadi array numpy
            landmarks = np.array(landmarks).reshape(1, -1)

            # Memprediksi gerakan menggunakan model KNN
            prediction = model.predict(landmarks)[0]
            gesture_name = gesture_map.get(prediction, "No_Action")

            # Menampilkan prediksi di layar
            cv2.putText(image, f'Label: {gesture_name}', (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Mengontrol keyboard berdasarkan prediksi gerakan
            if gesture_name == "Lompat":
                pyautogui.press('up')
            elif gesture_name == "Rolling":
                pyautogui.press('down')
            elif gesture_name == "Kiri":
                pyautogui.press('left')
            elif gesture_name == "Kanan":
                pyautogui.press('right')

    # Menampilkan gambar dengan hasil deteksi
    cv2.imshow('Hand Gesture Recognition', image)

    # Keluar dari program dengan menekan tombol "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Menutup kamera dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
