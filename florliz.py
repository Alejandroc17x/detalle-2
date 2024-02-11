from turtle import *
import colorsys
import random

# Efecto de brillo en toda la pantalla
def draw_sparkles():
    penup()
    for _ in range(500):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        goto(x, y)
        dot(random.randint(1, 3), 'white')

bgcolor("black")
tracer(2)
pensize(2)
h = 0

# Función para generar colores de rosa
def generate_pink_color(h):
    pink_color = colorsys.hsv_to_rgb(h, 0.9, 1)
    r, g, b = pink_color
    return r, g, b

# Dibujar el gráfico
for i in range(195):
    r, g, b = generate_pink_color(h)
    pencolor(r, g, b)
    h += 0.006
    lt(179)
    backward(i * 0.1)
    circle(i * 0.3, 120)
    rt(14)
    forward(i * 0.1)
    circle(i * 0.3, 120)

# Ajustes para el texto
penup()
goto(0, -350)  # Ubicación en la parte inferior
pendown()

# Borde blanco para la letra
color("white")
write("TE AMO MI NIÑA PRECIOSA\nESTOY MUY ORGULLOSO DE TI", align='center', font=('Courier', 20, 'bold'))

# Efecto de brillos
draw_sparkles()

done()
