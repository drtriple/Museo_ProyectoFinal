from controller.controllerObradeArte import ArtController
class ArtView:
    def __init__(self):
        self.controller = ArtController()
        
    def display_artwork_details(self,art):
        if not art:
            print("No se proporcionó información de la obra.")
            return
        
        print("\n--------- Detalles de la Obra de Arte ---------")
        
        # Formatear diccionario
        nombre = art.get("_nombre", "Desconocido")
        print(f"Nombre: {nombre.capitalize()}")
        
        print(f"Autor: {art.get('_autor', 'Desconocido')}")
        print(f"En venta: {'Sí' if art.get('_en_venta') else 'No'}")
        
        tipoObra = art.get('tipo_de_obra', 'Desconocido')
        print(f"Tipo de obra: {tipoObra}")
        
        if tipoObra.lower() == "pintura":
            print(f"Dimensiones: {art.get('_Pintura__dimensiones', 'No especificadas')}")
            print(f"Técnica: {art.get('_Pintura__tecnica', 'No especificadas')}")
            print(f"Es retrato: {'Sí' if art.get('_Pintura__retrato') else 'No'}")
            
        elif tipoObra.lower() == "escultura":
            print(f"Volumen: {art.get('_Escultura__volumen', 'No especificadas')}")
            print(f"Material: {art.get('_Escultura__material', 'No especificado')}")
            
        else:
            print("Detalles adiciconales no disponibles para este tipo de obra")
            
        print("----------------------------------------\n")
             
    def display_message(self, message):
        print(message)

    def display_artwork(self, artwork):
        if isinstance(artwork, dict):
            for key, value in artwork.items():
                print(f"{key}: {value}")
        else:
            print(artwork)

    def prompt_for_input(self, prompt_text):
        return input(prompt_text)

    def add_artwork_pintura(self):
        print("---------------------- AGREGAR OBRA DE ARTE: PINTURA ----------------------")
        
        nombre = self.prompt_for_input("Nombre de la pintura: ")
        autor = self.prompt_for_input("Autor: ")
        en_venta = str(input("La obra quedará a la venta? (S/N): ")).lower()
        en_venta2 = True if en_venta == "s" else False
        dimensiones = self.prompt_for_input("Dimensiones: ")
        tecnica = self.prompt_for_input("Técnica: ")
        retrato = str(input("La obra será una pintura tipo retrato? (S/N): ")).lower()
        retrato2 = True if retrato == "s" else False
        resultado = self.controller.add_pintura(nombre, autor, en_venta2, dimensiones, tecnica, retrato2)
        
        print("----------------- PINTURA AGREGADA -----------------")
        self.display_artwork_details(resultado)
               
    def add_artwork_escultura(self):
        print("---------------------- AGREGAR OBRA DE ARTE: ESCULTURA ----------------------")
        
        nombre = self.prompt_for_input("Nombre de la escultura: ")
        autor = self.prompt_for_input("Autor: ")
        en_venta = str(input("La obra quedará a la venta? (S/N): ")).lower()
        en_venta2 = True if en_venta == "s" else False
        volumen = self.prompt_for_input("Volumen: ")
        material = self.prompt_for_input("Material: ")
        resultado = self.controller.add_escultura(nombre, autor, en_venta2, volumen, material)
        
        print("----------------- ESCULTURA AGREGADA -----------------")
        self.display_artwork_details(resultado)
        
    def view_artwork_by_name(self):
        name = self.prompt_for_input("Nombre de la obra: ")
        artwork = self.controller.get_artwork_by_name(name)
     
        print(f"----------------- OBRA DE ARTE: {name} -----------------")
        self.display_artwork_details(artwork)
        
    def view_artwork_by_type(self):
        type_of_art = str(input("Tipo de obra (Pintura/Escultura): "))
        artworks = self.controller.get_artwork_by_type(type_of_art)
        
        if isinstance(artworks, str):  # Mensaje de error o vacío
            print(artworks)
            return

        print(f"----------------- OBRAS DE ARTE: {type_of_art} -----------------")
        for artwork in artworks:
            self.display_artwork_details(artwork)

                
    def update_values(self):
        print("---------------------- Actualiza una obra de arte ----------------------")
        name = self.prompt_for_input("Nombre de la obra: ")
        existenciaObra = self.controller.existing_artwork(name)
        
        if existenciaObra:
            print("Seleccione el componente que desea actualizar: \n 1. Estado de venta\n2. Nombre del Autor\n3. Tipo de técnica\n4. Estado retrato\n5. Dimensiones")
            op = int(input("Ingrese la opción que desea: "))
            
            if op == 1:
                en_venta = str(input("La obra quedará a la venta? (S/N): ")).lower()
                en_venta2 = True if en_venta == "s" else False
                resultado = self.controller.update_en_venta(name, en_venta2)
                print(resultado)
            elif op == 2:
                autor = str(input(f"Ingrese el nombre del nuevo autor de la obra {name}: "))
                resultado = self.controller.update_autor(name, autor)
                print(resultado)
            elif op == 3:
                tecnica = str(input(f"Ingrese el nombre de la nueva técnica de la obra {name}: "))
                resultado = self.controller.update_tecnica(name, tecnica)
                print(resultado)
            elif op == 4:
                retrato = str(input("La obra será una pintura tipo retrato? (S/N): ")).lower()
                retrato2 = True if retrato == "s" else False
                resultado = self.controller.update_retrato(name, retrato2)
                print(resultado)
            elif op == 5:
                dimensiones = str(input(f"Ingrese las nuevas dimensiones de la obra {name}: "))
                resultado = self.controller.update_dimensiones(name, dimensiones)
                print(resultado)
            else:
                print("La opción ingresa no es valida.")
        else:
            print(f"La obra {name} no existe en la base de datos del museo.")
            
    def delete_artwork(self):
        name = self.prompt_for_input("Nombre de la obra a eliminar: ")
        resultado = self.controller.delete_artwork_by_name(name)
        self.display_message(resultado)
        
    def view_all_artwork(self):
        artworks = self.controller.all_view_artwork()
        print(f"----------------- OBRAS DE ARTE -----------------")
        for artwork in artworks:
            self.display_artwork_details(artwork)