class Publication:
    def __init__(self, title, author):
        self.__title = (str(title))
        self.__author = (str(author))

    def set_title(self, title):
        self.__title = (str(title))

    def set_author(self, author):
        self.__author = (str(author))

    def get_title(self):
        print(f"Title: {self.__title}")

    def get_author(self):
        print(f"Author: {self.__author}")

    def display_info(self):
        self.get_title()
        self.get_author()

class Book(Publication):
    def __init__(self, number_of_pages, title, author):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

    def get_number_of_pages(self):
        print(f"Number of Pages: {self.__number_of_pages}")

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("invalid number of pages")
class Magazine(Publication):
    def __init__(self, issue_number, title, author):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        print(f"Issue Number: {self.__issue_number}")

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("invalid issue number")

pub1 = Publication("Journal of Experimental Psychology", 1)
book1 = Book(310, "The Hobbit", "J.R.R. Tolkien")
mag1 = Magazine(202, "National Geographic", "Various Authors")


print("Publication information")
pub1.display_info()

print("\nBook Information")
book1.set_number_of_pages(209) #invalid output
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information")
mag1.display_info()
mag1.set_issue_number(0)
print(mag1.get_issue_number())