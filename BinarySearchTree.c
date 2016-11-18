int numTrees(int n) {
    if(n<=1)
        return n;
    int *arrdp;
    arrdp = (int*)malloc(sizeof(int)*(n+1));
    arrdp[1]=1;
    arrdp[0]=1;
    int i,j;
    int temp;
    for(i=2;i<=n;i++){
        arrdp[i] = 0;
        temp = 0;
        if(i%2==0){// 
            for(j=0;j<=i-1;j++){
                temp = arrdp[j]*arrdp[i-j-1];
                arrdp[i] += temp;
            }
        }
        
        else{
            for(j=0;j<=i-1;j++){
                if(j!=(i-1)/2){
                    temp = arrdp[j]*arrdp[i-j-1];
                    arrdp[i] += temp;
                }
            }
            arrdp[i] += (arrdp[(i-1)/2]*arrdp[(i-1)/2]);
        }
    }
    return arrdp[n];
    
}
