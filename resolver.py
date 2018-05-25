from parsers import get_parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    if args.method == 'biseccion':
        print(f'Resolviendo por biseccion con intervalo [{args.a},{args.b}]')
    if args.method == 'punto-fijo':
        print(f'Resolviendo por punto fijo con valor inicial {args.inicial}')
    if args.method == 'newton-raphson':
        print(f'Resolviendo por Newton-Raphson con valor inicial {args.inicial}')
