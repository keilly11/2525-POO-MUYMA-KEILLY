# Programa para calcular el promedio semanal del clima usando programación tradicional (sin entrada del usuario)

def obtener_temperaturas():
    # Temperaturas predeterminadas para la semana
    temperaturas = [22.5, 23.0, 21.8, 24.2, 22.0, 23.5, 21.0]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for dia, temp in zip(dias, temperaturas):
        print(f"{dia}: {temp}°C")
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA ===")
    temps = obtener_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio de temperaturas de la semana es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
