char* addBinary(char* a, char* b) {
    int la = strlen(a), lb = strlen (b);
    char c=0;
    int l;
    char* res;
    l = 2 + (la < lb ? lb : la);
    
    res = (char*)malloc(sizeof(char)*l);
    
    memset(res, '0', sizeof(char)*l);
    res[--l] = '\0';
    while(l--)
    {
        c += (la > 0? a[--la] - '0' : 0) + (lb > 0? b[--lb] - '0' :0);
        
        res[l] = c % 2 + '0';
        c /=2;
    }
   if(res[0] == '0')
   res++;
    return res;
    
}