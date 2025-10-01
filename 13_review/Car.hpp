// hpp is a header file or .h
// description of the class
#include <iostream>
#include <string>

class Car {

public:
    // Constructors
    Car(); // no arg
    Car(std::string make, std::string model, int year, double MPG); // multiple arg constructor



    // getters
    //  constant methods - cannot modify class properties
    std::string getMake() const;
    std::string getModel() const;
    int GetYear() const;
    double getMPG() const;
    double get_fuel_capacity() const;


    // Setters
    void setMake(std::string new_make);
    void setModel(std::string new_model);
    void setYear(int new_year);
    void setMPG(double new_MPG);


    // methods
    void print(void) const;


private:
    std::string make;
    std::string model;
    int year;
    double MPG;
};