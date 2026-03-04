class usuarioIncorrecto (Exception):
    """Se lanza cuando el usuario ingresado es incorrecto"""
    pass

class passIncorrecto (Exception):
    """Se lanza cuando la contraseña es incorrecta"""
    pass

class emptyUser(Exception):
    """Se lanza cuando el usuario ingresado esta vacio"""
    pass

class emptyPass (Exception):
    """Se lanza cuando la contraseña esta vacia"""
    pass

class UsuarioNoExiste (Exception):
    """Se lanza cuando el usuario ingresado no existe"""
    pass
