#include "Car.hpp"



int main(void){
    // create a car object
    Car ferrari_spider("Ferrari", "Spider", 2021, 16.4);
    ferrari_spider.print();
    Car ferrari_f50;
    ferrari_f50.setMake("Ferrari");
    ferrari_f50.setModel("F 50");
    ferrari_f50.setYear(2025);
    ferrari_f50.setMPG(10.5);
    ferrari_f50.print();


    return 0;
}