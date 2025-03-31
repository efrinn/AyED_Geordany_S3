# Ejemplo de uso de la clase Edad para calcular la edad media de un grupo de personas

class Edad:
    def __init__(self, edad):
        self.edad = edad
    
    def calcular_media(self):
        return sum(self.edad) / len(self.edad)
    
    def mostrar_media(self):
        media = self.calcular_media()
        print(f"La edad media es: {media:.2f} años")

def main():
    edades = []
    while True:
        try:
            edad = int(input("Introduce una edad (o -1 para terminar): "))
            if edad == -1:
                break
            edades.append(edad)
        except ValueError:
            print("Por favor, introduce un número entero válido.")
        
    if(not edades):
        print("No se han introducido edades.")
    else:
        edad_obj = Edad(edades)
        print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()