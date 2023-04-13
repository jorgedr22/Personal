#include <stdio.h>
int power(int b, int n) {
    int p = 1;
    int q = b;
    int i = n;
    int count = 0;
    
    while (i > 0) {
        count ++;
        if (i % 2 == 1) {
            p *= q;
        }
        q *= q;
        i /= 2;
        
    }
    printf("number of passes: %d\n", count);
    return p;
}
int main(void) {
    int b;
    int n;
    
    printf("Enter number b and a positive integer n\n");
    
    scanf("%d", &b);
    scanf("%d", &n);
    
    int result = power(b, n);
    
    printf("%d^%d = %d\n", b, n, result);
    return 0;
}
