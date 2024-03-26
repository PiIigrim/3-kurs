#include <iostream>
using namespace std;
// Базовый класс
class BaseClass {
public:
    int baseVariable;
    virtual void method() {
        wcout << L"Вызвана виртуальная функция базового класса" << endl;}};
// Производный класс
class DerivedClass : public BaseClass {
public:
    int derivedVariable;
    void method() override {
        wcout << L"Вызвана виртуальная функция производного класса" << endl;}};
int main() {
    setlocale(LC_ALL, "");
    // Создание объекта производного класса
    DerivedClass derivedObj;
    derivedObj.baseVariable = 42;
    derivedObj.derivedVariable = 10;
    // Использование указателей базового класса для вызова виртуальной функции
    BaseClass* basePtr = &derivedObj;
    basePtr->method();
return 0;}
