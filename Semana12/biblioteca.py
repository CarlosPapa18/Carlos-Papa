# ================================
# Sistema de Gestión de Biblioteca Digital
# Autor: (tu nombre)
# Descripción: Este sistema permite gestionar
# libros, usuarios y préstamos en una biblioteca digital.
# Se emplean colecciones de Python (listas, tuplas, diccionarios, conjuntos)
# aplicando Programación Orientada a Objetos.
# ================================

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# -------------------- Clase Libro --------------------
@dataclass
class Libro:
    """
    Representa un libro de la biblioteca.
    - info: tupla (autor, título). Se usa tupla porque estos datos no cambian.
    - category: categoría/tema del libro.
    - isbn: identificador único del libro.
    - borrowed_by: almacena el ID del usuario que tiene prestado el libro, o None si está disponible.
    """
    info: Tuple[str, str]          # (autor, título) → inmutable
    category: str                  # categoría del libro
    isbn: str                      # identificador único
    borrowed_by: Optional[str] = None  # usuario que lo tiene prestado (o None)

    # Propiedad para acceder fácilmente al autor
    @property
    def autor(self) -> str:
        return self.info[0]

    # Propiedad para acceder fácilmente al título
    @property
    def titulo(self) -> str:
        return self.info[1]

    def __repr__(self) -> str:
        estado = f"prestado a {self.borrowed_by}" if self.borrowed_by else "disponible"
        return f"Libro(ISBN={self.isbn}, '{self.titulo}' - {self.autor}, {self.category}, {estado})"


# -------------------- Clase Usuario --------------------
@dataclass
class Usuario:
    """
    Representa un usuario de la biblioteca.
    - name: nombre del usuario.
    - user_id: identificador único del usuario.
    - borrowed_books: lista con los ISBN de los libros actualmente prestados.
    """
    name: str
    user_id: str
    borrowed_books: List[str] = field(default_factory=list)  # Lista vacía al inicio

    def __repr__(self) -> str:
        return f"Usuario({self.user_id}: {self.name}, prestados={len(self.borrowed_books)})"


