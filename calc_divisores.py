def obtener_numero():
    while True:
        entrada = input("Ingresa un número natural (1-100): ")
        try:
            numero = int(entrada)
            if numero == 0:
                raise ValueError("El número debe ser diferente de 0, ademas 0 no tiene divisores.")
            if numero <= 0:
                raise ValueError("El número debe ser mayor que 0")
            if numero > 100:
                raise ValueError("El número debe estar entre 1 y 100.")
            return numero
        except ValueError:
            print("La entrada es inválida: debes ingresar un número natural mas no caracteres no numericos.")

def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def main():
    print("BIENVENIDO AL CALCULADOR DE DIVISORES.")
    numero = obtener_numero()
    divisores = calcular_divisores(numero)
    print(f"Los divisores que se ha podido encontrar del {numero} son: {divisores}")

if __name__ == "__main__":
    main()

