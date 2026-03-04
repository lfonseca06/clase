from src.exceptions import  (usuarioIncorrecto, passIncorrecto, emptyUser, emptyPass)

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

    def __str__(self):
        return f"Login(usuario='{self.user}')"
