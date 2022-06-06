
def burc_bul(tarih: str) -> str:

    ay: int = int(tarih.split("/")[0])
    gun: int = int(tarih.split("/")[1])

    if (ay == 3 and gun >= 21) or (ay == 4 and gun <= 20):
        return "Koç Burcu"
    elif (ay == 9 and gun >= 22) or (ay == 10 and gun <= 23):
        return "Terazi"
    else:
        return "Bulunamadı"


if __name__ == '__main__':
    print("Program Başladı")

    tarih: str = input("Doğum tarihinizi girin: (ay/gün şeklinde girin)")

    burc = burc_bul(tarih)
    print("Girdiğiniz tarihe göre burcunuz ", burc)
