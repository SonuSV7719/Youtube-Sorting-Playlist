#include<bits/stdc++.h>
using namespace std;

int main(){

    int n = 5;
    int arr[] = {5, 1, 7, 3, 8};
    for(int i = 0; i < n; i++){
        for(int j = i; j >= 0; j--){
            if(arr[j] < arr[j-1]){
                swap(arr[j], arr[j-1]);
            }
        }
    }

      for(int i= 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}