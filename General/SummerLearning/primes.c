#include <stdio.h>
int main() {
    int n, sum = 0, i;
    printf("Please input a number: ");
    scanf("%d",&n);

    for(i = n; i > 0; --i) {
        if(n % i == 0) {
            ++sum;
        }
    }

    if (sum == 2)
        printf("Is a prime number.\n");
    else
        printf("Is not a prime number.\n");
    
    return 0;
}
