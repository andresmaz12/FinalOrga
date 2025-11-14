import fnvhash  # Libreria para hacer el hashing FNV-1

class Hashear:
    def __init__(self):
        pass

    def hashFnv1(self, texto):
        datos = None
        with open(texto, "rb") as f:
            datos = f.read()  # Corregido: f.read() sin parámetro

        print("========================")
        hash32 = fnvhash.fnv1_32(datos)
        print(f"FNV-1 32 bits: {hash32}")
        print("========================\n")

        print("========================")
        hash64 = fnvhash.fnv1_64(datos)  # Corregido: debe ser fnv1_64
        print(f"FNV-1 64 bits: {hash64}")
        print("========================\n")

        print("========================")
        hash_1a_32 = fnvhash.fnv1a_32(datos)  # Corregido: debe ser fnv1a_32
        print(f"FNV-1a 32 bits: {hash_1a_32}")
        print("========================\n")
        
        print("========================")
        hash_1a_64 = fnvhash.fnv1a_64(datos)  # Corregido: debe ser fnv1a_64
        print(f"FNV-1a 64 bits: {hash_1a_64}")
        print("========================\n")