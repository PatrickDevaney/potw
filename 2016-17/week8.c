// It counts as studying for the 60-140 midterm if I do it in C, right?

// Acceptable false positive rate (currently 0.8%) (1% made quinnftw.com malicious)
#define FALSEPOSRATE 0.008

#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// djb2a hash function - from http://www.cse.yorku.ca/~oz/hash.html
unsigned long hash(unsigned char *str) {
  unsigned long hash = 5381;
  int c;

  while (c = *str++)
    hash = hash * 33 ^ c;
  return hash;
}

// Performs an iteration of hashing
unsigned long hashIteration(char word[256], int iteration) {
  // Concatenate the word with the iteration number at the end
  sprintf(word, "%s%d", word, iteration);
  return hash(word);
}

int main(void) {
  // Get the number of words we're dealing with (n)
  int size;
  scanf("%d", &size);

  // The vector size (m)
  unsigned long vectorSize = ceil((-1 * size * log(FALSEPOSRATE)) / pow(log(2), 2));
  // Number of hashing iterations (k)
  unsigned long iterations = ceil((vectorSize / size) * log(2));
  // The actual bit array size (m/8)
  int bitArraySize = ceil(vectorSize / 8);
  unsigned char bitArray[bitArraySize];

  int i,j;
  // Set 0 (false) as the default value
  for(i = 0; i < bitArraySize; i++) {
    bitArray[i] = 0;
  }

  // Input the words and add them to the vector
  char buffer[256];
  unsigned long vectorPlace, bitArrayPlace, bitPlace;
  for(i = 0; i < size; i++) {
    scanf("%s", &buffer);
    // Add vector entries
    for(j = 0; j < iterations; j++) {
      // Perform an iteration of hashing
      vectorPlace = hashIteration(buffer, j) % vectorSize;
      // Find which bit to modify
      bitPlace = vectorPlace % 8;
      // Find where in the whole bit array that is
      bitArrayPlace = (vectorPlace - bitPlace) / 8;
      // Set that bit to true
      bitArray[bitArrayPlace] |= 1 << bitPlace;
    }
  }

  // Searching for words
  int searchNumber, check;
  bitPlace = bitArrayPlace = 0;
  // The number of words to check
  scanf("%d", &searchNumber);
  // Store the result for each site
  bool results[searchNumber + 1];
  for(i = 0; i < searchNumber; i++) {
    // By default it's malicious
    results[i] = 1;
    scanf("%s", &buffer);
    for(j = 0; j < iterations; j++) {
      check = hashIteration(buffer, j) % vectorSize;
      // Find which bit to check
      bitPlace = check % 8;
      // Find where in the whole bit array that is
      bitArrayPlace = (check - bitPlace) / 8;
      // Check if it's there
      if(((bitArray[bitArrayPlace] >> bitPlace) & 1) != 1) {
        // If not, then it must be safe
        results[i] = 0;
        break;
      }
    }
  }
  // Output the results
  for(i = 0; i < searchNumber; i++) {
    if(results[i] == 0) {
      printf("not malicious\n");
    }
    else {
      printf("maybe malicious\n");
    }
  }
  return EXIT_SUCCESS;
}
