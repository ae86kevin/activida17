class Bandas:
    def __init__(self):
        self.bandas = {}
        self.cargar_bandas()

    def cargar_bandas(self):
        try:
            with open("bandas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nombreBanda, institucion, categoria = linea.split(":")
                        self.bandas[nombreBanda] = {
                            "Institucion": institucion,
                            "Categoria": categoria
                        }
        except FileNotFoundError:
            print("No se encontro archivo bandas.txt, Creando uno archivo bandas.txt")


    def guardar_bandas(self):
        with open("bandas.txt", "w", encoding="utf-8") as archivo:
            for nombreBanda,dato in self.bandas.items():
                archivo.write(f"{nombreBanda}:{dato['Categoria']}: {dato['Institucion']}\n")


class ParticipantesBandas:
    def __init__(self,nombreBanda,institucion):
        self.nombreBanda = nombreBanda
        self.institucion = institucion

    def mostrarInformacion(self):
        return f"Nombre: {self.nombreBanda},{self.institucion} "

class BandaEscolar(ParticipantesBandas):
    categoria=["primaria","basico","diversifcado"]
    categoria2=["ritmo", "uniformidad","coregradia","puntalida"]

    def __init__(self,nombreBanda,institucion,categoria):
        super().__init__(nombreBanda,institucion)