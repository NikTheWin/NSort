# NSort
Devicing a sorting algorithm for fun

A simple sorting algorithm used for learning and training in Python. I guess it's some kind of bastard between insertion sort and merge sort. The idea with this program is to test wether the algorithm is viable. And to have fun.

The algorithm is unstable and online

How it works:
There are two lists, one unsorted (the source) and one sorted (the target)

1. Pop one item from the source
2. At first the target is empty, just add the item
3. Pop another item from the source
4. Check it against the only item in the target, if greater add item after, if lesser add item add before
5. Pop another item from the source
6. Check it against the target, if greater than last item add after, if lesser than first item add before
   If item from source is between items in target, start from first item and iterate forward until the correct place in the list is found
7. Repeat steps 5 and 6 until target is 20 items big
8. Keep repeating step 5 and 6 but use a binary iteration to move within list

That's it!
