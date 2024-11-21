from view.viewPrincipal import ArtView

class viewMain:
    def __init__(self):
            self.view = ArtView()

    def main(self):
        while True:
            print("\nOpciones:")
            print("1. Agregar Pintura")
            print("2. Agregar Escultura")
            print("3. Ver obra de arte por nombre")
            print("4. Ver obras de arte por tipo")
            print("5. Actualizar estado de venta")
            print("6. Eliminar obra de arte por nombre")
            print("7. Ver todas las obras de arte")
            print("8. Salir")

            option = self.view.prompt_for_input("Seleccione una opción (1-8): ")

            if option == "1":
                self.view.add_artwork_pintura()

            elif option == "2":
                self.view.add_artwork_escultura()

            elif option == "3":
                self.view.view_artwork_by_name()

            elif option == "4":
                self.view.view_artwork_by_type()

            elif option == "5":
                self.view.update_values()

            elif option == "6":
                self.view.delete_artwork()

            elif option == "7":
                self.view.view_all_artwork()

            elif option == "8":
                self.view.display_message("Saliendo del programa.")
                break

            else:
                self.view.display_message("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    execute = viewMain()
    execute.main()