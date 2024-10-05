import turtle
import numpy as np

def halvorsen(x, y, z, a=1.4):
    """
    Calcula el siguiente punto en el atractor de Halvorsen.
    """
    x_dot = -a * x - 4 * y - 4 * z - y**2
    y_dot = -a * y - 4 * z - 4 * x - z**2
    z_dot = -a * z - 4 * x - 4 * y - x**2
    return x + x_dot * dt, y + y_dot * dt, z + z_dot * dt

# Parámetros de la simulación
dt = 0.01  # Paso de tiempo
num_steps = 1000000000  # Número de pasos

# Posiciones iniciales
x = 0.1
y = 0.0
z = 0.0

# Configuración de la pantalla de turtle
screen = turtle.Screen()
screen.title("Atractor de Halvorsen")
screen.bgcolor("black")
screen.setup(width=800, height=800)

# Configuración del turtle
halvorsen_turtle = turtle.Turtle()
halvorsen_turtle.speed(0)
halvorsen_turtle.pensize(2)
halvorsen_turtle.color("white")
halvorsen_turtle.penup()
halvorsen_turtle.goto(x * 10, y * 10)
halvorsen_turtle.pendown()

# Escala para ajustar la visualización
scale = 10

# Simulación del atractor de Halvorsen
for _ in range(num_steps):
    x, y, z = halvorsen(x, y, z)
    halvorsen_turtle.goto(x * scale, y * scale)

# Ocultar el turtle y mostrar la ventana
halvorsen_turtle.hideturtle()
screen.mainloop()
