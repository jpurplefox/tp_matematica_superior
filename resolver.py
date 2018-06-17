from methods import Bisection, FixedPoint
from parsers import get_parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    function = lambda x: x**2 - 2

    if args.method == 'biseccion':
        method = Bisection(function, args.a, args.b)
    if args.method == 'punto-fijo':
        method = FixedPoint(function, args.a, args.b)
    if args.method == 'newton-raphson':
        print(f'Resolviendo por Newton-Raphson con valor inicial {args.inicial}')
        exit()

    for i, valor in enumerate(method, 1):
        if method.get_error() <= 0.00001:
            break

    print(f'Se obtuvo el valor {valor} en {i} iteraciones')

