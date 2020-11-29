class Song:
    def __init__(self, title, performer, album, author, duration):
        self.title = title
        self.performer = performer
        self.album = album
        self.author = author
        self.duration = duration

    def get_info(self):
        return f'Title: {self.title}' \
               f'\nPerformer: {self.performer}' \
               f'\nAlbum: {self.album}' \
               f'\nWritten by: {self.author}' \
               f'\nlasts: {self.duration} minutes' \
               f'\n============================='

    def __repr__(self):
        return f'{self.title}: {self.performer}: {self.album}: {self.author}: {self.duration}'


favorite_piece = Song("Ticket to the Moon", "ELO", "Time", "Jeff Lynn", 3.49)

print(favorite_piece.get_info())
print(favorite_piece)