int mySqrt(int x) {
    double a=x;
    double b=1.0;
    double check = 0;
    double p = 0.01;
    do{
        b = (a/b+b)/2.0;
        check = b*b-a;
    }while(check>p);
    int result = b;
    return result;
}