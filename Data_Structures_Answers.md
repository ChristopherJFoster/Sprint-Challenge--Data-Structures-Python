Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

   The runtime complexity of my ring buffer's `append` method is `O(1)`. Regardless of the size of `n` (`self.storage`), the method goes right to the index matching `self.current` and replaces whatever is there with the new item.

2) What is the space complexity of your ring buffer's `append` function?

   The space complexity of my ring buffer's `append` function is also `O(1)`. Regardless of the size of `n` (`self.storage`), the `append` function is only called once.

3) What is the runtime complexity of your ring buffer's `get` method?

   The runtime complexity of my ring buffer's `get` method is `O(n)`, where `n` is the size of `self.storage`. The reason is that `get` should not, according to the instructions, return any `None` values. Therefore it must check each value in `self.storage`.

4) What is the space complexity of your ring buffer's `get` method?

   The space complexity of my ring buffer's `get` method is `O(1)`. Regardless of the size of `n` (`self.storage`), the `get` method is only called once.

5. What is the runtime complexity of the provided code in `names.py`?

   The runtime complexity is `O(n * m)`, where `n` is the size of one of the lists of names, and `m` is the size of the other of the lists of names. Each name in one list must be compared directly with each list in the other.

   If we assume that the lists will be of equal length, we can say the runtime complexity is `O(n^2)`.

6. What is the space complexity of the provided code in `names.py`?

   The space complexity of the provided code is `O(1)`. Though the nested loops take a long time to run, they do not require significant additional memory as the lists of names grow larger.

7. What is the runtime complexity of your optimized code in `names.py`?

   The runtime complexity of my optimized code is `O(n log m)` (or `O(n log n)` if we assume lists of equal length). Each name in the first list must still be iterated through (thus `n`), but by storing the second list in a binary search tree, each name in the first list will only be compared to `log n` of the names in the second list.

8. What is the space complexity of your optimized code in `names.py`?

   Since the `contains` method of my binary search tree uses recursion, the space complexity of my code is `O(log n)`. The `contains` function will run at most `log n` copies of itself concurrently.

   To be thorough, I should say that the space complexity of building the binary search tree is also `O(log n)` due to recursion in the `insert` function.
