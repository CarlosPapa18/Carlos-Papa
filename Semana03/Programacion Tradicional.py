# programa_tradicional.py

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura diaria (7 días):")
    for i in range(7):
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()