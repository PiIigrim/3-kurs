#include <iostream>
using namespace std;
// Базовый класс
class BaseClass {
public:
    int baseVariable;
    void baseMethod() {
        wcout << L"Вызван метод базового класса" << endl;}};
// Производный класс
class DerivedClass : public BaseClass {
public:
    int derivedVariable;
    void derivedMethod() {
        wcout << L"Вызван метод производного класса" << endl;}};
int main() {
     setlocale(LC_ALL, "");
    // Создание объекта производного класса
    DerivedClass derivedObj;
    derivedObj.baseVariable = 42;
    derivedObj.derivedVariable = 10;
    // Использование указателей базового класса для доступа к объекту производного класса
    BaseClass* basePtr = &derivedObj;
    basePtr->baseVariable = 21;
    wcout << L"Значение baseVariable: " << derivedObj.baseVariable << endl;
    wcout << L"Значение derivedVariable: " << derivedObj.derivedVariable << endl;
    // Использование указателя производного класса для доступа к объекту производного класса
    DerivedClass* derivedPtr = &derivedObj;
    derivedPtr->baseVariable = 33;
    derivedPtr->derivedVariable = 99;
    cout << L"Значение baseVariable: " << derivedObj.baseVariable << endl;
    cout << L"Значение derivedVariable: " << derivedObj.derivedVariable << endl;
    return 0;}
