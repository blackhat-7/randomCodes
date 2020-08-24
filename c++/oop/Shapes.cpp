#include <iostream>
#include <vector>


class Shape {
    public:
        virtual double GetArea() = 0;
};


class Circle : public Shape {
    protected:
        const double PI = 3.14159;
        double radius;
    public:
        Circle(): radius(0) {}
        Circle(double r): radius(r) {}

        double GetArea() override {
            return PI * (radius * radius);
        }

        Circle& operator ++ () {
            radius++;
            return *this;
        }

        Circle const& operator + (Circle const& other) {
            radius += other.radius;
            return *this;
        }
};

class Rectangle : public Shape {
    protected:
        double length, width;
    public:
        Rectangle(): length(0), width(0) {}
        Rectangle(double l, double w): length(l), width(w) {}
        double GetArea() override final {
            return length * width;
        }

        Rectangle& operator ++ () {
            length++; width++;
            return *this;
        }

        Rectangle& operator + (const Rectangle& other) {
            length += other.length;
            width += other.width;
            return *this;
        }
};


class Square : public Rectangle {
    public:
        Square(): Rectangle() {}
        Square(double l): Rectangle(l, l) {}
        Square(const Rectangle& r): Rectangle(r) {}
};

int main() {
    Square square(5);
    Rectangle rect(4, 5);
    Circle circle(6);
    Square square2(6);
    Square sumSquare = square + square2;
    std::cout << sumSquare.GetArea() << std::endl;
}
