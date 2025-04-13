const strings = [
    {
        heading: "Creating a String",
        shortP: `String creation in Python involves defining sequences of characters, typically enclosed within either single quotes (') or double quotes (").`,
        inputCode: `# Using single quotes
greeting = 'Hello, World!'

# Using double quotes
name = "Marie"

# Using triple quotes for multiline strings
message = '''This is a 
multiline string.'''

print(greeting)
print("My name is", name)
print(message)`,
            firstPar: "In python, there are different methods of creating strings:",
            breakdown: `
            <li>
                <h3>Using Single Quotes</h3>
                <p><code>greeting = 'Hello, World!'</code>: the string <code>'Hello, World!'</code> is assigned to the variable <code>greeting</code> using single quotes</p>
            </li>
            <li>
                <h3>Using Double Quotes</h3>
                <p><code>name = "Marie"</code>: the string <code>"Marie"</code> is assigned to the variable <code>name</code> using double quotes</p>
            </li>
            <li>
                <h3>Using Triple Quotes for Multiline Strings</h3>
                <p>This creates a multiline string where the text spans across multiple lines. The triple quotes (<code>'''</code>) allow you to create strings that extend over several lines without the need for explicit newline characters (<code>&#92;n</code>).</p>
            </li>`,
            outputCode: `Output:

Hello, World!
My name is Marie
This is a 
multiline string.`
    },
    {
        heading: "String Concatenation",
        shortP: "String concatenation in Python refers to the process of joining two or more strings together to create a single string.",
        inputCode: `#Using the + operator
str1 = "Hello"
str2 = " World"
result = str1 + str2
print(result)

#Using the += Augmented Assignment Operator

str1 = "Hello"
str2 = " User!"
str1 += str2
print(str1)

#Using f-Strings (Formatted Strings)
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)`,
            firstPar: "In python, there are different way to concatenate strings:",
            breakdown: `
            <li>
                <h3>Using the + operator</h3>
                <ul>
                    <li>
                        The <code>+</code> operator appends <code>str1</code> and <code>str2</code>, together, resulting in the string <code>"Hello World"</code> together.
                    </li> 
                    <li>
                        This method is simple and straightforward, but it may be less efficient than other methods, especially when concatenating many strings.
                    </li>
                </ul>
            </li>
            <li>
                <h3>Using the += Augmented Assignment Operator</h3>
                <ul>
                    <li>
                        The <code>+=</code> operator appends <code>str2</code> to <code>str1</code>, modifying <code>str1</code> directly.
                    </li>
                    <li>
                        This method can be more efficient than using the <code>+</code> operator, especially when concatenating strings in a loop or when modifying a string repeatedly.
                    </li>
                </ul>
            </li>
            <li>
                <h3>Formatted Strings</h3>
                <ul>
                    <li>
                        The <code>f</code> before the string indicates that it's an f-string.
                    </li>
                    <li>
                        Expressions inside <code>{}</code> are evaluated and replaced with their values when the string is created.
                    </li>
                    <li>
                        This method is concise and readable, especially when combining strings with variables or expressions.
                    </li>
                </ul>
            </li>`,
            outputCode: `Output:

Hello World
Hello User!
My name is Alice and I am 25 years old.`
    },
    {
        heading: "Accessing Strings",
        shortP: "In Python, you can access individual characters in a string using indexing. Strings in Python are zero-indexed, meaning the first character has an index of 0, the second character has an index of 1, and so on. You can access characters using square brackets <code>[]</code>and specifying the index of the character you want to retrieve.",
        inputCode: `greeting = "Hello, World!"

# Accessing individual characters
first_char = greeting[0] 
last_char = greeting[-1]

print("First character:", first_char)
print("Last character:", last_char)`,
            firstPar: "Let's break down the code:",
            breakdown: `
            <li>
                <code>first_char</code>: This line accesses the first character of the string <code>greeting</code> using indexing. Indexing in Python starts from 0, so <code>greeting[0]</code> retrieves the first character, which is <code>'H'</code>.
            </li>
            <li>
                <code>last</code>: This line accesses the last character of the string <code>greeting</code> using negative indexing. Negative indexing allows you to access characters from the end of the string. Since <code>-1</code> represents the last character, <code>greeting[-1]</code> retrieves the last character, which is <code>'!'</code>.
            </li>
            `,
            outputCode: `Output:

First character: H
Last character: !`
    },
    {
        heading: "String Length",
        shortP: "In Python, you can find the length of a string—the number of characters it contains—using the built-in function <code>len()</code>.",
        inputCode: `sentence = "This is a long sentence."

# Getting length of the string
length = len(sentence)

print("Length of the string:", length)

output:
Length of the string: 24`,
            firstPar: "In this example, the <code>len()</code> function is used to find the length of the string <code>sentence</code>, which contains 24 characters. The result is stored in the variable <code>length</code>, which is then printed to the console.",
            breakdown: `             
            `,
            outputCode: `Output:

Length of the string: 24`
    },
] 