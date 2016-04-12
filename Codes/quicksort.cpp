#include <iostream>

using namespace std;

int Partition (int *a, int start, int end);
void Quicksort(int *a, int start, int end);

int main(){
	int a[]={7,2,1,6,8,5,3,4};
	Quicksort(a,0,7);
	for (int i=0; i<8;i++)
	{
		cout<<a[i]<<" ";
	}

}
int Partition(int *a, int start, int end)
{
	int pivot = a[end];
	int partitionIndex=start;
	for(int i = start;i<end;i++)
	{
		if(a[i]<=pivot){
			int temp = a[partitionIndex];
			a[partitionIndex] = a[i];
			a[i]=temp;
			partitionIndex++;
		}
	}
	int temp2=a[partitionIndex];
	a[partitionIndex] = a[end];
	a[end]=temp2;
	return partitionIndex;
}
void Quicksort(int *a, int start, int end)
{
	if (start<end)
	{
		int partitionIndex = Partition(a, start, end);
		Quicksort(a,start,partitionIndex-1);
		Quicksort(a,partitionIndex+1,end);
	}
}

