# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:12:51 2021

@author: turgu
"""

"""Encrypt a path through a Union Route Cipher.
Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers means start at top & read down.
Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.
  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END
Required inputs - a text message, # of columns, # of rows, key string
Prints translated plaintext
"""

import sys #3

# User Input 

plaintext = input("Please input your plain text: ") 


# number of columns in the in which you want to make in matrix #6
COLS = 4

#number of rows in the in which you want to make in matrix
ROWS = 5

#7 key with spaces between numbers; negative to read UP column  

key = """-1 2 -3 4"""

#8 END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#==============================================================================

def main():
    """Run program and print encrypted ciphertext."""
    print("\nplaintext = {}".format(plaintext)) 
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))
    print("Trying {} key".format(key))
    
    
    # split element into words, not letters
    plainlist = list(plaintext.split()) 
    validate_col_row(plainlist) 
    key_int = key_to_int(key) 
    encryption_matrix = build_matrix(key_int,plainlist) 
    ciphertext = encrypt(encryption_matrix) 
    
    print("Ciphertext = {}".format(ciphertext)) 
    
    
def validate_col_row(plainlist): #1
    """Check that input columns & rows are vs. message length"""
    factors = []
    len_cipher = len(plainlist)
    for i in range(2,len_cipher): #2 range exclufes 1-column ciphers
        if len_cipher % i ==0:
            factors.append(i)
            
    print("\nLength of cipher = {}".format(len_cipher)) #3
    print("Aceeptable column/row values include:{}".format(factors))
    print()
    
    if ROWS * COLS != len_cipher: #4
        print("\nError - Input columns & rows not factors of length"
              "of cipher. Terminating program.",file=sys.stderr)
        sys.exit(1)
        
        
def key_to_int(key):
    """Turn key in to list of integers & check validity"""
    key_int = [int(i) for i in key.split()] #6
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
            or 0 in key_int: #7
        print("\nError - Problem with key. Terminating.", file = sys.stderr) #8
        sys.exit(1)
    else:
        return key_int #9
       

def build_matrix(key_int,plainlist): #1
    """Turn every n items in a list into a new item in a list of lists."""
    encryption_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k<0: # write bottom to top of column
            col_items = list((reversed(plainlist[start:stop])))
            
        elif k > 0: #write top to bottom of column
            col_items = plainlist[start:stop]
        encryption_matrix[abs(k)-1] = col_items
        start += ROWS
        stop += ROWS
    return encryption_matrix
    
def encrypt(encryption_matrix):
    """Loop through nested lists popping off last item to a string."""
    encrypttext =''
    for i in range(ROWS):
        for matrix_col in encryption_matrix:
            word = str(matrix_col.pop())
            encrypttext += word + ' ' 
    return encrypttext

if __name__ == '__main__':
    main()       
    

# rest transport you godwın vıllage roanoke wıth are your ıs just supplies free snow heading to gone to suth fıller