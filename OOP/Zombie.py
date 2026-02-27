from enemigo import * # type: ignore

class Zombie(Enemigo): # type: ignore
    def __init__(self, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo="Zombie", puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):S
        print("*Hummmm........*")

    def propagar_enfermedad(self):
        print("El zombie eata tratando de propagar la enfermedad!!")