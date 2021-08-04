#include "pbPlots.h"
#include "supportLib.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define LENGTH 500


int print(double arr[], int len);
double mean(double arr[]);
double sum(double arr[]);
double cov(double arr1[], double arr2[]);
double square(double arr[]);
double slope(double arr1[], double arr2[]);
double intercept(double arr1[], double arr2[]);
double predict(double arr1[], double arr2[]);


int main() {
  int i;
  double x[LENGTH], y[LENGTH];
  int loop;
  srand(time(0));

  for(i=0;i<LENGTH;i++){
    x[i] = (rand() % 5) * i + ((rand() % 25)/ 100.);
    y[i] = (rand() % 5) * i + ((rand() % 50)/ 10.);
   }

  printf("Mean_x: %f \n", mean(x));
  printf("Mean_y: %f \n", mean(y));
  printf("Cov_matrix_mean: %f \n", cov(x,y));
  printf("Square_x: %f \n", square(x));
  printf("Slope: %f \n", slope(x,y));
  printf("Intercept_point: %f \n", intercept(x,y));

  clock_t t;
  t = clock();
  predict(x,y);
  t = clock() - t;
  double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

  printf("predict(x,y) took %f seconds to execute \n", time_taken);

  return 0;
}


int print(double arr[], int len){
  for(len = 0; len < 10; len++){
     printf("x: %f \n", arr[len]);
   }
}

double sum(double arr[]){
  int j;
  double sum;
  for(j = 0; j < LENGTH; j++){
     sum += arr[j];
   }
  return sum;
}

double mean(double arr[]){
   return sum(arr) / LENGTH;
}

double cov(double arr1[], double arr2[]){
  double cov_arr[LENGTH];
  int c;
  for (c = 0; c < LENGTH; c++){
    cov_arr[c] = arr1[c]*arr2[c];
  }

  return sum(cov_arr) / LENGTH;
}

double square(double arr[]){
  double square_arr[LENGTH];
  int s;
  for(s = 0; s < LENGTH; s++){
    square_arr[s] = arr[s] * arr[s];
  }

  return sum(square_arr) / LENGTH;
}

double slope(double arr1[], double arr2[]){
  double s1,s2;
  s1 = cov(arr1,arr2) - (mean(arr1) * mean(arr2));
  s2 = square(arr1) - (mean(arr1) * mean(arr1));

  return s1/s2;
}


double intercept(double arr1[], double arr2[]){
  return mean(arr2) - mean(arr1) * slope(arr1, arr2);
}

double predict(double arr1[], double arr2[]){

  double b0 = slope(arr1, arr2);
  double b1 = intercept(arr1, arr2);
  double arr[LENGTH];
  int p;
  printf("Predicted Coefficients: \n");
  for(p = 0; p < LENGTH; p++){
    arr[p] = ((b0 * arr1[p]) + b1);
    printf("%f\n", arr[p]);
  }



	RGBABitmapImageReference *canvasReference = CreateRGBABitmapImageReference();
  DrawScatterPlot(canvasReference, 1000, 250, arr1, LENGTH, arr, LENGTH);

  size_t length;
  double *pngData = ConvertToPNG(&length, canvasReference->image);
  WriteToFile(pngData,length,"plot2.png");
  return 0;

}
