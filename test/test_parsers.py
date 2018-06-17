import unittest

from parsers import get_parser
from methods import Bisection, FixedPoint
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        self.parser = get_parser()
 
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
        bisection = Bisection(lambda x: x**2 - 2, 1, 2)
        self.assertEqual(next(bisection), 1.5)
        self.assertEqual(next(bisection), 1.25)
        self.assertEqual(bisection.get_error(), 0.4375)

    def test_fixed_point(self):
        fixed_point = FixedPoint(lambda x: x**2 - 2, 1, 2)
        self.assertEqual(round(next(fixed_point), 3), 1.333)
        self.assertEqual(next(fixed_point), 1.4)
        self.assertEqual(round(fixed_point.get_error(), 3), 0.04)

