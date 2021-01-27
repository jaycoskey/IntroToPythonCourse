#!/usr/bin/env python3

# We saw in HW #7 that Celcius and Fahrenheit are related by the formula
#     def c2f(temp_f):
#        return (5/9) * temp_f - 32
# Here is an exercise to demonstrates that lambdas can be function inputs (i.e., arguments),
# and can also be function outputs (i.e., return values).

def make_multiplier(mult_factor):
    """Return a lambda that multiplies its argument by mult_factor."""
    return lambda x: mult_factor * x

def make_adder(summand):
    """Return a lambda that adds summand to its argument."""
    return lambda x: x + summand

def compose(f, g):
    """Given two functions as arguments, return the composition of those functions."""
    return lambda x: f(g(x))
 
def composed_c2f(x):
    """Convert Celcius to Fahrenheit."""
    m = make_multiplier(9/5)
    b = make_adder(32)
    result = compose(m, b)(x)
    return result

def verbose_c2f(celcius):
    fahrenheit = composed_c2f(celcius)
    print('Celcius={0:.2f} => Fahrenheit={1:.2f}'.format(celcius, fahrenheit))
    return fahrenheit

if __name__ == '__main__':
    multiply_by_five = make_multiplier(5)
    add_five = make_adder(5)
    assert(multiply_by_five(7) == 35)
    assert(add_five(7) == 12)
    assert(compose(add_five, multiply_by_five)(7) == 40)

    # Assert the temperature equivalencies from problem 6 in HW #7.
    assert(verbose_c2f(-40) == -40)
    assert(verbose_c2f(0) == 32)
    assert(verbose_c2f(100) == 212)
