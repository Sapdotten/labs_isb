#include <iostream>
#include <random>
#include <ctime>

int main() {
    int sequenceLength = 128;
    srand(time(0));
    for (int i = 0; i < sequenceLength; i++) {
        int randomNumber = rand()%2;
        std::cout<<randomNumber;
    }
    return 0;
}