"""
solution for 
    https://leetcode.com/problems/trapping-rain-water/
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Task is solved by counting the fields between two eqaully high bars from
top to bottom. Going from top to bottom ensures there is always a
continuouos chain of free blocks, which can be filled with rain water.
"""

import numpy as np


def main():
    height = np.array([4,2,0,3,2,5])
    rain_water = 0
    max_height = np.amax(height)
    while (max_height > 0):
        # All indices were height is maximal
        idx = np.where(height==max_height)[0]
        # one single maximum can't form a basin => decrease height an
        # continue
        if len(idx)==1:
            # Decrease height by 1
            height[idx[0]] = height[idx[0]] - 1
        else:
            # <idx> contains more than one element => basin between each
            # index pair
            for i in range(len(idx) - 1):  # omit last index because it has no right basin
                # Skip calculation if two neighboring cells have the same height
                # Same height is implicitly given, since <idx> only contains
                # indices of the same (maximal) height.
                if idx[i+1] - idx[i] == 1:
                    # Do not forget to decrease height
                    height[idx[i]] = height[idx[i]] - 1
                    continue
                # calculate amount of rain water
                # 11-7=4 but "in between" are just 3, so substract by 1
                rain_water += idx[i+1] - idx[i] - 1
                # decrease heigt of processed index
                height[idx[i]] = height[idx[i]] - 1
            # decrease height of last index (not processed in loop)
            height[idx[-1]] = height[idx[-1]] - 1
        # decrease max_height
        max_height = max_height - 1
    print(f"{rain_water = }")


if __name__ == "__main__":
    main()
