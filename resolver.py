from methods import Bisection, FixedPoint, NewtonRaphson
from parsers import get_parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    function = lambda x: 3143680 - 2*2**x - 51200*x
    derivative = lambda x: -2**x*0.69314718 - 51200
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

