import threading as td
import random
import os
import datetime
import time
class Juego():
    def __init__(self):
        if not os.path.exists("./textfiles"):
            os.mkdir("./textfiles")

        self.f_lobby = open("./textfiles/Lobby.txt",'w')
        self.f_p_estandar = open("./textfiles/PartidaEstandar.txt",'w')
        self.f_p_versus = open("./textfiles/PartidaVersus.txt",'w')
        self.f_p_rapida = open("./textfiles/PartidaRápida.txt",'w')
        self.f_p_navidad = open("./textfiles/PartidaEspecialNavidad.txt",'w')
        self.f_salida = open("./textfiles/Salida.txt",'w')

        self.cant_list = {
            'colas' : [7, 4, 8, 10],
            'duracion' : [7, 3, 6, 5],
            'partida' : [15, 2, 10, 12]
        }

        self.c_colas = [0, 0, 0, 0]
        self.c_partidas = [0, 0, 0, 0]

        self.lock1 = td.Lock()
        self.lock2  =td.Lock()
        self.lock3 = td.Lock()

        self.c_estandar = td.Semaphore(7)
        self.c_versus = td.Semaphore(4)
        self.c_rapida = td.Semaphore(8)
        self.c_navidad = td.Semaphore(10)

        self.c_list = [self.c_estandar, self.c_versus, self.c_rapida, self.c_navidad]

        self.p_estandar = td.Semaphore(15)
        self.p_versus = td.Semaphore(2)
        self.p_rapida = td.Semaphore(10)
        self.p_navidad = td.Semaphore(12)

        self.p_list = [self.p_estandar, self.p_versus, self.p_rapida, self.p_navidad]

        
    def jugador(self, name):
        #Variable
        name = "Jugador {name}".format(name=name)

        tiempo_entrada = datetime.datetime.now()

        #Escoger partida
        partida_selec = 1
        partida_selec = random.randint(0, 3)

        #Checkear cola
        with self.c_list[partida_selec]:

            #Ir de lobby a cola

            self.lock1.acquire()

            tiempo_cola = datetime.datetime.now()
            self.c_colas[partida_selec] += 1
            print(name, "c_colas:", self.c_colas[partida_selec])

            self.lock1.release()

            match partida_selec:
                case 0:
                    self.f_lobby.write("{name}, {tiempo_entrada}, Partida Estándar, {tiempo_cola}\n".format(name=name, tiempo_entrada=tiempo_entrada, tiempo_cola=tiempo_cola))
                case 1:
                    self.f_lobby.write("{name}, {tiempo_entrada}, Partida Versus, {tiempo_cola}\n".format(name=name, tiempo_entrada=tiempo_entrada, tiempo_cola=tiempo_cola))
                case 2:
                    self.f_lobby.write("{name}, {tiempo_entrada}, Partida Rápida, {tiempo_cola}\n".format(name=name, tiempo_entrada=tiempo_entrada, tiempo_cola=tiempo_cola))
                case 3:
                    self.f_lobby.write("{name}, {tiempo_entrada}, Partida Especial Navidad, {tiempo_cola}\n".format(name=name, tiempo_entrada=tiempo_entrada, tiempo_cola=tiempo_cola))


        #Esperar en cola
        with self.p_list[partida_selec]:

            #Ir de cola a partida
            self.lock2.acquire()

            tiempo_partida = datetime.datetime.now()
            self.c_colas[partida_selec] -= 1
            self.c_partidas[partida_selec] += 1
            print(name, "c_colas:", self.c_colas[partida_selec])
            print(name, "c_partidas:", self.c_partidas[partida_selec])

            self.lock2.release()

            match partida_selec:
                case 0:
                    self.f_p_estandar.write("{name}, {tiempo_cola}, {tiempo_partida}\n".format(name=name, tiempo_cola=tiempo_cola, tiempo_partida=tiempo_partida))
                case 1:
                    self.f_p_versus.write("{name}, {tiempo_cola}, {tiempo_partida}\n".format(name=name, tiempo_cola=tiempo_cola, tiempo_partida=tiempo_partida))
                case 2:
                    self.f_p_rapida.write("{name}, {tiempo_cola}, {tiempo_partida}\n".format(name=name, tiempo_cola=tiempo_cola, tiempo_partida=tiempo_partida))
                case 3:
                    self.f_p_navidad.write("{name}, {tiempo_cola}, {tiempo_partida}\n".format(name=name, tiempo_cola=tiempo_cola, tiempo_partida=tiempo_partida))
            

            #Jugar
            time.sleep(self.cant_list['duracion'][partida_selec])

            #Abandonar juego
            self.lock2.acquire()

            self.c_partidas[partida_selec] -= 1
            tiempo_salida = datetime.datetime.now()
            print(name, "c_partidas:", self.c_partidas[partida_selec])
            
            self.lock2.release()

            self.f_salida.write("{name}, {tiempo_salida}\n".format(name=name, tiempo_salida=tiempo_salida))

        return

    def fin(self):
        self.f_salida.close()
        self.f_p_navidad.close()
        self.f_p_rapida.close()
        self.f_p_versus.close()
        self.f_p_estandar.close()
        self.f_lobby.close()

if __name__ == "__main__":

    juego = Juego()
    threads = []

    for i in range(120):
        x = td.Thread(target=juego.jugador, args=(i,))
        threads.append(x)
        x.start()

    if len(threads) == 0:
        juego.fin()