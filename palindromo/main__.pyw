def es_palindromo(s):
    # Eliminar espacios en blanco y convertir a minúsculas
    s = s.replace(" ", "").lower()
    # Verificar si el string es igual a su reverso
    return s == s[::-1]

# Ejemplo de uso
string_ejemplo = "Anita lava la tina"
if es_palindromo(string_ejemplo):
    print("El string es un palíndromo.")
else:
    print("El string no es un palíndromo.")
