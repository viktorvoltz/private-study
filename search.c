#include<stdio.h>

//assuming the emlements of the array are in increasing order!!
int main(){
    int c, first, last, middle, n, search, array[100];

    printf("enter number of element: \n");
    scanf("%d", &n);
    printf("enter %d integer: \n", n);
    
    for(c = 0; c < n; c++){
    	scanf("%d", &array[c]);
	}
	
	printf("Enter the value to find: \n");
	scanf("%d", &search);
	
	first = 0;
	last = n - 1;
	middle = (first + last) / 2;
	while (first <= last){
		if (array[middle] < search){
			first = middle + 1;
			middle = (first + last)/2;
			printf("...searching \n");	
		}
		else if(array[middle] == search){
			printf("%d is present at index %d \n", search, middle + 1);
			break;
		}
		else{
			last = middle - 1;
			middle = (first + last)/2;
			printf("...searching \n");
		}
		
	}
	
	if (first > last){
		printf("%d not found, search terminated", search);
	}
	
    
    return 0;
}