# Library Stack Statis Buatan Sendiri

class StackBuku:
    KAPASITAS = 5

    def __init__(self):
        self.data = [None] * self.KAPASITAS
        self.puncak = -1

    def kosong(self):
        return self.puncak == -1

    def penuh(self):
        return self.puncak == self.KAPASITAS - 1

    def tambah_buku(self, nama_buku):
        if self.penuh():
            print("Tumpukan buku penuh!")
        else:
            self.puncak += 1
            self.data[self.puncak] = nama_buku
            print("Buku berhasil ditambahkan.")

    def ambil_buku(self):
        if self.kosong():
            print("Tumpukan buku kosong!")
        else:
            buku = self.data[self.puncak]
            self.data[self.puncak] = None
            self.puncak -= 1
            print("Buku yang diambil:", buku)

    def tampilkan_buku(self):
        if self.kosong():
            print("Tumpukan buku kosong!")
        else:
            print("Tumpukan buku dari atas:")
            for i in range(self.puncak, -1, -1):
                print("-", self.data[i])
