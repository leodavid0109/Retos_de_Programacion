"""
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 """
import re
def morse(texto):
    morseDict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
    }

    # Caso texto es natural
    if re.match(r'^[A-Za-z0-9]+[A-Za-z0-9 ,.!?\'/()&:;=+-_"$@]*$', texto):
        texto = texto.upper()
        morse = ''
        for c in texto:
            if c == ' ':
                morse += ' '
            else:
                morse += morseDict[c] + ' '
        return morse
    # Caso texto es morse
    elif re.match(r'^[.\- ]+$', texto):
        texto = texto.split(' ')
        natural = ''
        for c in texto:
            if c == '':
                natural += ' '
                continue
            for k, v in morseDict.items():
                if v == c:
                    natural += k
        return natural

    return 'Texto no válido'

print(morse('Hola, mundo!')) # Debe devolver: '.... --- .-.. .- --..--   -- ..- -. -.. --- -.-.--'
print(morse('.... --- .-.. .- --..--   -- ..- -. -.. --- -.-.--')) # Debe devolver: 'HOLA, MUNDO!'