"""
Library: Queue statis tanpa library bawaan.
Implementasi array melingkar (circular array) dengan kapasitas tetap.
"""


class AntreanStatis:
    """Queue FIFO berkapasitas tetap menggunakan array melingkar."""

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._data = [None] * maxsize   
        self._front = 0                
        self._count = 0                 

    def enqueue(self, x):
        """Menambah elemen di belakang. Gagal (OverflowError) jika penuh."""
        if self.is_full():
            raise OverflowError("Antrean penuh")
        indeks_belakang = (self._front + self._count) % self.maxsize
        self._data[indeks_belakang] = x
        self._count += 1

    def dequeue(self):
        """Mengeluarkan elemen terdepan. Gagal (IndexError) jika kosong."""
        if self.is_empty():
            raise IndexError("Antrean kosong")
        x = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self.maxsize
        self._count -= 1
        return x

    def peek(self):
        """Melihat elemen terdepan tanpa mengeluarkannya."""
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data[self._front]

    def is_empty(self):
        return self._count == 0

    def is_full(self):
        return self._count == self.maxsize

    def size(self):
        return self._count

    def item_at(self, i):
        """Mengambil elemen ke-i dari depan (0 = front)."""
        return self._data[(self._front + i) % self.maxsize]

    def to_list(self):
        """Seluruh isi antrean dari depan ke belakang."""
        return [self.item_at(i) for i in range(self._count)]