#include <stdio.h>

int main(void) {
  int hour;
  float min;
  float total_hour,temp;
  printf ("Enter hour :\n");
  scanf ("%d", &hour);
  printf ("Enter minute:\n");
  scanf ("%f", &min);
  total_hour = hour +(min/60.0);
  temp = ((4*(total_hour * total_hour))/(total_hour+2))-20;
  printf("The temperature is : %f", temp);
  return 0;
}