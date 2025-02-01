
class Book:
    def __init__(self, title, isPaperback):
        self.title = title
        self.is_paperback = isPaperback

        if isPaperback:
            self.price = 9.99
        else:
            self.price = 19.99

        
    