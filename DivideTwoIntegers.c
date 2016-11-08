int divide(int dv, int dr) {
    if(dv == INT_MIN && dr == -1 || dr == 0)
        return INT_MAX;
    unsigned int tmp = dv,sum = dr,ret = 0,cnt = 1,sign = 1;
    if(tmp & INT_MIN)
        tmp = ~(tmp -1);/// get absolute value
    if(sum & INT_MIN)
        sum = ~(sum -1);///get absolute value
    if(tmp < sum)
        return 0;
    unsigned int  ts = sum;
    while(tmp - sum >= sum) sum <<= 1,cnt <<=1;
    while(sum >= ts)
   {
        if(sum <= tmp)
        {
            ret += cnt;
           tmp -= sum;
        }
        sum >>= 1,cnt >>= 1;
    }
    if((dv^dr)&INT_MIN)/// check if the result should be negative.
        ret = (~ret) + 1;
    return ret;
}