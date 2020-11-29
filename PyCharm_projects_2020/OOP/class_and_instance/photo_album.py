class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]
        self.current_slot = [0, 0]
        self.free = True

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        if self.free:
            page = self.current_slot[0]
            slot = self.current_slot[1]
            self.photos[page].append(label)
            prt_text = f"{label} photo added successfully on page {page + 1} slot {slot + 1}"
            slot += 1
            if slot == 4 and page <= self.pages - 1:
                slot = 0
                page += 1
                if page == self.pages:
                    self.free = False
            self.current_slot = [page, slot]
            return prt_text
        else:
            return "No more free spots"

    def display(self):
        prt_text = ""
        for p in range(self.pages):
            prt_text += f"{'-' * 11}\n"
            if len(self.photos[p]) != 0:
                prt_text += f"{' '.join( '[]' for _ in range(len(self.photos[p])))}"
                # for _ in range(len(self.photos[p])):
                #     prt_text += f"[] "
            prt_text += f"\n"
        prt_text += f"{'-' * 11}\n"
        return prt_text


album = PhotoAlbum(3)

for i in range(1, 10):
    print(album.add_photo(f'Me at age of {str(i)}'))
print(album.photos)


print(album.__dict__)

print(album.display())
second_album = PhotoAlbum.from_photos_count(10)
print(second_album.__dict__)
print(second_album.display())