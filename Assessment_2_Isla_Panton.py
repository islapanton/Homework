"""  PYTHON AND MYSQL ASSESSMENT TEST - 2 hours  """

""" 1. Python theory questions """

# 1.	What is the program?
# A program is a set of instructions that inform the computer what actions or behaviours it should carry out.

# 2.	What is the process?
# A process is the method the computer will follow through a set of instructions (the programme) to achieve the desired outcome.

# 3.	What is Cache?
# Cache is a small portion of computer memory that is used to store frequently used programs or processes

# 4.	What is Thread and Multithreading?
# A thread is used to allow two parts of a programme or two functions  to happen at the same time


# 5.	What is GIL in Python and how does it work?
# Global Interpreter Lock but can't remember what it does??

# 6.	What is Concurrency and Parallelism and what are the differences?


# 7.	What do these stand for in programming: DRY, KISS, BDUF
# DRY is an acronym for Don't Repeat Yourself
# KISS is an acronym for Keep It Simple Stupid
# BDUF is an acronym for Big Design Up Front


# 8.	What is Garbage collector? How does it work?


# 9.	What are ‘deadlock’ and ‘livelock’ in a relational database?
# A deadlock occurs when there are multiple tasks or queries that require another to be completed before they can proceed
# and therefore they cannot move forward in any respect so no progress can be made as they are waiting for each other.
# A livelock is

# 10.	What is Flask and what can we use it for?
# Flask is a microframework (which means it is relatively small and simple/easy to use) that allows us to develop
# web applications easily and is often very useful when dealing with APIs.


""" 2. Discuss the difference between Python 2 and Python 3 """
#???

""" 3. Write a function that can define whether a word is a Palindrome 
or not (a word, phrase, or sequence that reads the same backwards as 
forwards, e.g. madam) """
def is_palindrome(string):
    if string == string[::-1]:
        answer_t = 'True: This string is a palindrome'
        print(answer_t)
    else:
        answer_f = 'False: This string is not a palindrome '
        print(answer_f)

string = input('Type a word that you would like to check whether it is a palindrome or not:   ')
is_palindrome(string)

""" 4.	Write tests for the newly created Palindrome function.
Provide a brief explanation for your test case options. """
import unittest

def test_inverted_word(self):
    is_palindrome =

    self.assertTrue(result)




    """
5. Agile methodology, Scrum: name at least 3 types of meetings that are
exercised by Agile teams and describe the objective of each meeting.

Daily Scrum : This is a short daily meeting for the team to discuss what they were working
on in the previous day and what they will be working on today.
It is also an opportunity to set out or discuss any obstacles or issues facing the team as
a whole which could inhibit the sprint.

Sprint Review : This meeting is used to review or present what the sprint has achieved and
decide whether the goals and requirements of the sprint have been met and achieved.

Sprint Retrospective: This comes after the review meeting and is used to discuss what worked,
what didn't work and how they could be improved next time.This helps teams to be constantly
developing and improving, encouraging development and growth.

"""


""" 
6.	Exception handling in Python, explain what each of the following blocks 
means in the program flow (try, except, else, finally):
Try: This block is the code we are wanting to run in the function. So we are giving the code a chance to execute

Except : This block details what we want to happen if there is an exception or error. 
It is where we are likely to raise exceptions or print error messages. 

Else: This block contains what we would like to happen if there are no exceptions in our code / its execution. 

Finally: This block will execute no matter what, so comes at the end and will run whether there is an exception or not.

See example below:  

"""
a = int(input('Please insert a value:   '))
b = int(input('Please insert a value:   '))
try:
    if a > 1:
        c = a / b
except:
    a < 1 or a ==1 or b < 1 or b == 1
    raise ZeroDivisionError ('Invalid input. You cannot divide by zero. ')
else:
    c = a / b
    print(c)
finally:
    print('Thanks for using our calculator!')

""" 7. How can we connect a Python program (process) with a database? 
Explain how it works and how do we fetch / insert data into DB tables from a python program.

To connect a Python program with a database, we first have to establish a connection with our mysql server using our 
username, password and details of the host (often this is local) and call on the package mysql.connector to help with this. 

Once we have established a connection to the relevant database, we can write SQL queries in our IDE file, adding extra '' 
and {} to allow the code to work properly as these queries are not valid python syntax. In this way, we can directly 
insert or fetch data from SQL databases using an established connection to our server. 
 
"""

""" 
8. Given two SQL tables below: authors and books (!!!PLEASE CHECK THE ASSESSMENT2 DOCUMENT FOR THE TABLES!!!)
●	 The authors dataset has 1M+ rows
●	 The books dataset also has 1M+ rows 
Create an SQL query that shows the TOP 3 authors who sold the most books in total!

"""
''''
# Here I created a joined table (on an inner join) and then did my select statement below. 
CREATE TABLE new_joined_table(
select b1.author_name as AuthorName, b1.book_name as BookName, b2.sold_copies as CopiesSold
from authors b1 
inner join books b2
on b1.book_name = b2.book_name)
; 

Select AuthorName, sum(CopiesSold) as Total_Copies_Sold
from new_joined_table
WHERE AuthorName LIKE AuthorName
group by AuthorName
order by Total_Copies_Sold DESC; 
'''


"""
9.	TWO NUMBER SUM: 

●	Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
    If any two numbers in the input array sum up to the target sum, the function should return 
    them in an array, in any order. If no tWo numbers sum up to the target sum, the function should 
    return an empty array.

●	Note that the target sum has to be obtained by summing two different integers in the array. 
    You cannot add a single integer to itself in order to obtain the target sum.

●	You can assume that there will be at most one pair of numbers summing up to the target sum. 

Sample Input: 
    numbers = [3, 5, -4 ,8, 11, 1, -1, 6]  
    target_sum = 10

Sample Output: 
    [-1, 11] the numbers can be in any  order, it does not matter. 

"""
numbers = [3, 5, 2, 8, 11, 1, -1, 6]
target_sum = 10

def sum():
    for x in numbers:
        for y in numbers:
            if x+y == target_sum and x != y:
                print([x,y])
                numbers.remove(x)
                numbers.remove(y)
                break
    if x+y!= target_sum:
        numbers.clear()
        print(numbers)
        print('There are no numbers in the array which sum up to the target.')

sum()