import argparse

def get_parser():
    """Prepara el parser para interpretar las opciones pasadas por linea de comandos"""
    parser = argparse.ArgumentParser()
    add_methods(parser)

    return parser

def add_methods(parser):
    """Agrega al parser los distintos métodos de resolucion para encontrar la raíz de la funcion"""
    methods = parser.add_subparsers(
        title='metodo',
        dest='method',
        description='Metodo a utilizar para obtener la raiz de la funcion'
    )
    methods.required = True
    add_bisection_method(methods)
    add_fixed_point_method(methods)
    add_newton_raphson_method(methods)

def add_bisection_method(methods):
    """Agrega el método de biseccion al parser"""
    bisection_parser = methods.add_parser('biseccion')
    bisection_parser.add_argument('a', type=int, help='Primer punto del intervalo a aplicar el metodo')
    bisection_parser.add_argument('b', type=int, help='Segundo punto del intervalo a aplicar el metodo')

def add_fixed_point_method(methods):
    """Agrega el método de punto fijo al parser"""
    fixed_point_parser = methods.add_parser('punto-fijo')
    fixed_point_parser.add_argument('inicial', type=int, help='Valor inicial a usar al aplicar el metodo')

def add_newton_raphson_method(methods):
    """Agrega el método de Newton Raphson al parser"""
    newton_raphson_parser = methods.add_parser('newton-raphson')
    newton_raphson_parser.add_argument('inicial', type=int, help='Valor inicial a usar al aplicar el metodo')
