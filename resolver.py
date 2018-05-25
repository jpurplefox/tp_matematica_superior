import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title='metodo',
        dest='metodo',
        description='Metodo a utilizar para obtener la raiz de la funcion'
    )

    biseccion_parser = subparsers.add_parser('biseccion')
    biseccion_parser.add_argument('a', type=int, help='Primer punto del intervalo a aplicar el metodo')
    biseccion_parser.add_argument('b', type=int, help='Segundo punto del intervalo a aplicar el metodo')

    punto_fijo_parser = subparsers.add_parser('punto-fijo')
    punto_fijo_parser.add_argument('inicial', type=int, help='Valor inicial a usar al aplicar el metodo')

    newton_raphson_parser = subparsers.add_parser('newton-raphson')
    newton_raphson_parser.add_argument('inicial', type=int, help='Valor inicial a usar al aplicar el metodo')

    args = parser.parse_args()

    if args.metodo == 'biseccion':
        print(f'Resolviendo por biseccion con intervalo [{args.a},{args.b}]')
    if args.metodo == 'punto-fijo':
        print(f'Resolviendo por punto fijo con valor inicial {args.inicial}')
    if args.metodo == 'newton-raphson':
        print(f'Resolviendo por Newton-Raphson con valor inicial {args.inicial}')
