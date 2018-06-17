class Method:
    def __init__(self, func):
        self.func = func
        self.valor_anterior = None

    def __iter__(self):
        return self

    def __next__(self):
        """Must be overrided in derived classes"""
        raise NotImplementedError()

    def get_error(self):
        return abs(self.func(self.valor_anterior))

class BolzanoException(Exception):
    pass

class IntervalMethod(Method):
    def __init__(self, func, valor_minimo, valor_maximo):
        super().__init__(func)
        self.valor_minimo = valor_minimo
        self.valor_maximo = valor_maximo
        self.bolzano_check(self.valor_minimo, self.valor_maximo)

    def __next__(self):
        if not self.valor_anterior is None:
            self.make_new_interval()

        self.valor_anterior = self.get_next_value()
        return self.valor_anterior

    def bolzano_check(self, valor_minimo, valor_maximo):
        if self.func(valor_minimo) < 0 and self.func(valor_maximo) < 0:
            raise BolzanoException('El intervalo elegido no cumple Bolzano')

        if self.func(valor_minimo) > 0 and self.func(valor_maximo) > 0:
            raise BolzanoException('El intervalo elegido no cumple Bolzano')

    def get_next_value(self):
        """Must be overrided in derived classes"""
        raise NotImplementedError()

    def make_new_interval(self):
        try:
            self.bolzano_check(self.valor_anterior, self.valor_maximo)
            self.valor_minimo = self.valor_anterior
        except BolzanoException:
            self.valor_maximo = self.valor_anterior

class Bisection(IntervalMethod):
    def get_next_value(self):
        return (self.valor_minimo + self.valor_maximo) / 2

class FixedPoint(IntervalMethod):
    def get_next_value(self):
        a = self.valor_minimo
        b = self.valor_maximo
        f = self.func

        return b - (b-a)/(f(b)-f(a)) * f(b)

class NewtonRaphson(Method):
    def __init__(self, func, derivative, initial_value):
        super().__init__(func)
        self.valor_anterior = initial_value
        self.derivative = derivative

    def __next__(self):
        valor_anterior = self.valor_anterior
        func = self.func
        derivative = self.derivative
        self.valor_anterior = valor_anterior - func(valor_anterior)/derivative(valor_anterior)
        return self.valor_anterior

