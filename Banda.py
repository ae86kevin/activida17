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



    def inscribirBanda(self,nombre, institucion,categoria):
        if nombre in self.bandas:
            print("\nBanda ya esta registrada")
        else:
            categoria =categoria.lower()
            if categoria in  ["primaria", "basico","diversificado"]:
                self.bandas[nombre] = {
                    "institucion": institucion,
                    "categoria": categoria,
                    "puntajes":{}
                }
                self.guardar_bandas()
                print("Banda registrada exitosamente")
            else:
                print("Banda no registrada")

    def evalucion(self,nombre,puntajes):
        if nombre not in self.bandas:
            print("\nBanda no registrada")
            return

        evaluacionP= ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]


        calificacion = 0

        for var in evaluacionP:
            if var in puntajes:
                valor=puntajes[var]
                if valor >= 0:
                    if valor <= 10:
                        calificacion=calificacion+1
                    else:
                        print("\nPuntaje mayor a 10 en: ",var)

                else:
                    print("puntaje mayor a 10 en", var)
                    return
            else:
                print("puntaje mayor a  0 en", var)
                return
        else:
            print("informaion faltnate ")
            return

        if calificacion ==5:
            self.bandas[nombre]["puntualidad"]=calificacion
            print("registadoa")







