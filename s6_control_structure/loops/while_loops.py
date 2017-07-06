
"""
A while loop statement in Python programming language repeatedly executes a target statement
as long as a given condition is true.

Syntax
The syntax of a while loop in Python programming language is −

while expression:
   statement(s)

Here, statement(s) may be a single statement or a block of statements.

The condition may be any expression, and true is any non-zero value.

The loop iterates while the condition is true.

When the condition becomes false, program control passes to the line immediately following the loop.
"""

a = 10
while a > 0:
    print('a =', a)
    a = a - 1
print('finished')