#include <iostream>
#include "Car.hpp"
// implementation of Car class
/*
todo
add:
milage: the odometer of the car
fuel_capacity: tanke of the car
fule_level: current fuel in gallons

methods:
void refuel(double gallons);
void drive(double distance); if car has enough fuel to drive the given distance print <car (make, model) is driving! >


*/
// no arg constructor
Car::Car(){
    setMake("Unknown");
    setModel("Unknown");
    setYear(1900);
    setMPG(0.0);
}
Car::Car(std::string make, std::string model, int year, double MPG){
    setMake(make);
    setModel(model);
    setYear(year);
    setMPG(MPG);
}


// setters
void Car::setMake(std::string new_make){
    if (!new_make.empty()){
        make = new_make;
    }
}
void Car::setModel(std::string new_model){
    if (!new_model.empty()){
        model = new_model;
    }
}
void Car::setYear(int new_year){
    year = (year >= 1900 && year <= 2025) ? new_year : 1900;
}
void Car::setMPG(double new_MPG){
    MPG = (new_MPG > 0 ) ? new_MPG : 0;
}

// getters
std::string Car::getMake() const {return make;}
std::string Car::getModel() const {return model;}
int Car::GetYear() const {return year;}
double Car::getMPG() const { return MPG;}

void Car::print(void) const{
    std::cout << getMake() << std::endl;
    std::cout << getModel() << std::endl;
    std::cout << GetYear() << std::endl;
    std::cout << getMPG() << std::endl;
}