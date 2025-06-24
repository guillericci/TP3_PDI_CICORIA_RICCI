# TP3 - Deteccion de carriles

## Descripción del Ejercicio

Este repositorio contiene el desarrollo del **Trabajo Práctico N°3** de la materia **Procesamiento de Imágenes 1**. El objetivo es detectar y resaltar las líneas que delimitan carriles en dos videos de ejemplo utilizando técnicas de visión por computadora, en particular:

1. Conversión a escala de grises y suavizado (Gaussian Blur).
2. Detección de bordes con Canny.
3. Operaciones morfológicas de clausura para reforzar contornos.
4. Definición de una región de interés (máscara poligonal).
5. Detección de líneas con la transformada de Hough probabilística (HoughLinesP).

El script principal se encuentra en `TP3_PDI.py`. Adicionalmente, se incluyen dos videos de prueba (`ruta_1.mp4` y `ruta_2.mp4`) y un informe en PDF (`Informe - TP3-PDI.pdf`).

---

## Estructura del Repositorio

```
├── TP3_PDI.py
├── ruta_1.mp4
├── ruta_2.mp4
├── Informe - TP3-PDI.pdf
└── README.md      
```

* **TP3\_PDI.py**: Código Python que procesa los videos y dibuja las líneas de carril.
* **ruta\_1.mp4 / ruta\_2.mp4**: Videos de entrada para el procesamiento.
* **Informe - TP3-PDI.pdf**: Documento con descripción del ejercicio, problemas enfrentados, técnicas utilizadas, capturas de pantalla y conclusiones.

---

## Requisitos

* **Python 3.12**
* **Bibliotecas Python**:

  * `opencv-python`
  * `numpy`
  * `matplotlib`

Puedes instalarlas con:

```bash
pip install opencv-python numpy matplotlib
```

---

## Instrucciones de Uso

1. **Modifica la ruta de trabajo**

   * Abre `TP3_PDI.py` y busca la variable:

     ```python
     ruta = "C:/Users/Usuario/PDI1/tp3"
     ```
   * Cámbiala por la ruta absoluta donde clonaste este repositorio en tu computadora.

2. **Ejecuta el script**

   ```bash
   python TP3_PDI.py
   ```

   * El script procesará ambos videos (`ruta_1.mp4` y `ruta_2.mp4`), mostrará en pantalla la ventana de procesamiento y generará dos archivos de salida:

     * `video_lineas_carril_1.mp4`
     * `video_lineas_carril_2.mp4`
   * Para detener la ventana de visualización en cualquier momento, presiona la tecla `q`.

3. **Revisa los resultados**

   * Los videos procesados se guardarán en la misma carpeta de trabajo.
   * Reproduce `video_lineas_carril_1.mp4` y `video_lineas_carril_2.mp4` para observar las líneas de carril detectadas.

---

## Informe

El archivo `Informe - TP3-PDI.pdf` contiene:

* **Descripción del ejercicio** y objetivos.
* **Problemas encontrados** durante el desarrollo.
* **Técnicas utilizadas** 
* **Capturas de pantalla** de pasos intermedios (detección de bordes, máscara, resultados intermedios).
* **Conclusión** sobre el desempeño de la metodología.

---


