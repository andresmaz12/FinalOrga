from hashing import Hashear
from cifradoHuff import CifradoDatos
import os

class Main():
    def __init__(self):
        self.texto = None
        self.compresion = None
        self.hashear = Hashear()
        self.huffmn = CifradoDatos(None)
    
    def Menu(self):
        print("Bienvenido")
        while True:
            print("\nQue desea hacer")
            print("1.) Ingresar mensaje")
            print("2.) Calcular hash FNV-1")
            print("3.) Comprimir mensaje")
            print("4.) Firmar hash")
            print("5.) Salir")
            opcion = input("Opción: ")
            
            if opcion == "1":
                self.IngresoTexto()
            elif opcion == "2":
                self.Hashear()
            elif opcion == "3":
                self.Codificar()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida")

    def IngresoTexto(self):
        texto = input("Que texto desea ingresar: ")
        
        with open("texto.txt", "w", encoding='utf-8') as f:  # Corregido: modo "w" y encoding
            f.write(texto)
        
        self.texto = "texto.txt"  # Guardar la ruta del archivo
        print(f"Texto guardado en {self.texto}")

    def Hashear(self):
        if self.texto is None:
            print("No se ha ingresado ningun texto")
        else:
            self.hashear.hashFnv1(self.texto)  # Corregido: llamar al método correctamente
    
    def Codificar(self):
        if self.texto is None:
            print("No se ha ingresado ningun texto")
        else:
            with open(self.texto, "r", encoding='utf-8') as f:
                contenido = f.read()
            self.huffmn.ComprimirTexto(contenido)

    def EnvioTexto(self):
        pass

    def RecepcionTexto(self):
        pass

if __name__ == "__main__":  # Corregido: era "__Main__"
    app = Main()
    app.Menu()