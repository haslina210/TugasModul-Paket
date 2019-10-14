import math

class Tanah(object):
    def __init__( self, p, l):
        self.panjang = p
        self.lebar = l

    def LuasTanah(self):
        return self.panjang * self.lebar

    def KelilingTanah(self):
        return 2* (self.panjang + self.lebar)

class Sumur(object):
    def __init__(self, phi, r, t):
        self.phi = phi
        self.r = r
        self.t = t

    def VolumeSumur(self):
        return self.phi * self.r **2 *self.t

class AlatTulis(object):
    def __init__(self, jb, jp, b, p):
        self.jumlahBuku = jb
        self.jumlahPulpen = jp
        self.buku = b
        self.pulpen = p
    
    def TotalBarang(self):
        return self.jumlahBuku + self.jumlahPulpen
        
    def JumlahHargaBarang (self):
        return (self.jumlahBuku * self.buku) + (self.jumlahPulpen * self.pulpen)
        
    
    
