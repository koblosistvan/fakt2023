class Auto:
    def __init__(self, sebesseg_hatar):
        self.sebesseg = 0
        self.sebesseg_hatar = sebesseg_hatar

    def gyorsit(self, gyorsulas):
        if self.sebesseg + gyorsulas <= self.sebesseg_hatar:
            self.sebesseg += gyorsulas
        else:
            print("Gyorsítás nem lehetséges, elérve a sebességhatárt.")

    def lassit(self, gyorsulas):
        if self.sebesseg - gyorsulas >= 0:
            self.sebesseg -= gyorsulas
        else:
            print("Lassítás nem lehetséges, már megálltál.")

    def gyorshajt(self, szabalyos_sebesseg):
        if self.sebesseg > szabalyos_sebesseg:
            print(f"Gyorshajtás! A megengedett sebesség {szabalyos_sebesseg}, a jelenlegi sebesség {self.sebesseg}.")

def main():
    sebesseg_hatar = 120  #km/h-ban
    auto = Auto(sebesseg_hatar)

    while True:
        print(f"A jelenlegi sebesség: {auto.sebesseg} km/h")
        valasztas = input("Válassz egy lehetőséget (gyorsítás/gyorshajtás/lassítás/kilépés): ").lower()

        if valasztas == "kilépés":
            break
        elif valasztas == "gyorsítás":
            auto.gyorsit(10)  # gyorsulás
        elif valasztas == "lassítás":
            auto.lassit(10)  # gyorsulás
        elif valasztas == "gyorshajtás":
            auto.gyorshajt(sebesseg_hatar)  # másik szabályos sebesség
        else:
            print("Érvénytelen választás. Próbáld újra.")

if __name__ == "__main__":
    main()
