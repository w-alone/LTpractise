int minimumTotal(int** triangle, int triangleRowSize, int *triangleColSizes) {
    int dp_arrary[2][triangleColSizes[triangleRowSize-1]];
    //init
    int i,j,result;
    for(i=0;i<triangleColSizes[0];i++)
        dp_arrary[0][i] = triangle[0][i];
    //dp solution
    //j = 0;
    //if(triangleRowSize>1)
    for(j=1;j<triangleRowSize;j++)
        for(i=0;i<triangleColSizes[j];i++){
            if(i==0)
                dp_arrary[j%2][i] = dp_arrary[(j+1)%2][i]+triangle[j][i];
            else if(i==triangleColSizes[j]-1)
                dp_arrary[j%2][i] = dp_arrary[(j+1)%2][i-1]+triangle[j][i];
            else
                if(dp_arrary[(j+1)%2][i-1]>dp_arrary[(j+1)%2][i])
                    dp_arrary[j%2][i] = dp_arrary[(j+1)%2][i]+triangle[j][i];
                else 
                    dp_arrary[j%2][i] = dp_arrary[(j+1)%2][i-1]+triangle[j][i];
            
        }//for(i)
    result = dp_arrary[(j+1)%2][0];
    for(i=1;i<triangleColSizes[triangleRowSize-1];i++)
        if(dp_arrary[(j+1)%2][i]<result)
            result = dp_arrary[(j+1)%2][i];
    
    return result;
}