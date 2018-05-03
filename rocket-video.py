import sys
import dlib
import cv2


font = cv2.FONT_HERSHEY_COMPLEX_SMALL
pula_quadros = 15
captura = cv2.VideoCapture("recursos/video/mis-cort.avi")
contadorQuadros = 0
detector = dlib.simple_object_detector("recursos/detector_rocket.svm")

while captura.isOpened():
    conectado, frame = captura.read()
    contadorQuadros += 1
    if contadorQuadros % pula_quadros == 0:
        objetosDetectados = detector(frame, 1)
        for o in objetosDetectados:
            e, t, d, f = (int(o.left()), int(o.top()), int(o.right()), int(o.bottom()))
            cv2.rectangle(frame, (e, t), (d, f), (0, 0, 255), 2)
            cv2.putText(frame, "Rocket detected!", (e, t), font, 1, (0, 0, 255))

        cv2.imshow("Preditor de Objetos", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

captura.release()
cv2.destroyAllWindows()
sys.exit(0)