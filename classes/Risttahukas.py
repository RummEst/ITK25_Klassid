from math import sqrt


class Risttahukas:
    """Risttahuka (ristkülikukujulise paralleeltahuka) klass"""

    def __init__(self, pikkus: float, laius: float, korgus: float):
        if pikkus <= 0 or laius <= 0 or korgus <= 0:
            raise ValueError("Kõik mõõtmed peavad olema positiivsed!")
        self.a = pikkus
        self.b = laius
        self.c = korgus

    def ruumala(self) -> float:
        return self.a * self.b * self.c

    def pindala(self) -> float:
        # 2(ab + ac + bc)
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)

    def ruumdiagonaal(self) -> float:
        return sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2)

    def __str__(self):
        return f"Risttahukas ({self.a:.1f} × {self.b:.1f} × {self.c:.1f} cm)"