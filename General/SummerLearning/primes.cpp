#include <iostream>   
#include <cstdlib>

using namespace std;

int main(void) {
    int n, sum = 0, i;
    cout << "Please input a number: ";
    cin >> n;

    for(i = n; i > 0; i--) {
        if(n % i == 0) {
            sum++;
        }
    }
                  
    if(sum == 2) {
        cout << "Is a prime number." << endl;
    }
    else {
        cout << "Is not a prime number." << endl;
    }

    return 0;
}
