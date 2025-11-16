# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------

def older_book(book1: Book, book2: Book):
    book1_year = book1.year
    book2_year = book2.year

    if book1_year < book2_year:
        print(f"{book1.name} is older, it was published in {book1.year}")
    elif book2_year < book1_year:
        print(f"{book2.name} is older, it was published in {book2.year}")
    elif book1_year == book2_year:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)



# class Book:
#     def __init__(self, name: str, author: str, genre: str, year: int):
#         self.name = name
#         self.author = author
#         self.genre = genre 
#         self.year = year
 
# def older_book(book1: Book, book2: Book):
#     same = True
#     if book1.year < book2.year:
#         older = book1
#         same = False
#     elif book1.year > book2.year:
#         older = book2
#         same = False
 
#     if same:
#         print(f"{book1.name} and {book2.name} were published in {book1.year}")
#     else:
#         print(f"{older.name} is older, it was published in {older.year}")