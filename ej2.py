texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

def formatear_dialogo(texto):
    partes = texto.split('#')
    return "\n\n".join(part.capitalize() + "." for part in partes)

texto_formateado = formatear_dialogo(texto_original)
print(texto_formateado)
