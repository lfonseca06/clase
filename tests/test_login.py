import pytest 
from src.login import login
from src.exceptions import  (UsuarioNoExiste, ContrasenaIncorrecta, UsuarioVacio, ContrasenaVacia, UsuarioEspacios, ContrasenaEspacios)

def test_login_correcto():
    usuario_login = login("candy", "candy159")
    assert usuario_login.usuario == "candy"
    assert usuario_login.contrasena == "candy159"

def test_usuario_vacio():
    with pytest.raises(UsuarioVacio):
        login("", "candy159")

def test_usuario_solo_espacios():
    with pytest.raises(UsuarioEspacios):
        login("   ", "candy159")

def test_contrasena_vacia():
    with pytest.raises(ContrasenaVacia):
        login("candy", "")

def test_contrasena_solo_espacios():
    with pytest.raises(ContrasenaEspacios):
        login("candy", "   ")

def test_usuario_no_existe():
    with pytest.raises(UsuarioNoExiste):
        login("Pedro", "candy159")

def test_contrasena_incorrecta():
    with pytest.raises(ContrasenaIncorrecta):
        login("candy", "123")







"""
import pytest # type: ignore
from src.login import login
from src.exceptions import usuarioIncorrecto, passIncorrecto, emptyUser, emptyPass, UsuarioNoExiste

def test_acceso_correcto():
    ULogin = login("lfonseca01", "123456789")
    assert ULogin.user == "lfonseca01"
    assert ULogin.passw == "123456789"

def test_usuario_vacio():
    with pytest.raises(emptyUser):
        login("", "123456789")

def test_pass_vacio():
    with pytest.raises(emptyPass):
        login("lfonseca01", "")

def test_user_no_existe():
    with pytest.raises(UsuarioNoExiste):
        login("lfonsec", "123456789")

def test_user_incorrecto():
    with pytest.raises(usuarioIncorrecto):
        login("lfonseca","123456789")

def test_contrasena_incorrecta():
    with pytest.raises(passIncorrecto):
        login("lfonseca01", "123")
"""
'''
"""
def test_crear_producto_valido():
    producto = Producto("Laptop", 1000, 5)
    assert producto.nombre == "Laptop"
    assert producto.precio == 1000
     

def test_crear_producto_sin_categoria():
    producto = Producto("Mouse", 25, 10)
    assert producto.categoria == "General"

def test_precio_negativo_error():
    with pytest.raises(PrecioInvalidoError):
        Producto("Test", -100, 5)

def test_cantidad_negativa_error():
    with pytest.raises(CantidadInvalidaError):
        Producto
"""
'''
