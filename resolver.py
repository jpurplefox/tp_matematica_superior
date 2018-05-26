from methods import Bisection
from parsers import get_parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    if args.method == 'biseccion':
        bisection = Bisection(lambda x: x**2 - 2, args.a, args.b)
        for i, valor in enumerate(bisection, 1):
            pass
        print(f'Se obtuvo el valor {valor} en {i} iteraciones')
    if args.method == 'punto-fijo':
        print(f'Resolviendo por punto fijo con valor inicial {args.inicial}')
    if args.method == 'newton-raphson':
        print(f'Resolviendo por Newton-Raphson con valor inicial {args.inicial}')
