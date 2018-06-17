class BolzanoException(Exception):
    pass

class Bisection:
    def __init__(self, func, valor_minimo, valor_maximo):
        self.func = func
        self.valor_minimo = valor_minimo
        self.valor_maximo = valor_maximo
        self.bolzano_check(self.valor_minimo, self.valor_maximo)
        self.valor_anterior = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.valor_anterior is None:
            if self.get_error(self.valor_anterior) <= 0.00001:
                raise StopIteration()

            self.make_new_interval()

        self.valor_anterior = (self.valor_minimo + self.valor_maximo) / 2
        return self.valor_anterior

    def bolzano_check(self, valor_minimo, valor_maximo):
        if self.func(valor_minimo) < 0 and self.func(valor_maximo) < 0:
            raise BolzanoException('El intervalo elegido no cumple Bolzano')

        if self.func(valor_minimo) > 0 and self.func(valor_maximo) > 0:
            raise BolzanoException('El intervalo elegido no cumple Bolzano')

    def get_error(self, valor):
        return abs(self.func(valor))
        
    def make_new_interval(self):
        try:
            self.bolzano_check(self.valor_anterior, self.valor_maximo)
            self.valor_minimo = self.valor_anterior
        except BolzanoException:
            self.valor_maximo = self.valor_anterior
