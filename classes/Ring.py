from math import pi


class Ring:
    """Lihtne ringi klass"""

    def __init__(self, raadius: float):
        if raadius <= 0:
            raise ValueError("Raadius peab olema positiivne!")
        self.r = raadius

    def umbermood(self) -> float:
        return 2 * pi * self.r

    def pindala(self) -> float:
        return pi * self.r ** 2

    def diameeter(self) -> float:
        return 2 * self.r

    def __str__(self):
        return f"Ring (r = {self.r:.2f} cm)"