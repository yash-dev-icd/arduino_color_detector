import cv2
import numpy as np
import serial
import time

# Configurar la conexión serial con el Arduino
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

pointerX, pointerY = 320, 240  # Centro de una imagen de 640x480

def get_color_name(h, s, v):
    if s < 50 and v > 50:
        return "White"
    elif s < 50:
        return "Black"
    elif h < 10 or h > 160:
        return "Red"
    elif 10 <= h < 25:
        return "Orange"
    elif 25 <= h < 35:
        return "Yellow"
    elif 35 <= h < 85:
        return "Green"
    elif 85 <= h < 115:
        return "Cyan"
    elif 115 <= h < 160:
        return "Blue"
    return "Undefined"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Obtener el color del píxel en la posición fija del puntero
    b, g, r = frame[pointerY, pointerX]
    hsv = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)
    h, s, v = hsv[0][0]
    color_name = get_color_name(h, s, v)

    # Enviar el nombre del color al Arduino
    arduino.write(f'{color_name}\n'.encode())
    time.sleep(0.1)  # Añadir una pequeña pausa para la comunicación

    # Mostrar la posición fija del puntero y el color detectado
    cv2.putText(frame, f'Color: {color_name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.circle(frame, (pointerX, pointerY), 5, (255, 255, 255), -1)

    cv2.imshow("Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
