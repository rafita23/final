class Movie():
     def __init__(self, id, nombre=None, apellido=None, direccion=None) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion

     def to_JSON(self):
         return {
             'id': self.id,
             'nombre': self.nombre,
             'apellido': self.apellido,
             'direccion': self.direccion
         }

 