from herramientas import greet
from herramientas import calculate_circle_area as ca

def execute_calculations():
    print(greet("Andres", 26, "male"))
    radius = 10
    area = ca (radius)
    print (f"The area of a circle with radius {radius} is: {area}")

if __name__ == "__name__":
    execute_calculations()