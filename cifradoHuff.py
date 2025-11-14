from dahuffman import HuffmanCodec  # Libreria usada para compresion por algoritmo de huffman 
import sys

class CifradoDatos():
    def __init__(self, textoComp):  # Corregido: era "tectoComp"
        self.codec = None
        self.textoComp = textoComp

    def ComprimirTexto(self, texto):
        self.codec = HuffmanCodec.from_data(texto) 
        comprimido = self.codec.encode(texto)

        with open("textoComprimido.huff", "wb") as f:
            f.write(comprimido)

        self.textoComp = comprimido

        print("Texto comprimido como textoComprimido.huff")
        print(f"Tamaño antes de ser comprimido: {sys.getsizeof(texto)} bytes")  # Corregido: caracteres especiales
        print(f"Tamaño después de ser comprimido: {sys.getsizeof(comprimido)} bytes")

    def DescomprimirTexto(self):
        ruta = input("Ingrese la ruta de su archivo comprimido: ")
        
        with open(ruta, "rb") as f:
            comprimido = f.read()  # Corregido: leer todo el archivo
        
        descomprimido = self.codec.decode(comprimido)  # Corregido: usar decode() no llamar codec como función

        print(f"Texto descomprimido: {descomprimido}")