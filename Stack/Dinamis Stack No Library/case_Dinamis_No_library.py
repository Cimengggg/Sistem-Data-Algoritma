from dinamis_Stack_No_Library import Stack

class History:
    def __init__(self):
        self.retr = Stack()
        self.now = "Home"

    def open(self, page):
        self.retr.push(self.now)
        self.now = page

    def back(self):
        if self.retr.is_empty():
            print("No Page")
            return
        self.now = self.retr.pop()

if __name__ == "__main__":
    h = History()
    h.open("google.com")
    h.open("youtube.com")
    h.open("wikipedia.com")
    print(h.retr.tampil())

    h.open("uinjkt.ac.id")
    print(h.now)
    print(h.retr.tampil())

    h.back()
    print(h.now)
    
    h.back()
    print(h.now)
    print(h.retr.tampil())