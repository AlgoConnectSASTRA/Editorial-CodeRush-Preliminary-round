Separate into alice's books and bob's books.

For each alice and bob,

1. We have to keep the top element of each tower in an array. Initially empty.
2. Use[ Binary search](https://leetcode.com/problems/search-insert-position/) to find which is the best place to update the new element. If it cannot be placed on top of any towers, add it as a new element.
3. Finally, return the length of this array.

Return the best performer.
