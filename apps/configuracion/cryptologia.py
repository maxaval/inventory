from cryptography.fernet import Fernet
from datetime import datetime

def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)
        
def carga_clave():
    return open("clave.key","rb").read()

def text_licence_prepare(texto1,texto2,texto3):
    textocompleto = texto1+";"+texto2+";"+texto3
    return textocompleto

def genera_licencia(texto):
    clave = carga_clave()
    texto = texto.encode()
    f = Fernet(clave)
    encriptado = f.encrypt(texto)
    return encriptado
    
def leer_licencia(texto):
    clave = carga_clave()
    f = Fernet(clave)
    decriptado = f.decrypt(texto)
    return decriptado

def validar_licencia(texto):
    partes = str(texto).split(sep=";")
    empresa = partes[0]
    fechaini = partes[1]
    fechafin = partes[2]
    startdate = datetime.strptime(fechaini, "%Y-%m-%d").date()
    enddate = datetime.strptime(fechafin, "%Y-%m-%d").date()
    now = datetime.now()
    if enddate > now.date():
        return "La licencia es valida aun"
    else:
        return "La licencia ya caduco"
    