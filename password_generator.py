import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  # Letras mayúsculas y minúsculas

    if use_digits:
        characters += string.digits  # Añadir dígitos
    if use_special_chars:
        characters += string.punctuation  # Añadir caracteres especiales

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Bienvenido al Generador de Contraseñas Aleatorias.")
    length = int(input("Introduce la longitud de la contraseña (por defecto 12): ") or 12)
    use_digits = input("¿Incluir dígitos? (s/n, por defecto s): ").lower() != 'n'
    use_special_chars = input("¿Incluir caracteres especiales? (s/n, por defecto s): ").lower() != 'n'

    password = generate_password(length, use_digits, use_special_chars)
    print(f"\nTu contraseña generada es: {password}")

if __name__ == "__main__":
    main()

