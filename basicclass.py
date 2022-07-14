from numpy import true_divide


class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return self.name + ' by ' + self.author

    def __eq__(self, obj):
        if ((self.name == obj.name) * (self.author == obj.title)):
            return True
        else:
            return False

class Library:

    def __init__(self):
        self.library = []

    def __len__(self):
        return len(self.library)

    def add_book(self, name, author):
        self.library.append(Book(name, author))

    def __getitem__(self, key):
        return self.library[key]

    def by_author(self, author):
        matches = []
        for book in self.library:
            if book.author == author:
                matches.append(book)

        if not matches:
            raise KeyError('Author does not exist')

        return matches

    @property
    def titles(self):
        titles = []
        for book in self.library:
            titles.append(book.name)
        return titles

    @property
    def authors(self):
        authors = []
        for book in self.library:
            if book.author in authors:
                pass
            else:
                authors.append(book.author)
        return authors

    def union(self, other_lib):
        library = []
        for book in self.library:
            if not Book().__eq__(other_lib):
                library.append(book)

        return Library(library)

#------------------
library = Library()

library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')

print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')
for book in books:
    print(book)

#books = library.by_author('Carol')

print(library.titles)
print(library.authors)