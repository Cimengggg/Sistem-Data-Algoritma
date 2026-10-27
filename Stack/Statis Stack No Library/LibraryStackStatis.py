# Library Stack Statis Menggunakan List Python

class StackBukuStatis:
    def __init__(self, kapasitas=5):
        # Menggunakan list kosong, namun dibatasi oleh variabel kapasitas
        self.data = []
        self.kapasitas = kapasitas

    def kosong(self):
        return len(self.data) == 0

    def penuh(self):
        # Fungsi baru untuk mengecek apakah list sudah mencapai batas maksimal
        return len(self.data) == self.kapasitas

    def tambah_buku(self, nama_buku):
        if self.penuh():
            print("Tumpukan buku penuh! Tidak dapat menambahkan buku baru.")
        else:
            # append() menambahkan data ke ujung, dilindungi oleh cek kapasitas
            self.data.append(nama_buku)
            print("Buku berhasil ditambahkan.")

    def ambil_buku(self):
        if self.kosong():
            print("Tumpukan buku kosong!")
        else:
            # pop() mengambil dan menghapus elemen terakhir dari list
            buku = self.data.pop()
            print("Buku yang diambil:", buku)

    def tampilkan_buku(self):
        if self.kosong():
            print("Tumpukan buku kosong!")
        else:
            print("Tumpukan buku dari atas:")
            # Menampilkan dari indeks terakhir (puncak) ke indeks pertama (dasar)
            for i in range(len(self.data) - 1, -1, -1):
                print("-", self.data[i])