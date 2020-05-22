#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This algorithm has a runtime of O(n) because its while loop runs linear with respect to the input

b) This algorithm has a runtime of O(n log n) because the for loop is linear to the input and the while loop is log n of the input since it increases j by a multiple of 2 for every iteration ultimately cutting the ammount of time to reach its condition in half.

c) This algorithm has a runtime of O(n) because our recursive function aproches our base case in a linear fashion. If our input is 5 it will get closer to our base case by 1 for every call on itself.

## Exercise II

To find f and minimize dropped + broken I would use binary search as the core of this algorithm. If an egg is dropped at the middle and it broke we search the middle of the lower half else if the egg didnt break we search the upper half until middle - 1 doesn't break an egg.

the best case would be O(1) and worse case O(log n)
