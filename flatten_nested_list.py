"""
Write a function that flattens arbitary layers of nested lists

For example:

arr = [[1,2,3], [4,5], 6]
flatten(arr) == [1,2,3,4,5,6]

arr = [ [[1,2], [3,4]], [5,6] ]
flatten(arr) == [1,2,3,4,5,6]
"""

from typing import List, Union

def flatten(arr: List[Union[List, int]]) -> List[int]:
    pass

if __name__ == "__main__":

    arr = []
    assert flatten(arr) == []

    arr = [1, 2, 3]
    assert flatten(arr) == [1, 2, 3]

    arr = [1, [2, [3, [4]]]]
    assert flatten(arr) == [1, 2, 3, 4]

    arr = [[[1, 2], 3], [4, [5]], 6, []]
    assert flatten(arr) == [1, 2, 3, 4, 5, 6]