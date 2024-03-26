#include <iostream>
using namespace std;
class Shape {
public:
    virtual void draw() = 0;};
class Circle : public Shape {
public:
    void draw() override {
        wcout << L"Рисуем круг: " << L"()" <<endl;}};
class Square : public Shape {
public:
    void draw() override {
        wcout << L"Рисуем квадрат: "<< L"[]"<<endl;}};
int main() {
     setlocale(LC_ALL, "");
    Shape* shape;
    int option;
    do {
        wcout << L"Выберите фигуру для отрисовки:" << endl;
        wcout << L"1. Круг" << endl;
        wcout << L"2. Квадрат" << endl;
        wcout << L"0. Выход" << endl;
        wcout << L"Введите номер: ";
        wcin >> option;
        switch (option) {
            case 1:
                shape = new Circle();
                shape->draw();
                delete shape;
                break;
            case 2:
                shape = new Square();
                shape->draw();
                delete shape;
                break;
            case 0:
                wcout << L"Выход из программы." << endl;
                break;
            default:
                wcout << L"Ошибка: некорректный выбор." << endl;
                break;}} 
    while (option != 0);
    return 0;}
