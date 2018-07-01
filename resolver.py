from methods import Bisection, FixedPoint, NewtonRaphson
from parsers import get_parser
from math import log

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    function = lambda x: 3143680 - 2*2**x - 51200*x
    derivative = lambda x: - 2*2**x*0.69314718 - 51200
    fixed_point_function = lambda x: log((3143680 - 51200*x)/2, 2)
    error_esperado = args.error

    if args.method == 'biseccion':
        method = Bisection(function, args.a, args.b, args.redondeo)
    if args.method == 'punto-fijo':
        method = FixedPoint(function, fixed_point_function, args.inicial, args.redondeo)
    if args.method == 'newton-raphson':
        method = NewtonRaphson(function, derivative, args.inicial, args.redondeo)

    valor_anterior = 0
    for i, valor in enumerate(method, 1):
        if args.corte == 'abs':
            error = abs(valor_anterior - valor)
        elif args.corte == 'rel':
            error = abs((valor_anterior - valor) / valor)
        elif args.corte == 'funct-val':
            error = abs(function(valor))
        error = round(error, args.redondeo)
        print(f'n={i}, xn-1={valor_anterior}, xn={valor}, e={error} {method.get_info()}')
        if error <= error_esperado:
            break
        if i >= 1000:
            break

        valor_anterior = valor

    print(f'Se obtuvo el valor {valor} en {i} iteraciones')

