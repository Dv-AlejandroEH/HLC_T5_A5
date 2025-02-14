lista_libros = []

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def agregar_libro(self, libro):
        lista_libros.append(libro)

    def mostrar_libros(self):
        for i, libro in enumerate(lista_libros, start=1):
            print(f"{i}. {libro.titulo} - {libro.autor}")

biblio = Biblioteca()
biblio.agregar_libro(Libro("1984", "George Orwell"))
biblio.agregar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
biblio.mostrar_libros()