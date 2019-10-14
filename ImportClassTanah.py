from Paket.Class import Tanah as t

def main():
    p = float (input("Panjang \t: "))
    l = float (input("Lebar\t\t: "))
    obj = t (p,l)
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
    
if __name__ == "__main__":
    main()

