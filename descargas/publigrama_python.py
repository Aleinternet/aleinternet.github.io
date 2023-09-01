

import serial
import time
import cv2
import threading

def enviar_numero_a_arduino(numero):
    arduino.write(str(numero).encode())
    time.sleep(2)

def reproducir_video(ruta_video):
    cap = cv2.VideoCapture(ruta_video)

    # Verificar si se puede abrir el video
    if not cap.isOpened():
        print("Error al abrir el video.")
        return

    # Obtener dimensiones de la ventana de video
    window_name = "Reproduciendo video"
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()

        if not ret:
            # Fin del video, salir de la reproducción
            break

        # Mostrar el fotograma en pantalla completa
        cv2.imshow(window_name, frame)

        # Esperar 30 ms y verificar si se presionó la tecla 'q' para salir
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        if valor_anterior != valor:
            break

    # Cerrar ventana al finalizar la reproducción
    cv2.destroyAllWindows()

# Función para reproducir el video en un hilo separado
def reproducir_video_thread(ruta_video):
    thread = threading.Thread(target=reproducir_video, args=(ruta_video,))
    thread.start()
    return thread

# Configurar comunicación con Arduino
arduino = serial.Serial("COM5", 9600)
time.sleep(2)

# Rutas de los videos
ruta_rojo = r'D:\Baul\Ale_UAI_Cosas\2023\2do semestre\Taller_prod_Caaro_pino_fran\E07_publicida\Final\Videos\2vid_rojo.mp4'
ruta_verde = r'D:\Baul\Ale_UAI_Cosas\2023\2do semestre\Taller_prod_Caaro_pino_fran\E07_publicida\Final\Videos\2vid_verde.mp4'
ruta_azul = r'D:\Baul\Ale_UAI_Cosas\2023\2do semestre\Taller_prod_Caaro_pino_fran\E07_publicida\Final\Videos\2vid_azul.mp4'
ruta_amarilla = r'D:\Baul\Ale_UAI_Cosas\2023\2do semestre\Taller_prod_Caaro_pino_fran\E07_publicida\Final\Videos\2vid_amarillo.mp4'
ruta_morada = r'D:\Baul\Ale_UAI_Cosas\2023\2do semestre\Taller_prod_Caaro_pino_fran\E07_publicida\Final\Videos\2vid_morado.mp4'
ruta_cian = r'D:\Baul\Ale_UAI_Cosas\2023\2do semestre\Taller_prod_Caaro_pino_fran\E07_publicida\Final\Videos\2vid_cian.mp4'
ruta_blanco = r'D:\Baul\Ale_UAI_Cosas\2023\2do semestre\Taller_prod_Caaro_pino_fran\E07_publicida\Final\Videos\2vid_blanco.mp4'

# Inicializar el valor anterior
valor_anterior = None
video_thread = None

while True:
    valor = arduino.readline().decode('utf-8').strip()
    print(valor)

    # Interrumpir el video en curso si se recibe un nuevo valor
    if video_thread is not None and video_thread.is_alive():
        video_thread.join()  # Esperar a que el hilo de reproducción termine
        cv2.destroyAllWindows()

    if valor == valor_anterior:
        # Si el valor es igual al valor anterior, reproducir el video actual nuevamente
        if valor == '1':
            video_thread = reproducir_video_thread(ruta_rojo)
        elif valor == '2':
            video_thread = reproducir_video_thread(ruta_verde)
        elif valor == '3':
            video_thread = reproducir_video_thread(ruta_azul)
        elif valor == '4':
            video_thread = reproducir_video_thread(ruta_amarilla)
        elif valor == '5':
            video_thread = reproducir_video_thread(ruta_morada)
        elif valor == '6':
            video_thread = reproducir_video_thread(ruta_cian)
        elif valor == '7':
            video_thread = reproducir_video_thread(ruta_blanco)
    else:
        # Si el valor es diferente al valor anterior, actualizar el valor anterior y reproducir el video correspondiente
        valor_anterior = valor
        if valor == '1':
            video_thread = reproducir_video_thread(ruta_rojo)
        elif valor == '2':
            video_thread = reproducir_video_thread(ruta_verde)
        elif valor == '3':
            video_thread = reproducir_video_thread(ruta_azul)
        elif valor == '4':
            video_thread = reproducir_video_thread(ruta_amarilla)
        elif valor == '5':
            video_thread = reproducir_video_thread(ruta_morada)
        elif valor == '6':
            video_thread = reproducir_video_thread(ruta_cian)
        elif valor == '7':
            video_thread = reproducir_video_thread(ruta_blanco)


