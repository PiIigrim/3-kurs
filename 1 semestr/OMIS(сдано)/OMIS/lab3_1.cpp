#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    wstring name;
    int age;

public:
    Student() {
        name = L"";
        age = 0;
    }

    Student(wstring _name, int _age) {
        name = _name;
        age = _age;
    }

    wstring getName() const {
        return name;
    }

    void setName(wstring _name) {
        name = _name;
    }

    int getAge() const {
        return age;
    }

    void setAge(int _age) {
        age = _age;
    }
};

class Teacher {
private:
    wstring name;
    wstring specialization;

public:
    Teacher() {
        name = L"";
        specialization = L"";
    }

    Teacher(wstring _name, wstring _specialization) {
        name = _name;
        specialization = _specialization;
    }

    wstring getName() const {
        return name;
    }

    void setName(wstring _name) {
        name = _name;
    }

    wstring getSpecialization() const {
        return specialization;
    }

    void setSpecialization(wstring _specialization) {
        specialization = _specialization;
    }
};

class Course {
private:
    wstring name;
    Teacher* teacher;

public:
    Course() {
        name = L"";
        teacher = nullptr;
    }

    Course(wstring _name, Teacher* _teacher) {
        name = _name;
        teacher = _teacher;
    }

    wstring getName() const {
        return name;
    }

    void setName(wstring _name) {
        name = _name;
    }

    Teacher* getTeacher() {
        return teacher;
    }

    void setTeacher(Teacher* _teacher) {
        teacher = _teacher;
    }
};

class University {
private:
    wstring name;
    int numStudents;
    Student* students;

public:
    University() {
        name = L"";
        numStudents = 0;
        students = nullptr;
    }

    University(wstring _name, int _numStudents) {
        name = _name;
        numStudents = _numStudents;
        students = new Student[numStudents];
    }

    ~University() {
        delete[] students;
    }

    University& operator=(const University& other) {
        if (this != &other) {
            name = other.name;
            numStudents = other.numStudents;

            delete[] students;
            students = new Student[numStudents];
            for (int i = 0; i < numStudents; ++i) {
                students[i] = other.students[i];
            }
        }
        return *this;
    }
};

int main() {
    // Пример использования классов
    setlocale(LC_ALL, "");
    Teacher* teacher = new Teacher(L"Иванов", L"Математика");
    Course* course = new Course(L"Алгебра", teacher);
    University university(L"МГУ", 1000);
    wcout<<course->getName()<<L" "<<course->getTeacher()<<endl;
    wcout<<teacher->getName()<<L" "<<teacher->getSpecialization()<<endl;

    delete course;
    delete teacher;

    return 0;
}