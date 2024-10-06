#include<stdio.h>

int main()
{
    int n;
    printf("Enter the limit of the array: ");
    scanf("%d",&n);
    int a[n];
    printf("Enter the elements in the array: \n");
    for(int i = 0; i < n; i++){
        scanf("%d",&a[i]);
    }
    int c=0;
    for(int i=0;i<n-1;i++){
        int inx=i;
        for(int j=i+1;j<n;j++){
            c++;
            if(a[inx]>a[j]){
                inx=j;
            }
        }
        int temp=a[i];
        a[i]=a[inx];
        a[inx]=temp;
    }
    printf("The Sorted array is: \n");
    for(int i=0; i < n; i++){
        printf("%d ",a[i]);
    }
    printf("\n%d",c );
    return 0;
}