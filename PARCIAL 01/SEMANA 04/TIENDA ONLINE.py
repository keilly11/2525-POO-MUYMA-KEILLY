# Clase Producto representa un artículo que se vende en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")


# Clase Cliente representa a un usuario que realiza compras
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.stock -= cantidad
            print(f"{cantidad} unidad(es) de {producto.nombre} añadidas al carrito de {self.nombre}")
        else:
            print(f"No hay suficiente stock de {producto.nombre} para agregar {cantidad} unidad(es)")

    def mostrar_carrito(self):
        print(f"Carrito de {self.nombre}:")
        for producto, cantidad in self.carrito:
            print(f"{producto.nombre} x{cantidad} = ${producto.precio * cantidad}")

    def total_compra(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.carrito)
        print(f"Total a pagar por {self.nombre}: ${total}")
        return total


# Prueba del sistema (esto se puede ejecutar para ver el funcionamiento del programa)
if __name__ == "__main__":
    # Crear productos
    p1 = Producto("Laptop", 1000, 5)
    p2 = Producto("Mouse", 25, 20)

    # Mostrar información inicial
    p1.mostrar_info()
    p2.mostrar_info()

    # Crear cliente
    cliente1 = Cliente("Ana")

    # Cliente agrega productos al carrito
    cliente1.agregar_al_carrito(p1, 1)
    cliente1.agregar_al_carrito(p2, 2)

    # Mostrar contenido del carrito y total
    cliente1.mostrar_carrito()
    cliente1.total_compra()

    # Mostrar stock actualizado
    p1.mostrar_info()
    p2.mostrar_info()
