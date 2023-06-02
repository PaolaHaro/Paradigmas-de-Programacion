from aplication.repositorio.repositoriodeusuario import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#==================================================
#  Implementa la interface RepositorioDeUsuarios
#==================================================
class SistemaDeArchivos(RepositorioDeUsuarios):
    __directorios: str

    def __init__(mi, directorio:str):
        mi.__directorio = directorio

    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi.__directorio}")

    def guardar(mi, usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNone()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
        print(f"Guardando usuario en el archivo :{mi.__directorio}/{usuario.getNombre()}")
        print(xml)

    def cerrar(mi) -> None:
        print("Cerrando el archivo")

