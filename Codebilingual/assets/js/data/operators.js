const operators = [
    {
        heading: "Arithmetic Operators",
        firstPar: "Arithmetic operators are used to perform mathematical operations.",
        inputCode: `# Addition
result = 5 + 3
print("Addition:", result)

# Subtraction
result = 8 - 2
print("Subtraction:", result)

# Multiplication
result = 4 * 6
print("Multiplication:", result)

# Division
result = 20 / 5
print("Division:", result)

# Modulus
result = 10 % 3
print("Modulus:", result)

# Exponentiation
result = 2 ** 4
print("Exponentiation:", result)`,
        example: "The code given demonstrates the usage of various arithmetic operators in Python:",
        breakdown: 
        `
            <li><strong>Addition</strong>: <code>5 + 3 = </code> Adds two numbers together.</li>
            <li><strong>Subtraction</strong>: <code>8 - 2 = </code> Subtracts the second number from the first.</li>
            <li><strong>Multiplication</strong>: <code>4 * 6 = 24</code> Multiplies two numbers.</li>
            <li><strong>Division</strong>: <code>20 / 5 = 4.0</code> Divides the first number by the second.</li>
            <li><strong>Modulus</strong>: <code>10 % 3 = 1</code> Returns the remainder of the division.</li>
            <li><strong>Exponentiation</strong>: <code>2 ** 4 = 16</code> Raises the first number to the power of the second.</li>
        `,
        secondPar: "After performing these operations, the code prints out the values of sum, difference, multiplication, division, modulis, and exponentiation using print.",
        outputCode: `Output:

Addition: 8
Subtraction: 6
Multiplication: 24
Division: 4.0
Modulus: 1
Exponentiation: 16`
    },
    {
        heading: "Comparison Operators",
        firstPar: "Comparison operators are used to compare values. They return either True or False.",
        inputCode: `# Equal to
print(5 == 5)

# Not equal to
print(7 != 3)

# Greater than
print(10 > 5)

# Less than
print(2 < 4)

# Greater than or equal to
print(8 >= 8)

# Less than or equal to
print(6 <= 3)`,
        example: "The code given shows the different comparison operators in Python:",
        breakdown: 
        `
            <li><strong>Equal to</strong><code>(==)</code>: Checks if the left operand is equal to the right operand.</li>
            <li><strong>Not equal to</strong><code>(!=)</code>: Checks if the left operand is not equal to the right operand.</li>
            <li><strong>Greater than</strong><code>(>)</code>): Checks if the left operand is greater than the right operand.</li>
            <li><strong>Less than</strong><code>(<)</code>: Checks if the left operand is less than the right operand.</li>
            <li><strong>Greater than or equal to</strong><code>(>=)</code>: Checks if the left operand is greater than or equal to the right operand.</li>
            <li><strong>Less than or equal to</strong><code>(<)</code>): Checks if the left operand is less than or equal to the right operand.</li>
        `,
        secondPar: "Here's the output corresponding to each line of code:",
        outputCode: `Output:

True
True
True
True
True
False`
    },
    {
        heading: "Logical  Operators",
        firstPar: "Logical operators in Python are used to combine conditional statements. The three main logical operators are and, or, and not",
        inputCode: `# Logical AND
print(True and False)

# Logical OR
print(True or False)

# Logical NOT
print(not True)`,
        example: "Here's how the three main logical operator works:",
        breakdown: 
        `
            <li><strong>and</strong><code>:</code>Returns True if both statements are true.</li>
            <li><strong>or</strong><code>:</code>Returns True if one of the statements is true.</li>
            <li><strong>not</strong><code>:</code>Reverse the result, returns True if the result is false.</li>
        `,
        secondPar: "Here's the output corresponding to each line of code:",
        outputCode: `Output:

False
True
False`
    },
    {
        heading: "Assignment  Operators",
        firstPar: `The assignment operator in Python, denoted by "=", is used to assign a value to a variable. It operates from right to left, with the value on the right being assigned to the variable on the left.`,
        inputCode: `variable = value

#Example
x = 10
z = 0
print("Initial value of x:", x)
print("") #newline

#Reassignment
x = 20
print("Reassigned vaue of x:", x)
print("") #newline

#Multiple Assignment
a, b, c = 1, 2, 3
print("Multiple Assignment: ")
print("Value of a:", a)
print("Value of b:", b)
print("Value of c:", c)
print("") #newline

#Chained Assignment
print("Chained Assignment: ")
d = e = f = 0
print("Value of d:", d)
print("Value of e:", e)
print("Value of f:", f)
print("") #newline

#Augmented Assignment
print("Augmented Assignment: ")
z += 5  # Equivalent to z = z + 5
print("Value of z:", z)`,
        example: "Here's how the three main logical operator works:",
        breakdown: 
        `
            <li><code>x = 10</code>: The variable <code>x</code> is assigned the value <code>10</code>.></li>
            <li><code>x = 20</code>: The variable <code>x</code> is reassigned to the value <code>20</code></li>
            <li><code>a, b, c = 1, 2, 3</code>: You can assign multiple variables in a single line.</li>
            <li><code>d = e = f = 0</code>: You can assign the <strong>same</strong> value to multiple variables in a single line.</li>
            <li><code>z += 5  # Equivalent to z = z + 5</code>: Augmented assignment operators combine arithmetic operations with assignment.</li>
        `,
        secondPar: "Here's the output corresponding code:",
        outputCode: `Output:

Initial value of x: 10
Reassigned value of x: 20

Multiple Assignment: 
Value of a: 1
Value of b: 2
Value of c: 3

Chained Assignment: 
Value of d: 0
Value of e: 0
Value of f: 0

Augmented Assignment: 
Value of z: 5`
    },
]