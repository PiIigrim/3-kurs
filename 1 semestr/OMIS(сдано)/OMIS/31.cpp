#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    wstring title;
    wstring author;

public:
    Book() {
        title = L"";
        author = L"";
    }

    Book(wstring _title, wstring _author) {
        title = _title;
        author = _author;
    }

    wstring getTitle() const {
        return title;
    }

    void setTitle(wstring _title) {
        title = _title;
    }

    wstring getAuthor() const {
        return author;
    }

    void setAuthor(wstring _author) {
        author = _author;
    }
};

class Librarian {
private:
    wstring name;
    wstring department;

public:
    Librarian() {
        name = L"";
        department = L"";
    }

    Librarian(wstring _name, wstring _department) {
        name = _name;
        department = _department;
    }

    wstring getName() const {
        return name;
    }

    void setName(wstring _name) {
        name = _name;
    }

    wstring getDepartment() const {
        return department;
    }

    void setDepartment(wstring _department) {
        department = _department;
    }
};

class LibrarySection {
private:
    wstring name;
    Librarian* librarian;

public:
    LibrarySection() {
        name = L"";
        librarian = nullptr;
    }

    LibrarySection(wstring _name, Librarian* _librarian) {
        name = _name;
        librarian = _librarian;
    }

    wstring getName() const {
        return name;
    }

    void setName(wstring _name) {
        name = _name;
    }

    Librarian* getLibrarian() {
        return librarian;
    }

    void setLibrarian(Librarian* _librarian) {
        librarian = _librarian;
    }
};

class Library {
private:
    wstring name;
    int numBooks;
    Book* books;

public:
    Library() {
        name = L"";
        numBooks = 0;
        books = nullptr;
    }

    Library(wstring _name, int _numBooks) {
        name = _name;
        numBooks = _numBooks;
        books = new Book[numBooks];
    }

    ~Library() {
        delete[] books;
    }

    Library& operator=(const Library& other) {
        if (this != &other) {
            name = other.name;
            numBooks = other.numBooks;

            delete[] books;
            books = new Book[numBooks];
            for (int i = 0; i < numBooks; ++i) {
                books[i] = other.books[i];
            }
        }
        return *this;
    }
};

int main() {
    // Пример использования классов для библиотеки
    setlocale(LC_ALL, "");
    Librarian* librarian = new Librarian(L"Петрова", L"Научная литература");
    LibrarySection* section = new LibrarySection(L"Физика", librarian);
    Library library(L"Центральная библиотека", 5000);
    wcout << section->getName() << L" " << section->getLibrarian()->getName() << endl;
    wcout << librarian->getName() << L" " << librarian->getDepartment() << endl;

    delete section;
    delete librarian;

    return 0;
}
