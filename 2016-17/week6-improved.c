#include <stdio.h>

int main(void) {
  int count, currentNumber, i;
  scanf("%d", &count);
  // The array of process IDs
  int processIDs[count];
  // The main show happens in this loop
  for(i = 0; i < count; i++) {
    scanf("%d", &currentNumber);
    // If we haven't seen this process ID before
    if(processIDs[currentNumber] != 1) {
      processIDs[currentNumber] = 1;
    }
    // If we have...
    else {
      printf("%d", currentNumber);
      break;
    }
  }
  return 0;
}
