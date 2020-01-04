# Programming Assignment #9

## Description
Process a list of strings

## Instructions
1. To begin this program, create an empty list to store your data. Then, write the code to read from a file of unknown length, i.e., use a sentinel-controlled while loop. The data in the file will be strings (words). Stop reading when you reach a string “ZZZZZ”
Name the data file: **pa9.words**
As you read the strings, append them into your list. Remember to strip the strings as you read them.

	When done reading the file, print the following statistics:
	- length of the list
	- average word length (round to 1 decimal)
	- count of words that are longer than the average word length
	- count of vowels
	- print the list in reverse, but skip 10 items as you print (that is, step should be -10)

## Sample Run
	Length = 91
	Average Word Length = 4.5
	Number of words above average word length = 42
	A count = 40
	E count = 56
	I count = 27
	O count = 24
	U count = 13
	List printed in reverse, skipping 10 entries at a time ...
	changed , means , can , simple , types , both , operations , one , data , a ,