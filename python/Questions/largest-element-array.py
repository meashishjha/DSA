'''
Given an array, we have to find the largest element in the array.
Example 1:

Input:
 arr[] = {2,5,1,3,0};
Output:
 5
Explanation:
 5 is the largest element in the array.

Example2:

Input:
 arr[] = {8,10,5,7,9};
Output:
 10
Explanation:
 10 is the largest element in the array.
'''

def find_largest_element(arr):
    largest_element = 0
    for element in arr:
        if element > largest_element:
            largest_element = element

    return largest_element

input_array = [2,5,1,3,0]
print(find_largest_element(input_array))

#**************************************************************************
#* (C) Copyright by Ashish Jha (ash2kcs@gmail.com) and                    *
#* Outshine Labs. All Rights Reserved.                                    *
#*                                                                        *
#* DISCLAIMER: The authors and publisher of this book/code have used their*
#* best efforts in preparing the book/code. These efforts include the     *
#* development, research, and testing of the theories and programs        *
#* to determine their effectiveness. The authors and publisher make       *
#* no warranty of any kind, expressed or implied, with regard to these    *
#* programs or to the documentation contained in these books/code. The    *
#* authors and publisher shall not be liable in any event for incidental  *
#*  or consequential damages in connection with, or arising out of, the   *
#* furnishing, performance, or use of these programs.                     *
#**************************************************************************