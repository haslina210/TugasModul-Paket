from Paket.Class import AlatTulis as AT

def main():
    b = 3000
    p = 1500

    print("-------------------------------------")
    print("Daftar Harga Barang")
    print("-------------------------------------")
    print("Buku tulis\t: Rp.",b)
    print("Pulpen\t\t: Rp.",p)
    print("-------------------------------------")
    print("Barang Yang Di Beli")
    print("-------------------------------------")

    jb = float (input("Jumlah Buku\t: "))
    jp = float (input("Jumlah Pulpen\t: "))
    at = AT(jb, jp, b, p)
    TB = at.TotalBarang()
    JHB = at.JumlahHargaBarang()

    print("-------------------------------------")
    print("MENGHITUNG BELANJAAN ANDA")
    print("-------------------------------------")
    print("Total Barang\t: ",TB)
    print("Total Harga\t: Rp.",JHB)
    
if __name__ == "__main__":
    main()
