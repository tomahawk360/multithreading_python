# multithreading_python

Simula un juego de "Battle Royale" con 120 jugadores.

Dicho juego tiene un Lobby que recibe a todos los jugadores que entren al juego, y cuatro modalidades:
  -Partida Estándar: Recibe máximo 15 jugadores en la partida, la cual dura 7 segundos. Además, tiene una cola que recibe 7 jugadores en espera.
  -Partida Versus: Recibe máximo 2 jugadores en la partida, la cual dura 3 segundos. Además, tiene una cola que recibe 4 jugadores en espera.
  -Partida Rápida: Recibe máximo 10 jugadores en la partida, la cual dura 6 segundos. Además ,tiene una cola que recibe 8 jugadores en espera.
  -Partida Especial Navidad: Recibe máximo 12 jugadores en la partida, la cual dura 5 segundos. Además, tiene una cola que recide 10 jugadores en espera.
  
Cada jugador esta representado en una hebra, en la función jugador.
Reglas:
  -Al entrar un jugador al juego, este va al Lobby inmediatamente, y queda allí hasta escoger un modo de juego.
  -La elección de modo de juego de cada jugador es aleatoria.
  -Una vez escoge, abandona el Lobby y se dirige a la cola de la partida con el modo de juego escogido.
  -En la cola todos los jugadores esperan mientras la partida este en curso. Una vez esta termine, los jugadores entran en orden de llegada a la partida.
  -La partida no comienza hasta que esten todos los cupos llenos.
  -Si un jugador escoge una partida, y la cola de dicha partida esta con todos los cupos llenos, se queda esperando en el Lobby hasta que se depeje.
  -Una vez el jugador termine su partida, este abandona el juego definitivamente.
