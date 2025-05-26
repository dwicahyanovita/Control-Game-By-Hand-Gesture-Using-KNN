import cv2
import mediapipe as mp
import pandas as pd
import numpy as np
import pyautogui
import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils.class_weight import compute_class_weight

# pemetaan label ke deskripsi gesture
gesture_map = {
    'up' : "Lompat",
    'down' : "Menggelinding",
    'left' : "Kiri",
    'right' : "Kanan",
    'no_action' : "No_Action"
}

# Membaca file CSV yang berisi koordinat tangan
data = pd.read_csv('hand_coordinate.csv')

# Memisahkan fitur (x) dan label (y)
X = data.drop('label', axis=1)
y = data['label']

# Mengambil  fitur dan label dari dataset yang telah diseimbangkan
X_balanced = data.drop('label', axis=1).values
y_balanced = data['label'].values

# Menghitung bobot masing-masing kelas secara otomatis agar model tidak bias
class_weights = compute_class_weight('balanced', classes=np.unique(y_balanced), y=y_balanced)
weights_dict = {cls: weight for cls, weight in zip(np.unique(y_balanced), class_weights)}

# Membuat dan melatih model KNN
model = KNeighborsClassifier(n_neighbors=5, weights='distance')
model.fit(X_balanced, y_balanced)

# Insialisasi MediaPipe Hands untuk deteksi tangan
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Membuka kamera
cap = cv2.VideoCapture(0)

last_prediction = 'no_action'
last_action_time = 0
gesture_delay = 1
distance_threshold = 0.4

# Loop utama untuk pengenalan gesture secara real_time
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Konversi frame ke format RGB untuk Mediapipe
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    
    # Proses deteksi tangan
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # jika ada tangan yang terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            #gambar garis koneksi antar titik tangan
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Ekstraksi koordinat dari titik-titik tangan
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
                
            # Konversi ke array numpy dan reshape sesuai input model
            landmarks = np.array(landmarks).reshape(1, -1)
            
            distances, _ = model.kneighbors(landmarks)
            average_distance = np.mean(distances)
            
            if average_distance > distance_threshold:
                prediction = 'no_action'
            else :
            # Predisksi gesture dari input tangan
                prediction = model.predict(landmarks)[0]
            
            # Mapping hasil prediksi ke nama gesture
            gesture_name = gesture_map.get(prediction, "Tidak Diketahui")
            
            # Tampilkan hasil prediksi pada layar
            cv2.putText(image, f'Gesture: {gesture_name}', (10,540), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 200, 100), 5)
            cv2.putText(image, f'Distance : {average_distance:.2f}', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 255), 2)
            current_time = time.time()
            

            if prediction != last_prediction or ( current_time - last_action_time > gesture_delay):
                # Kontrol ke keyboard
                if gesture_name == 'Lompat':
                    pyautogui.press('w')
                elif gesture_name == 'Menggelinding':
                    pyautogui.press('s')
                elif gesture_name == 'Kiri':
                    pyautogui.press('a')
                elif gesture_name == 'Kanan':
                    pyautogui.press('d')
            
                last_action_time = current_time
            
            last_prediction = prediction
        else:
            last_prediction = 'no_action'
            
    # Tampilkan hasil deteksi di jendela OpenCV
    cv2.imshow('Control Game by Hand Gesture', image)
        
    # Tekan tombol "q" untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    # Tutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()