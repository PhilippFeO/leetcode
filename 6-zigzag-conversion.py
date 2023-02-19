"""
solution for
    https://leetcode.com/problems/zigzag-conversion/
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:
        string convert(string s, int numRows);

    Solution scratch:
        * Pattern can be decomposed to concatenated sheered "V"s
        * => Process one "V", then iterate over all "V"s
"""

def main():
    s = "PAYPALISHIRING"
    num_rows = 4
    num_diag = num_rows - 2
    length_sheered_V = num_rows + num_diag
    zigzag = ""
    if num_diag < 0:
        zigzag = s
    else:
        for r in range(num_rows):
            for idx_sheered_V in range(0, len(s), length_sheered_V):
                idx = idx_sheered_V + r
                if idx < len(s):
                    zigzag += s[idx]
                if 0 == r or r == num_rows-1:
                    continue
                idx = idx_sheered_V + num_rows + num_diag - r 
                if idx < len(s):
                    zigzag += s[idx] 
    print(f"{zigzag = }")


if __name__ == "__main__":
    main()

