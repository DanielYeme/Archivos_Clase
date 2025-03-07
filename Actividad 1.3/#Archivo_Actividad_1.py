# Archivos Actividad 1.3

class Torniquete:
    def __init__(self):
        self.estado = "Bloqueado"

    def procesar_entrada(self, entrada):


        if self.estado == "Bloqueado":
            if entrada == 1:
                self.estado = "Desbloqueado"
                print("Moneda ingresada. Torniquete desbloqueado.")

            elif entrada == 2:
                print("Torniquete bloqueado. No puede pasar.")
        elif self.estado == "Desbloqueado":

            if entrada == 1:
                print("Moneda ingresada. Pero el torniquete ya se encuentra desbloqueado.")
            elif entrada == 2:
                self.estado = "Bloqueado"
                print("Paso permitido. Torniquete bloqueado nuevamente.")

    def ejecutar(self):
        while True:
            print(f"Estado actual: {self.estado}")
            try:
                entrada = int(input("Elige una opción; 1 para Echar moneda, 2 para Empujar (0 para salir): "))
                if entrada == 0:
                    print("Saliendo del programa...")
                    break
                self.procesar_entrada(entrada)
            except ValueError:
                print("Por favor, ingresa un número válido")

if __name__ == "__main__":
    torniquete = Torniquete()
    torniquete.ejecutar()
