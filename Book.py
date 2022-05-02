'''
Header for file
'''
import csv


class Book:
    '''
    for google books csv
    self is the attribute of the book init method
    self.id is the attribute for the function
    self.id could be self.i as long as it matches the arguments of the function init
    '''
    def __init__(self, ID, title, author, rating, voters, price, currency,
                 description, publisher, page_count, generes, ISBN, language, published_date):
        self.ID = ID
        self.title = title
        self.author = author
        self.rating = rating
        self.voters = voters
        self.price = price
        self.currency = currency
        self.description = description
        self.publisher = publisher
        self.page_count = page_count
        self.generes = generes
        self.ISBN = ISBN
        self.language = language
        self.published_date = published_date
        '''
        behavior functions will go here, like in the shape class a behavior was area and that could
        be applied to any shape like square
        '''
    def brief(self):
        # brief = "Author(s): {}\n Title: {}\n publisher: {}\n published_date: {}".format(self.author, self.title,
        #                                                                           self.publisher, self.published_date)
        brief = "{:<15} {:>20}\n".format("Author(s)", self.author)
        brief = "{:<15} {:>20}\n".format("title", self.title)
        brief = "{:<15} {:>20}\n".format("publisher", self.publisher)
        brief = "{:<15} {:>20}\n".format("published_date", self.published_date)
        # brief += "-" * 78

        return brief

    def show(self):
        show = self.brief()
        show += "{:<15} {:>20}\n".format("ID", self.ID)
        show += "{:<15} {:>20}\n".format("Rating", self.rating)
        show += "{:<15} {:>20}\n".format("Voters", self.voters)
        show += "{:<15} {:>20}\n".format("Price", self.price)
        show += "{:<15} {:>20}\n".format("Currency", self.currency)
        show += "{:<15} {:>20}\n".format("Page count", self.page_count)
        show += "{:<15} {:>20}\n".format("Generes", self.generes)
        show += "{:<15} {:>20}\n".format("ISBN", self.ISBN)
        show += "{:<15} {:>20}\n".format("Language", self.language)
        show += "{:<15} {:>20}\n".format("Description", self.description)
        show += "-" * 50
        show += "\n"
        return show


class BookList:

    def __init__(self, bookcsv):
        self.bookcsv = csv
        self.booklist = []
        with open(bookcsv, encoding="UTF_8") as fd:
            reader = csv.DictReader(fd)
            for row in reader:
                self.booklist.append(Book(row["ID"], row["title"], row["author"], row["rating"], row["voters"], row["price"],
                                          row["currency"], row["description"], row["publisher"], row["page_count"],
                                          row["generes"], row["ISBN"], row["language"], row["published_date"]))

    def title_search(self, search_string, categories=None):
        found_books = []
        for b in self.booklist:
            if search_string in b.title:
                found_books.append(b)
            return found_books

    def append_book(self, book):
        pass

    def append_list(self, csv):
        pass


def test1():
    ID = "1"
    title = "ted"
    author = "ted"
    rating = "5.0"
    voters = "10000"
    price = "100.0"
    currency = "USD"
    description = "good"
    publisher = "frankly"
    page_count = "150"
    generes = "horror"
    ISBN = "9758225156"
    language = "English"
    published_date = "4/12/2022"
    my_book = Book(ID, title, author, rating, voters, price, currency, description, publisher,
                   page_count, generes, ISBN, language, published_date)
    assert(my_book.ID == ID)
    assert(my_book.title == title)
    assert(my_book.author == author)
    assert(my_book.rating == rating)
    assert(my_book.voters == voters)
    assert(my_book.price == price)
    assert(my_book.currency == currency)
    assert(my_book.description == description)
    assert(my_book.publisher == publisher)
    assert(my_book.page_count == page_count)
    assert(my_book.generes == generes)
    assert(my_book.ISBN == ISBN)
    assert(my_book.language == language)
    assert(my_book.published_date == published_date)
    print("all test1 passed")


if __name__ == "__main__":
    test1()
