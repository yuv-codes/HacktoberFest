//Bubble Sort
#include <stdio.h> 
# define Max 10
int arr[Max];
int display(int arr[],int n){
	int i;
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
}
int main()
{
	int n,i,temp;
	printf("Enter the range of array: ");
	scanf("%d",&n);
	printf("Enter the elements: ");
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	printf("\nBefore Sorting: ");
	display(arr,n);
	for(i=0;i<n;i++){
		for (int j=0;j<n-i;j++){
			if(arr[j]>arr[j+1]){
				temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
		}
	}
	printf("\nAfter Sorting");
	display(arr,n);
}