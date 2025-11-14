# Liberiras usadas para realizar la firma digital
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature
import os

class FirmaDigital():
    def __init__(self):
        self.rutaClavePrivada = "clavePrivada.pem"
        self.rutaClavePublica = "clavePublica.pem"
        self.clavePrivada = None
        self.clavePublica = None

    def GenerarClaves(self):
        # Corregido: Primero generar las claves
        self.clavePrivada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.clavePublica = self.clavePrivada.public_key()
        
        # Guardar clave privada
        with open(self.rutaClavePrivada, "wb") as archivo:
            archivo.write(
                self.clavePrivada.private_bytes(  # Corregido: usar self.clavePrivada
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        # Guardar clave pública
        with open(self.rutaClavePublica, "wb") as archivo:
            archivo.write(
                self.clavePublica.public_bytes(  # Corregido: usar self.clavePublica
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

        print(f"Claves generadas como {self.rutaClavePrivada} y {self.rutaClavePublica}")

    def FirmarArchivo(self, rutaArchivo):
        if not rutaArchivo or rutaArchivo.strip() == "":
            raise ValueError("Debe especificar una ruta de archivo válida")
            
        if not os.path.exists(rutaArchivo):
            raise FileNotFoundError(f"El archivo no existe: {rutaArchivo}")
        
        if os.path.getsize(rutaArchivo) == 0:
            raise ValueError(f"El archivo está vacío: {rutaArchivo}")
        
        # Cargar clave privada si no existe
        if self.clavePrivada is None:
            with open(self.rutaClavePrivada, "rb") as f:
                self.clavePrivada = serialization.load_pem_private_key(
                    f.read(),
                    password=None
                )
        
        # Leer el archivo y firmarlo
        with open(rutaArchivo, "rb") as f:
            datos = f.read()
        
        firma = self.clavePrivada.sign(
            datos,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        # Guardar la firma
        with open(f"{rutaArchivo}.sig", "wb") as f:
            f.write(firma)
        
        print(f"Archivo firmado. Firma guardada en {rutaArchivo}.sig")
        return firma