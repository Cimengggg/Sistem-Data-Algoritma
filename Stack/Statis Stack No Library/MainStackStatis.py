from LibraryStackStatis import StackBukuStatis

# Menginisialisasi stack statis dengan batas maksimal 5 buku
stack = StackBukuStatis(kapasitas=5)

# Menambahkan dua buku awal
stack.tambah_buku("Algoritma")
stack.tambah_buku("Basis Data")

while True:
    print("\n=== TUMPUKAN BUKU PERPUSTAKAAN (STATIS) ===")
    print("1. Tambah buku")
    print("2. Ambil buku")
    print("3. Tampilkan tumpukan buku")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama buku: ")
        stack.tambah_buku(nama)

    elif pilihan == "2":
        stack.ambil_buku()

    elif pilihan == "3":
        stack.tampilkan_buku()

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")