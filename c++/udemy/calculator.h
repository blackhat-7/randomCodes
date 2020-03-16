#ifndef CALCULATOR_H_
#define CALCULATOR_H_

class Calculator {
private:

    long double a;
    long double b;

public:
    
    Calculator(): a(0), b(0) { }
    Calculator(long double a, long double b) {
        this->a = a;
        this->b = b;
    }

    long double sum() {
        return a + b;
    }

    long double subtract() {
        return a - b;
    }
};

#endif
