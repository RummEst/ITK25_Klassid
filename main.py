from classes.Ring import Ring
from classes.Risttahukas import Risttahukas


def kysi_murdarv(kysimus: str) -> float:
    """Küsib kasutajalt murdarvu turvaliselt"""
    while True:
        try:
            v = float(input(kysimus))
            if v <= 0:
                print("Palun sisesta POSITIIVNE arv!")
                continue
            return v
        except ValueError:
            print("Vigane sisend! Palun sisesta number (nt 5.7 või 12)")


def main():
    print("=== Geomeetriliste kujundite arvutaja ===\n")

    # RING
    print("1. RING")
    r = kysi_murdarv("Ringi raadius (cm): ")
    ring = Ring(r)

    print("\n" + "═" * 60)
    print(f"Sisestatud: {ring}")
    print("-" * 60)
    print(f"Ümbermõõt:      {ring.umbermood():10.2f} cm")
    print(f"Pindala:        {ring.pindala():10.2f} cm²")
    print(f"Diameeter:      {ring.diameeter():10.2f} cm")

    # RISTTAHUKAS
    print("\n" + "═" * 60)
    print("\n2. RISTTAHUKAS")
    a = kysi_murdarv("Pikkus (cm):   ")
    b = kysi_murdarv("Laius  (cm):   ")
    c = kysi_murdarv("Kõrgus (cm):   ")

    tahukas = Risttahukas(a, b, c)

    print("\n" + "═" * 60)
    print(f"Sisestatud: {tahukas}")
    print("-" * 60)
    print(f"Ruumala:        {tahukas.ruumala():10.2f} cm³")
    print(f"Täispindala:    {tahukas.pindala():10.2f} cm²")
    print(f"Ruumdiagonaal:  {tahukas.ruumdiagonaal():10.2f} cm")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgramm katkestatud.")
    except Exception as e:
        print(f"\nViga: {e}")
    finally:
        print("\n=== Aitäh kasutamast! ===\n")