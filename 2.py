import turtle
import time
import random
import pygame  # Importa pygame para los sonidos

# Inicializa pygame para poder usar sonidos
pygame.init()

# Carga los sonidos
sonido_comida = pygame.mixer.Sound("sonidos/laser.mp3")  # Sonido cuando come la comida
sonido_colision = pygame.mixer.Sound("sonidos/golpe.mp3")  # Sonido cuando colisiona
pygame.mixer.music.load("sonidos/explosion.mp3")  # Música de fondo
pygame.mixer.music.play(-1)  # Reproduce la música en bucle infinito

delay = 0.1  # Retraso para controlar la velocidad de la serpiente

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Juego de la Serpiente")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)  # Desactiva la actualización automática de la ventana

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Cuerpo de la serpiente
cuerpos = []

# Puntaje
puntaje = 0
mejor_puntaje = 0

# Texto del puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Puntaje: 0  Mejor Puntaje: 0", align="center", font=("Courier", 24, "normal"))

# Funciones de movimiento
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def mover():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Controles de teclado
ventana.listen()
ventana.onkey(arriba, "Up")
ventana.onkey(abajo, "Down")
ventana.onkey(izquierda, "Left")
ventana.onkey(derecha, "Right")

# Bucle principal del juego
while True:
    ventana.update()

    # Colisión con los bordes
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        pygame.mixer.Sound.play(sonido_colision)  # Reproduce sonido de colisión
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # Esconder el cuerpo de la serpiente
        for cuerpo in cuerpos:
            cuerpo.goto(1000, 1000)  # Mueve los segmentos fuera de la pantalla
        cuerpos.clear()

        # Reiniciar el puntaje
        puntaje = 0
        texto.clear()
        texto.write("Puntaje: {}  Mejor Puntaje: {}".format(puntaje, mejor_puntaje), align="center", font=("Courier", 24, "normal"))

    # Colisión con la comida
    if cabeza.distance(comida) < 20:
        pygame.mixer.Sound.play(sonido_comida)  # Reproduce sonido al comer
        # Mover la comida a una posición aleatoria
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)

        # Agregar un nuevo segmento al cuerpo de la serpiente
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("gray")
        nuevo_cuerpo.penup()
        cuerpos.append(nuevo_cuerpo)

        # Aumentar el puntaje
        puntaje += 10
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje

        texto.clear()
        texto.write("Puntaje: {}  Mejor Puntaje: {}".format(puntaje, mejor_puntaje), align="center", font=("Courier", 24, "normal"))

    # Mover el cuerpo de la serpiente
    for i in range(len(cuerpos) - 1, 0, -1):
        x = cuerpos[i - 1].xcor()
        y = cuerpos[i - 1].ycor()
        cuerpos[i].goto(x, y)

    # Mover el primer segmento al lugar de la cabeza
    if len(cuerpos) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpos[0].goto(x, y)

    mover()

    # Colisión con el propio cuerpo
    for cuerpo in cuerpos:
        if cuerpo.distance(cabeza) < 20:
            pygame.mixer.Sound.play(sonido_colision)  # Reproduce sonido de colisión
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            # Esconder el cuerpo de la serpiente
            for cuerpo in cuerpos:
                cuerpo.goto(1000, 1000)
            cuerpos.clear()

            # Reiniciar el puntaje
            puntaje = 0
            texto.clear()
            texto.write("Puntaje: {}  Mejor Puntaje: {}".format(puntaje, mejor_puntaje), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
