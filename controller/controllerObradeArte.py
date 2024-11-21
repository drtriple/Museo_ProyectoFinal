# controller/controllerObradeArte.py
from dataAccess.dataAcces_DB import DataAccessDB
from dtoGenerics.generic import GenericDTO
from model.pintura import Pintura
from model.escultura import Escultura

class ArtController:
    def __init__(self):
        self.data_access = DataAccessDB()
        
    def existing_artwork(self,name):
        result = self.get_artwork_by_name(name)
        if isinstance(result, dict):
            return True
        else:
            return False

    def add_pintura(self, nombre, autor, en_venta, dimensiones, tecnica, retrato):
        pintura = Pintura(nombre, autor, en_venta, dimensiones, tecnica, retrato)
        pintura_dict = pintura.__dict__.copy()
        pintura_dict["tipo_de_obra"] = "Pintura"  # Añadimos el tipo de obra
        dto = GenericDTO(pintura_dict)
        save = self.data_access.add_artwork(dto)
        return pintura_dict

    def add_escultura(self, nombre, autor, en_venta, volumen, material):
        escultura = Escultura(nombre, autor, en_venta, volumen, material)
        escultura_dict = escultura.__dict__.copy()
        escultura_dict["tipo_de_obra"] = "Escultura"  # Añadimos el tipo de obra
        dto = GenericDTO(escultura_dict)
        save =  self.data_access.add_artwork(dto)
        return escultura_dict
        
    def get_artwork_by_name(self, name):
        """
        Consulta una obra de arte por su nombre.
        """       
        data = self.data_access.load_all_artworks()
        if not data:
            return "El archivo está vacío."

        for artwork in data:
            if artwork.get("_nombre") == name:
                return artwork

        return f"No se encontró ninguna obra con el nombre: {name}."
        
    def get_artwork_by_type(self, type):
        """
        Consulta obras de arte por su tipo.
        """
        data = self.data_access.load_all_artworks()
        if not data:
            return "El archivo está vacío."

        matching_artworks = [artwork for artwork in data if artwork.get("tipo_de_obra", "").lower() == type.lower()]
        return matching_artworks if matching_artworks else f"No se encontraron obras de tipo: {type}."

        
    def update_en_venta(self, name, en_venta):
        """Actualiza el estado de venta de una obra."""
        data = self.data_access.load_all_artworks()
        for artwork in data:
            if artwork.get("_nombre") == name:
                artwork["_en_venta"] = en_venta
                self.data_access.save_all_artworks(data)
                return f"Obra '{name}' actualizada con _en_venta = {en_venta}."
        return f"No se encontró ninguna obra con el nombre: {name}."

    def update_autor(self, name, autor):
        """Actualiza el autor de una obra."""
        data = self.data_access.load_all_artworks()
        for artwork in data:
            if artwork.get("_nombre") == name:
                artwork["_autor"] = autor
                self.data_access.save_all_artworks(data)
                return f"Obra '{name}' actualizada con _autor = {autor}."
        return f"No se encontró ninguna obra con el nombre: {name}."

    def update_tecnica(self, name, tecnica):
        """Actualiza la técnica de una pintura."""
        data = self.data_access.load_all_artworks()
        for artwork in data:
            if artwork.get("_nombre") == name and "tipo_de_obra" in artwork and artwork["tipo_de_obra"] == "Pintura":
                artwork["_Pintura__tecnica"] = tecnica
                self.data_access.save_all_artworks(data)
                return f"Obra '{name}' actualizada con _Pintura__tecnica = {tecnica}."
        return f"No se encontró ninguna pintura con el nombre: {name}."

    def update_retrato(self, name, retrato):
        """Actualiza el valor de retrato de una pintura."""
        data = self.data_access.load_all_artworks()
        for artwork in data:
            if artwork.get("_nombre") == name and "tipo_de_obra" in artwork and artwork["tipo_de_obra"] == "Pintura":
                artwork["_Pintura__retrato"] = retrato
                self.data_access.save_all_artworks(data)
                return f"Obra '{name}' actualizada con _Pintura__retrato = {retrato}."
        return f"No se encontró ninguna pintura con el nombre: {name}."

    def update_dimensiones(self, name, dimensiones):
        """Actualiza las dimensiones de una pintura."""
        data = self.data_access.load_all_artworks()
        for artwork in data:
            if artwork.get("_nombre") == name and "tipo_de_obra" in artwork and artwork["tipo_de_obra"] == "Pintura":
                artwork["_Pintura__dimensiones"] = dimensiones
                self.data_access.save_all_artworks(data)
                return f"Obra '{name}' actualizada con _Pintura__dimensiones = {dimensiones}."
        return f"No se encontró ninguna pintura con el nombre: {name}."


    def delete_artwork_by_name(self, name):
        """
        Elimina una obra de arte del archivo JSON basado en su nombre.
        
        :param name: Nombre de la obra a eliminar.
        :return: Mensaje indicando si la obra fue eliminada o si no se encontró.
        """
        data = self.data_access.load_all_artworks()
        if not data:
            return "El archivo está vacío. No hay obras para eliminar."

        for artwork in data:
            if artwork.get("_nombre") == name:
                data.remove(artwork)
                self.data_access.save_all_artworks(data)
                return f"Obra '{name}' eliminada exitosamente."

        return f"No se encontró ninguna obra con el nombre: {name}."
    
    
    def all_view_artwork(self):
        return self.data_access.load_all_artworks()