# many_to_many.py

class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        """Returns a list of contracts for this author."""
        return self._contracts

    def books(self):
        """Returns a list of unique books associated with this author."""
        return list(set(contract.book for contract in self._contracts))

    def sign_contract(self, book, date, royalties):
        """Creates a new contract for the author and the specified book."""
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        """Calculates the total royalties from all contracts."""
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        """Returns a list of contracts for this book."""
        return self._contracts

    def authors(self):
        """Returns a list of unique authors associated with this book."""
        return list(set(contract.author for contract in self._contracts))

    def add_contract(self, contract):
        """Adds a contract to this book."""
        self._contracts.append(contract)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author type. Must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Invalid book type. Must be an instance of Book.")
        if not isinstance(date, str):
            raise Exception("Invalid date type. Must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties type. Must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add contract to the author and book
        self.author.contracts().append(self)
        self.book.add_contract(self)

        # Store the contract in the global list of contracts
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns a list of contracts sorted by date."""
        return sorted([contract for contract in cls.all if contract.date == date], key=lambda c: c.date)

# Example usage:
# author = Author("John Doe")
# book = Book("Python Programming")
# contract = author.sign_contract(book, "01/01/2024", 10000)