# -------------------- Clase Biblioteca --------------------
class Biblioteca:
    """
    Gestiona los libros, usuarios y préstamos de la biblioteca.
    Se usan:
    - Diccionario (books) con ISBN → Libro, para búsqueda rápida.
    - Diccionario (users) con user_id → Usuario.
    - Conjunto (user_ids) para garantizar que no se repitan IDs.
    - Diccionario (loans) con ISBN → user_id, para registrar los préstamos.
    """
    def __init__(self):
        self.books: Dict[str, Libro] = {}   # libros de la biblioteca
        self.users: Dict[str, Usuario] = {} # usuarios registrados
        self.user_ids: set = set()          # conjunto para IDs únicos
        self.loans: Dict[str, str] = {}     # préstamos registrados

    # ---------- Gestión de libros ----------
    def add_book(self, libro: Libro) -> None:
        """Añadir un libro nuevo al catálogo si el ISBN no está repetido."""
        if libro.isbn in self.books:
            raise ValueError(f"El ISBN {libro.isbn} ya existe en la biblioteca.")
        self.books[libro.isbn] = libro

    def remove_book(self, isbn: str) -> None:
        """Eliminar un libro si existe y no está prestado."""
        if isbn not in self.books:
            raise ValueError(f"No existe un libro con ISBN {isbn}.")
        if self.books[isbn].borrowed_by is not None:
            raise ValueError("No se puede eliminar un libro que está actualmente prestado.")
        del self.books[isbn]
        self.loans.pop(isbn, None)  # limpiar de préstamos en caso de error

    # ---------- Gestión de usuarios ----------
    def register_user(self, usuario: Usuario) -> None:
        """Registrar un usuario nuevo (verificando ID único)."""
        if usuario.user_id in self.user_ids:
            raise ValueError(f"El ID de usuario {usuario.user_id} ya está registrado.")
        self.users[usuario.user_id] = usuario
        self.user_ids.add(usuario.user_id)

    def unregister_user(self, user_id: str) -> None:
        """Dar de baja un usuario si no tiene libros prestados."""
        if user_id not in self.users:
            raise ValueError(f"Usuario {user_id} no registrado.")
        if self.users[user_id].borrowed_books:
            raise ValueError("El usuario tiene libros prestados. Debe devolverlos antes de la baja.")
        del self.users[user_id]
        self.user_ids.remove(user_id)

    # ---------- Gestión de préstamos ----------
    def lend_book(self, isbn: str, user_id: str) -> None:
        """Prestar un libro a un usuario."""
        if isbn not in self.books:
            raise ValueError("ISBN no encontrado.")
        if user_id not in self.users:
            raise ValueError("Usuario no registrado.")
        book = self.books[isbn]
        if book.borrowed_by is not None:
            raise ValueError("El libro ya está prestado.")
        # registrar préstamo
        book.borrowed_by = user_id
        self.users[user_id].borrowed_books.append(isbn)
        self.loans[isbn] = user_id

    def return_book(self, isbn: str, user_id: str) -> None:
        """Devolver un libro prestado."""
        if isbn not in self.books:
            raise ValueError("ISBN no encontrado.")
        book = self.books[isbn]
        if book.borrowed_by is None:
            raise ValueError("El libro no está prestado.")
        if book.borrowed_by != user_id:
            raise ValueError("Este libro fue prestado a otro usuario.")
        # procesar devolución
        book.borrowed_by = None
        self.users[user_id].borrowed_books.remove(isbn)
        self.loans.pop(isbn, None)

    # ---------- Búsquedas ----------
    def search_by_title(self, query: str) -> List[Libro]:
        """Buscar libros por título."""
        q = query.lower()
        return [b for b in self.books.values() if q in b.titulo.lower()]

    def search_by_author(self, query: str) -> List[Libro]:
        """Buscar libros por autor."""
        q = query.lower()
        return [b for b in self.books.values() if q in b.autor.lower()]

    def search_by_category(self, query: str) -> List[Libro]:
        """Buscar libros por categoría."""
        q = query.lower()
        return [b for b in self.books.values() if q in b.category.lower()]

    # ---------- Listados ----------
    def list_borrowed_books(self, user_id: str) -> List[Libro]:
        """Listar todos los libros prestados a un usuario."""
        if user_id not in self.users:
            raise ValueError("Usuario no registrado.")
        return [self.books[isbn] for isbn in self.users[user_id].borrowed_books if isbn in self.books]

    def list_all_books(self) -> List[Libro]:
        """Listar todos los libros de la biblioteca."""
        return list(self.books.values())

    def __repr__(self) -> str:
        return f"Biblioteca(libros={len(self.books)}, usuarios={len(self.users)}, préstamos={len(self.loans)})"


# -------------------- PRUEBAS DE USO --------------------
if __name__ == "__main__":
    # Crear biblioteca
    b = Biblioteca()

    # Crear y añadir libros (autor, título)
    libro1 = Libro(("Gabriel García Márquez", "Cien años de soledad"), "Realismo mágico", "ISBN-0001")
    libro2 = Libro(("George Orwell", "1984"), "Distopía", "ISBN-0002")
    libro3 = Libro(("Yuval Noah Harari", "Sapiens"), "Historia", "ISBN-0003")

    b.add_book(libro1)
    b.add_book(libro2)
    b.add_book(libro3)

    # Registrar usuarios
    u1 = Usuario("Ana Pérez", "U001")
    u2 = Usuario("Carlos López", "U002")
    b.register_user(u1)
    b.register_user(u2)

    print("Estado inicial:", b)

    # Prestar un libro
    b.lend_book("ISBN-0001", "U001")
    print("\nDespués de prestar ISBN-0001 a U001:")
    print("Libros prestados a U001:", b.list_borrowed_books("U001"))

    # Buscar por autor
    print("\nBuscar por autor 'Orwell':", b.search_by_author("orwell"))

    # Devolver libro
    b.return_book("ISBN-0001", "U001")
    print("\nDespués de devolver ISBN-0001:")
    print("Libros prestados a U001:", b.list_borrowed_books("U001"))

    # Intentar eliminar un libro prestado
    b.lend_book("ISBN-0002", "U002")
    try:
        b.remove_book("ISBN-0002")
    except ValueError as e:
        print("\nError esperado al eliminar libro prestado:", e)

    # Finalmente devolver y eliminar libro
    b.return_book("ISBN-0002", "U002")
    b.remove_book("ISBN-0002")

    print("\nCatálogo final:", b.list_all_books())
