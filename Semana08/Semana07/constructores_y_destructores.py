# Clase Biblioteca: representa una biblioteca que contiene varios libros
class Libro:
    def __init__(self, titulo, autor):
        # Constructor: inicializa los atributos del objeto
        self.titulo = titulo
        self.autor = autor
        print(f" Libro creado: '{self.titulo}' por {self.autor}")

    def mostrar_info(self):
        print(f"Título: {self.titulo} | Autor: {self.autor}")

    def __del__(self):
        # Destructor: muestra un mensaje cuando se elimina el objeto
        print(f" Libro eliminado: '{self.titulo}'")

# Clase Usuario: representa un usuario que toma libros prestados
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []
        print(f" Usuario creado: {self.nombre}")

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)
        print(f"{self.nombre} ha tomado prestado: '{libro.titulo}'")

    def devolver_todos(self):
        print(f"{self.nombre} está devolviendo todos los libros...")
        self.libros_prestados.clear()

    def __del__(self):
        # Destructor: mensaje cuando se elimina al usuario
        print(f" Usuario eliminado: {self.nombre}")

# Código principal del programa
if __name__ == "__main__":
    # Crear libros
    libro1 = Libro("1984", "George Orwell")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes")

    # Crear usuario
    usuario1 = Usuario("Carlos")

    # Prestar libros
    usuario1.prestar_libro(libro1)
    usuario1.prestar_libro(libro2)

    # Mostrar libros prestados
    print("\n Libros actualmente prestados:")
    for libro in usuario1.libros_prestados:
        libro.mostrar_info()

    # Devolver libros
    usuario1.devolver_todos()

    # Eliminar objetos manualmente (para activar el destructor)
    del libro1
    del libro2
    del usuario1
