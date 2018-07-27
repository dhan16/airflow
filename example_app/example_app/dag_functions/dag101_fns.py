import datetime
import time

from example_app.tutorial.classes.complex import Complex


def print_complex():
    x = Complex(3.0, -4.5)
    x.print()
    y = Complex(1.0, time.time())
    y.print()
    z = Complex(datetime.datetime.now(), 2)
    z.print()
    return 'Whatever'


def print_number(n):
    x = Complex(n, 0)
    x.print()

