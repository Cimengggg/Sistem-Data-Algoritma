from myqueue import Queue

# Studi kasus: antrian layanan
antrian = Queue()

antrian.enqueue("Budi")
antrian.enqueue("Siti")
antrian.enqueue("Andi")
antrian.display()

print("Dilayani:", antrian.dequeue())   # Budi
print("Dilayani:", antrian.dequeue())   # Siti
antrian.display()

print("Antrian terdepan:", antrian.peek())  # Andi
print("Jumlah antrian:", antrian.size)
