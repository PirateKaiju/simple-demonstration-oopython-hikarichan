from calc_module.calc import Calc
from presentation.easy_breezy_presentator import EasyBreezyPresentator

if __name__ == "__main__":
    calc = Calc()
    presentator = EasyBreezyPresentator()

    # Simulate some functionality here. This could be easily called from another place
    # We're calling it from main just for simplicity

    presentator.simple_print(calc.sum(7, 7))

