"""
Program utama: Simulasi antrean makan restoran.
Memakai library AntreanStatis dari antrean_statis.py.
"""

from library_queue import AntreanStatis

MAKS_ORANG_PER_GRUP = 10
MENIT_PER_GRUP = 30  # perkiraan lama makan satu grup


def minta_angka(pesan, default=None, minimal=1, maksimal=None):
    """Meminta input angka dari pengguna sampai valid."""
    while True:
        teks = input(pesan).strip()
        if teks == "" and default is not None:
            return default
        try:
            nilai = int(teks)
        except ValueError:
            print("  [!] Input harus berupa angka.")
            continue
        if nilai < minimal or (maksimal is not None and nilai > maksimal):
            batas = f"{minimal}-{maksimal}" if maksimal else f"minimal {minimal}"
            print(f"  [!] Angka harus {batas}.")
            continue
        return nilai


def format_grup(grup):
    kode, nama, jumlah = grup
    return f"{kode} | {nama} ({jumlah} orang)"


def tampil_antrean(antrean, kapasitas):
    """Menampilkan seluruh slot antrean (kapasitas tetap): terisi maupun kosong."""
    isi = antrean.to_list()
    print(f"\n  ANTREAN SAAT INI ({len(isi)}/{kapasitas} slot terisi)")
    print("  " + "-" * 50)
    for i in range(kapasitas):
        if i < len(isi):
            label = "  [FRONT]" if i == 0 else ("  [REAR]" if i == len(isi) - 1 else "")
            print(f"  Slot {i + 1:>2} : {format_grup(isi[i])}{label}")
        else:
            print(f"  Slot {i + 1:>2} : (kosong)")
    print("  " + "-" * 50)


def tampilkan_menu():
    print("\n==================== MENU ====================")
    print("  1. Daftar antrean            (ENQUEUE)")
    print("  2. Panggil grup ke meja      (DEQUEUE)")
    print("  3. Lihat antrean terdepan    (PEEK)")
    print("  4. Lihat seluruh antrean")
    print("  5. Cek status antrean        (isEmpty / isFull / size)")
    print("  0. Keluar")
    print("==============================================")


def main():
    print("=" * 46)
    print("   ANTREAN MAKAN RESTORAN - SIMULASI QUEUE")
    print("=" * 46)
    kapasitas = minta_angka("Kapasitas ruang tunggu (Enter = 5 grup): ", default=5, minimal=1, maksimal=20)

    antrean = AntreanStatis(kapasitas)
    nomor_terakhir = 0
    total_dilayani = 0

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":  # ENQUEUE
            if antrean.is_full():
                print("\n  [OVERFLOW] Ruang tunggu penuh! Tamu baru belum bisa mendaftar.")
                print("             Silakan tunggu sampai ada grup yang dipanggil.")
                continue
            nama = input("  Nama pemesan       : ").strip()
            if not nama:
                print("  [!] Nama tidak boleh kosong.")
                continue
            jumlah = minta_angka(f"  Jumlah orang (1-{MAKS_ORANG_PER_GRUP}): ",
                                 minimal=1, maksimal=MAKS_ORANG_PER_GRUP)

            kode = f"R-{nomor_terakhir + 1:03d}"
            try:
                antrean.enqueue((kode, nama, jumlah))
                nomor_terakhir += 1  # nomor hanya naik jika berhasil masuk antrean
                posisi = antrean.size()
                print(f"\n  [ENQUEUE] Berhasil! Nomor antrean {kode} atas nama {nama} ({jumlah} orang).")
                print(f"            Posisi antrean ke-{posisi}, estimasi tunggu +/- {(posisi - 1) * MENIT_PER_GRUP} menit.")
            except OverflowError:
                print("\n  [OVERFLOW] Ruang tunggu penuh! Pendaftaran ditolak.")

        elif pilihan == "2":  # DEQUEUE
            try:
                grup = antrean.dequeue()
                total_dilayani += 1
                print(f"\n  [DEQUEUE] Panggilan: {format_grup(grup)}")
                print("            Silakan menuju meja Anda. Selamat menikmati hidangan!")
                if not antrean.is_empty():
                    print(f"            Berikutnya: {format_grup(antrean.peek())}")
                else:
                    print("            Tidak ada lagi tamu yang menunggu.")
            except IndexError:
                print("\n  [UNDERFLOW] Antrean kosong, tidak ada grup yang bisa dipanggil.")

        elif pilihan == "3":  # PEEK
            if antrean.is_empty():
                print("\n  [PEEK] Antrean kosong.")
            else:
                print(f"\n  [PEEK] Grup terdepan (akan dipanggil berikutnya): {format_grup(antrean.peek())}")

        elif pilihan == "4":
            tampil_antrean(antrean, kapasitas)

        elif pilihan == "5":
            print("\n  STATUS ANTREAN")
            print(f"    size()          : {antrean.size()} grup")
            print(f"    isEmpty()       : {antrean.is_empty()}")
            print(f"    isFull()        : {antrean.is_full()}")
            print(f"    Sisa slot       : {kapasitas - antrean.size()} dari {kapasitas}")
            print(f"    Total dipanggil : {total_dilayani} grup")

        elif pilihan == "0":
            sisa = antrean.size()
            print(f"\n  Terima kasih! Total grup dipanggil: {total_dilayani}, masih menunggu: {sisa}.")
            break

        else:
            print("\n  [!] Menu tidak dikenal, pilih 0-5.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  Program dihentikan.")