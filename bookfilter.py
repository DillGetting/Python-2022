'''
   Header looking through books
   argparse is a better tool for parsing but not here
'''
import csv
import Book
import sys


def main():
    ''' arg 1 is book file
    '''
    bookcsv = sys.argv[1]
    title_search = sys.argv[2]

    booklist = Book.BookList(bookcsv)
    found = booklist.title_search(title_search)
    for b in booklist.booklist:
        print(b.show())

    for l in lines:
        print(l.show)



    # with open(bookcsv, encoding="utf_8") as fd:
    #     lines = fd.readlines()

    # with open(bookcsv, encoding="UTF_8") as fd:
    #     reader = csv.DictReader(fd)
    #     for row in reader:
    #         booklist.append(Book.Book(row["ID"], row["title"], row["author"], row["rating"], row["voters"], row["price"],
    #                                   row["currency"], row["description"], row["publisher"], row["page_count"],
    #                                   row["generes"], row["ISBN"], row["language"], row["published_date"]))


        # for b in booklist:
        #     print(b.show())
    #         print("id: {} title: {}".format(b.ID, b.title))
    # print(booklist)



    # for line in lines:
    #     print(line)


if __name__ == "__main__":
    main()
