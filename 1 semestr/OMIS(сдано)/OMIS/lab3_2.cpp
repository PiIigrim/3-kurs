//Возможным решением может быть добавление в класс "Студент" оценки по курсу (которая будет вещественным числом). Класс "Курс" может агрегировать студентов и их оценки. Дополнительно, мы можем добавить базовый класс "Person" с полями "name" и "age", от которого будут наследоваться классы "Student" и "Teacher". После добавления этих изменений, результирующий код будет выглядеть следующим образом:

#include <iostream>
#include <string>
using namespace std;

class Person {
protected:
    wstring name;
    int age;
public:
    Person() : name(L""), age(0) {}

    Person(wstring _name, int _age) : name(_name), age(_age) {}

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

class Student : public Person {
private:
    double grade;
public:
    Student() : Person(), grade(0.0) {}

    Student(wstring _name, int _age, double _grade) : Person(_name, _age), grade(_grade) {}

    double getGrade() const {
        return grade;
    }

    void setGrade(double _grade) {
        grade = _grade;
    }
};

class Teacher : public Person {
private:
    wstring specialization;
public:
    Teacher() : Person(), specialization(L"") {}

    Teacher(wstring _name, wstring _specialization) : Person(_name, 0), specialization(_specialization) {}

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
    Student* students;
    int numStudents;
public:
    Course() : name(L""), teacher(nullptr), students(nullptr), numStudents(0) {}

    Course(wstring _name, Teacher* _teacher, Student* _students, int _numStudents) 
        : name(_name), teacher(_teacher), students(_students), numStudents(_numStudents) {}

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

    Student* getStudents() {
        return students;
    }

    void setStudents(Student* _students, int _numStudents) {
        students = _students;
        numStudents = _numStudents;
    }
};

class University {
private:
    wstring name;
    int numStudents;
    Student* students;
public:
    University() : name(L""), numStudents(0), students(nullptr) {}

    University(wstring _name, int _numStudents, Student* _students) 
        : name(_name), numStudents(_numStudents), students(_students) {}

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
    Student students[2] = {Student(L"Иванов", 20, 4.5), Student(L"Петров", 19, 4.2)};
    Course* course = new Course(L"Алгебра", teacher, students, 2);
    University university(L"МГУ", 2, students);
    wcout<<course->getName()<<L" "<<course->getStudents()<<L" "<<course->getTeacher()<<endl;
    wcout<<students[0].getAge()<<L" "<<students[0].getGrade()<<L" "<<students[0].getName()<<endl;
    wcout<<students[1].getAge()<<L" "<<students[1].getGrade()<<L" "<<students[1].getName()<<endl;
    delete course;
    delete teacher;
    return 0;
}
/*
Здесь создается два студента с оценками, которые затем добавляются в курс и университет. Также преподаватель назначается на курс. 
В общем, студент имеет запланированную оценку (ставки), и эта оценка используется при создании объектов курса и университета.*/