from methods import Bisection, FixedPoint, NewtonRaphson
from parsers import get_parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    function = lambda x: x**2 - 2
    derivative = lambda x: 2*x
    error_esperado = 0.00001

    if args.method == 'biseccion':
        method = Bisection(function, args.a, args.b)
    if args.method == 'punto-fijo':
        method = FixedPoint(function, args.a, args.b)
    if args.method == 'newton-raphson':
        method = NewtonRaphson(function, derivative, args.inicial)

    for i, valor in enumerate(method, 1):
        if method.get_error() <= error_esperado:
            break

    print(f'Se obtuvo el valor {valor} en {i} iteraciones')

