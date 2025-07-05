# -------------------------
# Clase base: Vehiculo
# Demuestra Encapsulación con atributos privados y uso de getters/setters
# -------------------------

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca  # atributo privado
        self.__modelo = modelo  # atributo privado
        self.__año = año  # atributo privado

    # Métodos getter
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    # Métodos setter
    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    def set_año(self, nuevo_año):
        self.__año = nuevo_año

    def mostrar_info(self):
        print(f"Vehículo: {self.__marca} {self.__modelo} ({self.__año})")

    # Método que será sobrescrito (para polimorfismo)
    def arrancar(self):
        print("El vehículo está arrancando...")

# -------------------------
# Clase derivada: Automovil
# Hereda de Vehiculo y sobrescribe un método (polimorfismo)
# -------------------------

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_combustible):
        super().__init__(marca, modelo, año)
        self.tipo_combustible = tipo_combustible

    def mostrar_info(self):
        # Método sobrescrito (polimorfismo)
        print(f"Automóvil: {self.get_marca()} {self.get_modelo()} ({self.get_año()}) - Combustible: {self.tipo_combustible}")

    def arrancar(self):
        print(f"El automóvil {self.get_modelo()} está arrancando con {self.tipo_combustible}...")

# -------------------------
# Clase derivada: Motocicleta
# Otra clase hija para mostrar más polimorfismo
# -------------------------

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        print(f"Motocicleta: {self.get_marca()} {self.get_modelo()} ({self.get_año()}) - {self.cilindrada}cc")

    def arrancar(self):
        print(f"La motocicleta {self.get_modelo()} ruge con su motor de {self.cilindrada}cc...")

# -------------------------
# Código principal: Creación de objetos e invocación de métodos
# -------------------------

if __name__ == "__main__":
    # Instancia de clase base
    vehiculo_generico = Vehiculo("Toyota", "Corolla", 2010)
    vehiculo_generico.mostrar_info()
    vehiculo_generico.arrancar()

    print()

    # Instancias de clases derivadas
    auto = Automovil("Honda", "Civic", 2022, "Gasolina")
    moto = Motocicleta("Yamaha", "MT-03", 2023, 321)

    # Demostración de herencia, encapsulación y polimorfismo
    auto.mostrar_info()
    auto.arrancar()

    print()

    moto.mostrar_info()
    moto.arrancar()
