from Paket.Class import Sumur

def main():
    r = float (input("Jari-jari\t: "))
    t = float (input("Tinggi\t\t: "))
    phi = 3.14
    s = Sumur(phi,r,t)
    vol = s.VolumeSumur()

    print("-------------------------------------")
    print("Jari-jari Sumur\t: ",r," m")
    print("Tinggi Sumur\t: ",t," m")
    print("-------------------------------------")
    print("MENGHITUNG VOLUME SUMUR ANDA")
    print("-------------------------------------")
    print("Volume Sumur Andda\t: ",vol)
    
if __name__ == "__main__":
    main()
