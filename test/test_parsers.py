import unittest

from parsers import get_parser
from methods import Bisection, FixedPoint, NewtonRaphson
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        self.parser = get_parser()
        self.function = lambda x: x**2 - 2
        self.derivative = lambda x: 2*x
 
    def test_bisection_parser(self):
        args = self.parser.parse_args(['biseccion', '1', '2'])
        self.assertEqual(args.method, 'biseccion')
        self.assertEqual(args.a, 1)
        self.assertEqual(args.b, 2)
 
    def test_fixed_point_parser(self):
        args = self.parser.parse_args(['punto-fijo', '1', '2'])
        self.assertEqual(args.method, 'punto-fijo')
        self.assertEqual(args.a, 1)
        self.assertEqual(args.b, 2)
 
    def test_newton_raphson_parser(self):
        args = self.parser.parse_args(['newton-raphson', '1'])
        self.assertEqual(args.method, 'newton-raphson')
        self.assertEqual(args.inicial, 1)

    def test_bisection(self):
        bisection = Bisection(self.function, 1, 2)
        self.assertEqual(next(bisection), 1.5)
        self.assertEqual(next(bisection), 1.25)
        self.assertEqual(bisection.get_error(), 0.4375)

    def test_fixed_point(self):
        fixed_point = FixedPoint(self.function, 1, 2)
        self.assertEqual(round(next(fixed_point), 3), 1.333)
        self.assertEqual(round(next(fixed_point), 3), 1.4)
        self.assertEqual(round(fixed_point.get_error(), 3), 0.04)

    def test_newton_raphson(self):
        newton_raphson = NewtonRaphson(self.function, self.derivative, 2)
        self.assertEqual(round(next(newton_raphson), 3), 1.5)
        self.assertEqual(round(next(newton_raphson), 3), 1.417)
        self.assertEqual(round(newton_raphson.get_error(), 3), 0.007)

