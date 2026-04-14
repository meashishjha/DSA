# (C) Copyright 2026 by Ashish Jha and Outshine Labs.                       #
# All Rights Reserved.  https://wwww.ashishjha.com/                         #
# Copyright.  https://wwww.outshinelabs.com/                                #
#                                                                           #
# DISCLAIMER: The authors and publisher of this book/code have used their   #
# best efforts in preparing the book/code. These efforts include the        #
# development, research, and testing of the theories and programs           #
# to determine their effectiveness. The authors and publisher make          #
# no warranty of any kind, expressed or implied, with regard to these       #
# programs or to the documentation contained in these books/codes.          #
# The authors and publisher shall not be liable in any event for incidental #
# or consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                        #

# print n times

def print_n_times(n):
    if n <= 0:
        return
    print("This is first time")
    print_n_times(n-1)

print_n_times(3)