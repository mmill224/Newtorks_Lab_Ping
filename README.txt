Matthew Miller

A small python program I made to make a Networks class assigment easier


The assignment was to ping a KSU server 100 times and make a histogram of the data. The program prints on the left the number of 
milliseconds, and to the right, it prints a number of pluses equal to the number of pings at that number of milliseconds in the console.

The program reads the response from a ping, looks for the number of milliseconds it took, and fills up an array with that. Then the 
program performs a bucket sort on the data from the first array - the index of the sorted array is equal to the number of miliseconds, and
the value at the index is equal to the number of occurences. In order to keep the size of the sorted array lower, the program uses the 
minimum value from the first array as the base index for the second array. 

The program should run in O(n) time (not accounting for how long it takes you to ping the server 100 times)

Some improvements that could be made:
  Make use of python libraries that handle representing data
  Make the code easier to read
  Check if the user has the python packages required

Here's a sample of the output:
[37, 36, 36, 37, 36, 36, 36, 37, 37, 36, 37, 39, 36, 37, 37, 36, 37, 37, 36, 36, 36, 38, 37, 36, 36, 36, 36, 36, 37, 36, 37, 36, 38, 37,
36, 37, 37, 36, 37, 36, 36, 36, 36, 38, 37, 38, 36, 36, 39, 37, 37, 36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 36, 36, 36, 37, 36,
36, 36, 36, 36, 37, 36, 36, 37, 40, 38, 37, 37, 37, 36, 37, 36, 37, 37, 37, 36, 37, 36, 36, 37, 37, 37, 37, 36, 36, 37, 39, 37]
[52, 39, 5, 3, 1]
36      ++++++++++++++++++++++++++++++++++++++++++++++++++++
37      +++++++++++++++++++++++++++++++++++++++
38      +++++
39      +++
40      +
