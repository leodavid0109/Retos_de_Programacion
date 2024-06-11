"""
Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 - Url de ejemplo: https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
"""

import requests  # Para descargar la imagen de la url
from PIL import Image  # Para manejar la imagen
from io import BytesIO  # Crea el objeto de archivo de memoria (auxiliar)
import math  # Para cálculos matemáticos del aspect ratio


def descarga_imagen(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        raise Exception("Error al descargar la imagen")


def aspect_ratio(url):
    try:
        image = descarga_imagen(url)
        ancho, alto = image.size
        gcd = math.gcd(ancho, alto)
        ratio = (ancho // gcd, alto // gcd)
        return f"{ratio[0]}:{ratio[1]}"

    except Exception as e:
        return str(e)