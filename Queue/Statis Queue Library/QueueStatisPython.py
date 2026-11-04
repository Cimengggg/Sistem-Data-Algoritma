"""
Studi Kasus Queue (Antrean) - Antrean Makan di Restoran (INTERAKTIF)
Struktur Data & Algoritma

Implementasi STATIS: kapasitas ruang tunggu ditentukan di awal (maxsize) dan tidak bisa bertambah.
Library: queue.Queue bawaan Python (tanpa membuat class/library sendiri).

Pemetaan operasi Queue -> fungsi bawaan:
    enqueue(x)  -> put_nowait(x)     (gagal = queue.Full  -> OVERFLOW)
    dequeue()   -> get_nowait()      (gagal = queue.Empty -> UNDERFLOW)
    peek()      -> queue[0]          (lihat elemen terdepan tanpa mengeluarkan)
    isEmpty()   -> empty()
    isFull()    -> full()
    size()      -> qsize()

Skenario: tamu yang datang saat meja penuh mendaftar ke antrean (enqueue) di meja pendaftaran,
pelayan memanggil grup terdepan saat ada meja kosong (dequeue). Prinsip FIFO: siapa datang
lebih dulu, dipanggil lebih dulu.
"""

from queue import Queue, Full, Empty

MAKS_ORANG_PER_GRUP = 10
MENIT_PER_GRUP = 30  # perkiraan lama makan satu grup (untuk estimasi waktu tunggu)


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
    isi = list(antrean.queue)
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

    antrean = Queue(maxsize=kapasitas)  # ukuran tetap -> implementasi statis
    nomor_terakhir = 0
    total_dilayani = 0

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":  # ENQUEUE
            if antrean.full():
                print("\n  [OVERFLOW] Ruang tunggu penuh! Tamu baru belum bisa mendaftar.")
                print("             Silakan tunggu sampai ada grup yang dipanggil.")
                continue
            nama = input("  Nama pemesan       : ").strip()
            if not nama:
                print("  [!] Nama tidak boleh kosong.")
                continue
            jumlah = minta_angka(f"  Jumlah orang (1-{MAKS_ORANG_PER_GRUP}): ", minimal=1, maksimal=MAKS_ORANG_PER_GRUP)

            kode = f"R-{nomor_terakhir + 1:03d}"
            try:
                antrean.put_nowait((kode, nama, jumlah))
                nomor_terakhir += 1  # nomor hanya naik jika berhasil masuk antrean
                posisi = antrean.qsize()
                print(f"\n  [ENQUEUE] Berhasil! Nomor antrean {kode} atas nama {nama} ({jumlah} orang).")
                print(f"            Posisi antrean ke-{posisi}, estimasi tunggu +/- {(posisi - 1) * MENIT_PER_GRUP} menit.")
            except Full:  # OVERFLOW
                print("\n  [OVERFLOW] Ruang tunggu penuh! Pendaftaran ditolak.")

        elif pilihan == "2":  # DEQUEUE
            try:
                grup = antrean.get_nowait()
                total_dilayani += 1
                print(f"\n  [DEQUEUE] Panggilan: {format_grup(grup)}")
                print("            Silakan menuju meja Anda. Selamat menikmati hidangan!")
                if not antrean.empty():
                    print(f"            Berikutnya: {format_grup(antrean.queue[0])}")
                else:
                    print("            Tidak ada lagi tamu yang menunggu.")
            except Empty:  # UNDERFLOW
                print("\n  [UNDERFLOW] Antrean kosong, tidak ada grup yang bisa dipanggil.")

        elif pilihan == "3":  # PEEK
            if antrean.empty():
                print("\n  [PEEK] Antrean kosong.")
            else:
                print(f"\n  [PEEK] Grup terdepan (akan dipanggil berikutnya): {format_grup(antrean.queue[0])}")

        elif pilihan == "4":
            tampil_antrean(antrean, kapasitas)

        elif pilihan == "5":
            print("\n  STATUS ANTREAN")
            print(f"    size()          : {antrean.qsize()} grup")
            print(f"    isEmpty()       : {antrean.empty()}")
            print(f"    isFull()        : {antrean.full()}")
            print(f"    Sisa slot       : {kapasitas - antrean.qsize()} dari {kapasitas}")
            print(f"    Total dipanggil : {total_dilayani} grup")

        elif pilihan == "0":
            sisa = antrean.qsize()
            print(f"\n  Terima kasih! Total grup dipanggil: {total_dilayani}, masih menunggu: {sisa}.")
            break

        else:
            print("\n  [!] Menu tidak dikenal, pilih 0-5.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  Program dihentikan.")