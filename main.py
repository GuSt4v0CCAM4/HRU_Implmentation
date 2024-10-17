class Usuario:
    def __init__(self, nombre, nivel_de_seguridad):
        self.nombre = nombre
        self.nivel_de_seguridad = nivel_de_seguridad
class Recurso:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
class HRU:
    def __init__(self):
        self.usuarios = []
        self.recursos = []
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
    def agregar_recurso(self, recurso):
        self.recursos.append(recurso)
    def acceso_recurso(self, usuario, recurso):
        if usuario not in self.usuarios: #verificamos si el usuario existe ants de dar acceso
            return f"{usuario.nombre} no esta registrado en el sistema"
        if usuario.nivel_de_seguridad >= recurso.nivel:
            return f"{usuario.nombre} tiene acceso a {recurso.nombre}"
        else:
            return f"{usuario.nombre} denegado acceso a {recurso.nombre}"
    def eliminar_usuario(self, usuario): #metodo para eliminar usuario
        if usuario in self.usuarios: #primero verificamos si existe el usuario
            self.usuarios.remove(usuario) #lo eliminmos
hru = HRU()
hru.agregar_usuario(Usuario("UsuarioHRU1", 2))
hru.agregar_usuario(Usuario("UsuarioHRU2", 1))
hru.agregar_recurso(Recurso("TopSecret", 2))
#Imprimimos los accesos de cada usuari
resultado1 = hru.acceso_recurso(hru.usuarios[0], hru.recursos[0])
print(resultado1)
resultado2 = hru.acceso_recurso(hru.usuarios[1], hru.recursos[0])
print(resultado2)