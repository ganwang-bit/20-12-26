//#include <stdio.h>
//#include <stdlib.h>
//
//int main()
//{
//    printf("Hello world!\n");
//    return 0;
//}
#include<stdio.h>
int f(int a)
{
    {
        static int a=2;
    }
    return a+1;
}
int main()
{

    int a=1,b;
    b=f(a);
    printf("%d\n",b);
    b=f(a);
    printf("%d\n",b);
    return 0;
}
