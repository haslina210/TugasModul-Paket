import Paket.Class as C

def main():
#class Tanah
    p = float (input("Panjang \t: "))
    l = float (input("Lebar\t\t: "))

    obj = C.Tanah (p,l)
    luas = obj.LuasTanah()
    kel = obj.KelilingTanah()
    print("-------------------------------------")
    print("Panjang Tanah\t: ",p," m")
    print("Lebar Tanah\t: ",l," m")
    print("-------------------------------------")
    print("MENGHITUNG LUAS & KELILING TANAH ANDA")
    print("-------------------------------------")
    print("Luas Tanah Anda\t\t: ",luas)
    print("Keliling Tanah Anda\t: ",kel)
    print("=====================================")

#class Sumur
    print("-------------------------------------")
    r = float (input("Jari-jari\t: "))
    t = float (input("Tinggi\t\t: "))
    phi = 3.14
    s = C.Sumur(phi,r,t)
    vol = s.VolumeSumur()

    print("-------------------------------------")
    print("Jari-jari Sumur\t: ",r," m")
    print("Tinggi Sumur\t: ",t," m")
    print("-------------------------------------")
    print("MENGHITUNG VOLUME SUMUR ANDA")
    print("-------------------------------------")
    print("Volume Sumur Anda\t: ",vol)
    print("=====================================")

#class AlatTulis
    b = 3000
    p = 1500

    print("\n-------------------------------------")
    print("Daftar Harga Barang")
    print("-------------------------------------")
    print("Buku tulis\t: Rp.",b)
    print("Pulpen\t\t: Rp.",p)
    print("-------------------------------------")
    print("Barang Yang Di Beli")
    print("-------------------------------------")

    jb = float (input("Jumlah Buku\t: "))
    jp = float (input("Jumlah Pulpen\t: "))
    at = C.AlatTulis(jb, jp, b, p)
    TB = at.TotalBarang()
    JHB = at.JumlahHargaBarang()

    print("-------------------------------------")
    print("MENGHITUNG BELANJAAN ANDA")
    print("-------------------------------------")
    print("Total Barang\t: ",TB)
    print("Total Harga\t: Rp.",JHB)
    print("=====================================")

if __name__ == "__main__":
    main()

