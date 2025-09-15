#include <iostream>
#include <vector>



int numberOfDuplicates(const std::vector<int>& v, int nums);

int numberofDuplicates(const std::vector<int>& v, int nums){
    int duplicates = 0;
    for (int i = 0; i < v.size(); i++){
        if (nums = v[i]){
            duplicates++;
        }
    }
    std::cout << duplicates << std::endl;
    return 0;
}

int printVector(const std::vector <int>& v){
    for(int el: v){
        std::cout << el << ',';
        std::cout <<" ";

    }
    std::cout << std::endl;
    return 0;
}

int main(){
    std::vector v {1,2,3,4,4,5,6,7};
    numberofDuplicates(v, 4);
    printVector(v);
}


