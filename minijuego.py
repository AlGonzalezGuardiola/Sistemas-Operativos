import inquirer
import random

class Partida():
    def __init__(self):
        self.jugadores_info = {}
        self.f = TratamientoFichero('ttt.txt')

    def mostrar_menu(self):
        questions = [
            inquirer.List("opcion",
                          message="Selecciona una opción:",
                          choices=['Iniciar Partida', 'Ver Ranking', 'Salir'],
                          ),
        ]
        respuesta = inquirer.prompt(questions)["opcion"]
        return respuesta

    def ejecutar_opcion(self, opcion):
        if opcion == 'Iniciar Partida':
            self.iniciar_partida()
        elif opcion == 'Ver Ranking':
            self.ver_ranking()
        elif opcion == 'Salir':
            print("¡Hasta luego!")

    def iniciar_partida(self):
        self.jugadores_info = {}
        self.jugadores = int(input("¿Cuántos vais a jugar? "))

        if self.jugadores <= 0:
            print("Para qué me enciendes si no vas a jugar.")
            return

        for i in range(1, self.jugadores + 1):
            nombre = input(f"Ingrese el nombre del jugador {i}: ")
            self.jugadores_info[nombre] = {"puntos": 0, "intentos_maximos": 4}

        print("Jugadores registrados:", list(self.jugadores_info.keys()))

        for jugador in self.jugadores_info.keys():
            self.numero_azar = random.randint(1, 10)
            print(
                f"Bienvenido {jugador}! En esta partida voy a elegir un número al azar del 1 al 10. Cuanto antes lo adivines, más puntos ganarás.")
            self.respuesta(jugador)

        # Después de la partida, actualizamos el ranking en el archivo
        self.actualizar_ranking()

    def respuesta(self, jugador):
        intentos_maximos = self.jugadores_info[jugador]["intentos_maximos"]
        for intento in range(1, intentos_maximos + 1):
            pregunta = [
                inquirer.List("Posibles Respuestas",
                              message=f"Intento {intento}: {jugador}, elige un número del 1 al 10",
                              choices=[str(i) for i in range(1, 11)]
                              ),
            ]
            respuesta = int(inquirer.prompt(pregunta)["Posibles Respuestas"])

            if respuesta == self.numero_azar:
                puntos_ganados = 5 * (intentos_maximos - intento + 1)
                print(
                    f"¡Adivinaste el número en el intento {intento}! Ganaste {puntos_ganados} puntos.")
                self.jugadores_info[jugador]["puntos"] += puntos_ganados
                break
            else:
                if respuesta < self.numero_azar:
                    print("El número es más alto. ¡Sigue intentando!")
                else:
                    print("El número es más bajo. ¡Sigue intentando!")

        if intento == intentos_maximos:
            print(
                f"Agotaste tus {intentos_maximos} intentos. El número era {self.numero_azar}. Ganaste {self.jugadores_info[jugador]['puntos']} puntos.")

    def ver_ranking(self):
        ranking = self.f.read_file()
        if not ranking:
            print("Aún no hay jugadores registrados.")
        else:
            print("Ranking de Jugadores:")
            print(ranking)

    def actualizar_ranking(self):
        for jugador, info in sorted(self.jugadores_info.items(), key=lambda x: x[1]['puntos'], reverse=True):
            self.f.write_file(f"{jugador}: {info['puntos']} puntos")

class TratamientoFichero():
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def write_file(self, line_to_write):
        with open(self.nombre_fichero, "a") as f:
            f.write(line_to_write)
            f.write("\n")

    def read_file(self):
        try:
            with open(self.nombre_fichero, "r") as f:
                return f.read()
        except FileNotFoundError:
            return None

if __name__ == "__main__":
    partida = Partida()
    while True:
        opcion = partida.mostrar_menu()
        partida.ejecutar_opcion(opcion)
        if opcion == 'Salir':
            break

