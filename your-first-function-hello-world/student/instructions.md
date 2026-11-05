# Your First Function - Hello World

In this assignment you will write your very first function. A function is a named
block of code that you can use again and again.

Your task has two parts.

Part 1: Write a function
- Name the function `say_hello`.
- It takes no parameters.
- It must `return` the string `hello world` (all lowercase, with one space).
- The function should only return the text. It should not print it.

Part 2: Use the function
- Ask the user how many times to greet, using `input()`. Convert the answer to an integer.
- If the number is 1 or more, call `say_hello()` that many times. Print the result of each call on its own line.
- If the number is 0 or less, print exactly `Nothing to print` and nothing else.

You can assume the user always types a whole number.

Example 1:
  How many greetings? 2
  hello world
  hello world

Example 2:
  How many greetings? 0
  Nothing to print

Note: The tests look at the end of your program's output, so you can word your
"How many greetings?" prompt however you like. The greeting lines and the
`Nothing to print` message must match exactly.

Edge cases to consider:
- A count of 1.
- A count of 0.
- A negative count.
