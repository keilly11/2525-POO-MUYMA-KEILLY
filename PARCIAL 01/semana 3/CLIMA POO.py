# Programa para calcular el promedio semanal del clima usando POO (sin entrada del usuario)

class ClimaDia:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

class SemanaClimatica:
    def __init__(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        temps = [22.5, 23.0, 21.8, 24.2, 22.0, 23.5, 21.0]
        self.dias_semana = [ClimaDia(dia, temp) for dia, temp in zip(dias, temps)]

    def mostrar_temperaturas(self):
        for dia in self.dias_semana:
            print(f"{dia.dia}: {dia.temperatura}°C")

    def calcular_promedio(self):
        total = sum(dia.temperatura for dia in self.dias_semana)
        return total / len(self.dias_semana)

def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")
    semana = SemanaClimatica()
    semana.mostrar_temperaturas()
    promedio = semana.calcular_promedio()
    print(f"\nEl promedio de temperaturas de la semana es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
