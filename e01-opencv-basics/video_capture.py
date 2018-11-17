import cv2
cap = cv2.VideoCapture(0)

while(True):
    # Получить очередной кадр
    ret, frame = cap.read()

    # Преобразовать в ч/б
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    

    # Нарисовать подсказку о выходе
    cv2.putText(gray, "Press `q` to quit", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, 0)

    # Показать
    cv2.imshow('Video Capture Test',gray)

    # Если нажата q, выйти, иначе начать снова
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Закрыть камеру и окна 
cap.release()
cv2.destroyAllWindows()
