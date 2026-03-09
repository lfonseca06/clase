from src.exceptions import  (UsuarioNoExiste, ContrasenaIncorrecta, UsuarioVacio, ContrasenaVacia, UsuarioEspacios, ContrasenaEspacios)

class login:

    def __init__(self, usuario, contrasena):
        self._validar_usuario(usuario)
        self._validar_contrasena(contrasena)

        self.usuario = usuario
        self.contrasena = contrasena

    def _validar_usuario(self, usuario):
        if not usuario:
            raise UsuarioVacio("El usuario no pued estar vacio")

        if usuario.strip() == "":
            raise UsuarioEspacios("El usuario no puede contener solo espacios")

        if usuario != "candy":
            raise UsuarioNoExiste(f"El usuario no esta registrado: {usuario}")

    def _validar_contrasena(self, contrasena):
        if not contrasena:
            raise ContrasenaVacia("La contraseña no puede estar vacía")

        if contrasena.strip() == "":
            raise ContrasenaEspacios("La contraseña no puede contener solo espacios")

        if contrasena != "candy159":
            raise ContrasenaIncorrecta(f"La contraseña es incorrecta: {contrasena}")

    def __str__(self):
        return f"Login(usuario='{self.usuario}')"
























"""
from src.exceptions import usuarioIncorrecto, passIncorrecto, emptyUser, emptyPass, UsuarioNoExiste

class login:

    def __init__(self, user, passw):
        self._validar_usuario(user)
        self._validar_contrasena(passw)

        self.user = user
        self.passw = passw

    def _validar_usuario(self, user):
        if not user:
            raise emptyUser("El usuario no puede estar vacio")

    def _usuario_incorrecto(self, user):
        if user != "lfonseca01":
            raise usuarioIncorrecto(f"El usuario es incorrecto: {user}")

    def _validar_contrasena(self, passw):
        if not passw:
            raise emptyPass("La contraseña no puede estar vacía")

    def _passw_incorrecto(self, passw):
       if passw != "123456789":
            raise passIncorrecto(f"La contraseña es incorrecta: {passw}")
       
    def _usuario_no_existe(self, user):
        if user != "lfonseca01":
            raise UsuarioNoExiste(f"El usuario no existe: {user}")

    def __str__(self):
        return f"Login(usuario='{self.user}')"
"""