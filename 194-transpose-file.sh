#!/bin/sh
# solution for 
#    https://leetcode.com/problems/transpose-file/

#export PS4="\$LINENO: "
#set -xv

file="194-file.txt"
transposed_file="194-file-transposed.txt"
# delete file contents
cat /dev/null > $transposed_file

# count ' ' (spaces) in the first line as the are the delimiter
#   no trailing spaces assumed
#   +1 because there is always one delimiter less than entries
nmb_cols=$(($(head -1 194-file.txt | grep -o " " | wc -l) + 1))
# iterate over evey column
for i in $(seq 1 $nmb_cols); do
    # extract column, replace newlines with spaces, append to output file
    cut -d " " -f $i < $file | tr "\n" " " >> $transposed_file
    # append newline for proper formatting
    echo "" >> $transposed_file
done
