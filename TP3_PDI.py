import cv2
import numpy as np
import matplotlib.pyplot as plt

def imshow(img, new_fig=True, title=None, color_img=False, blocking=False, colorbar=True, ticks=False):
    if new_fig:
        plt.figure()
    if color_img:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap='gray')
    plt.title(title)
    if not ticks:
        plt.xticks([]), plt.yticks([])
    if colorbar:
        plt.colorbar()
    if new_fig:        
        plt.show(block=blocking)

def detectar_lineas_carril(frame, width, height):
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gris, (5, 5), 0)
    bordes = cv2.Canny(blur, 50, 150)

    # Clausura morfológica
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    clausura = cv2.morphologyEx(bordes, cv2.MORPH_CLOSE, kernel)

    # Región de interés
    mascara = np.zeros_like(clausura)
    poligono = np.array([[
        (int(0.1 * width), height),
        (int(0.45 * width), int(0.6 * height)),
        (int(0.55 * width), int(0.6 * height)),
        (int(0.9 * width), height)
    ]], np.int32)
    cv2.fillPoly(mascara, poligono, 255)
    recorte = cv2.bitwise_and(clausura, mascara)

    lineas = cv2.HoughLinesP(recorte, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=150)
    if lineas is not None:
        for linea in lineas:
            x1, y1, x2, y2 = linea[0]
            pendiente = (y2 - y1) / (x2 - x1 + 1e-6)
            if abs(pendiente) > 0.5:
                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
    return frame

def procesar_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = detectar_lineas_carril(frame, width, height)
        cv2.imshow(f'Procesando: {video_path}', frame)
        out.write(frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

ruta = "C:/Users/Usuario/PDI1/tp3"

ruta_video_1 = f"{ruta}/ruta_1.mp4"
ruta_video_2 = f"{ruta}/ruta_2.mp4"

procesar_video(f"{ruta}/ruta_1.mp4", f"{ruta}/video_lineas_carril_1.mp4")
procesar_video(f"{ruta}/ruta_2.mp4", f"{ruta}/video_lineas_carril_2.mp4")
