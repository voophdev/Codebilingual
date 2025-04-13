const data = [
  {
    header: "Integer",
    paragraph:
      "Integer data type represents whole numbers without any fractional part. These numbers can be positive, negative, or zero. They are represented without quotes and can be used for arithmetic operations such as addition, subtraction, multiplication, and division.",
    input: `# Integer data type
num = 10
print(num)`,
    output: `Output:

10`,
  },
  {
    header: "Float",
    paragraph:
      "The float data type represents real numbers with a fractional part. Floats are used to represent numbers that may have a decimal point. They can be positive, negative, or zero. Floats are represented with a decimal point, even if the value after the decimal is zero.",
    input: `#Float data type
num = 3.14
print(num)`,
    output: `Output:

3.14`,
  },
  {
    header: "String",
    paragraph: `The string data type represents sequences of characters enclosed within single (<code>' '</code>) or double (<code>" "</code>) quotes. Strings can contain letters, digits, symbols, and spaces. They are versatile and can store textual data, such as names, sentences, or even entire documents. Examples of strings include <code>"Hello"</code>, <code>'Python'</code>, and <code>"123"</code>. Strings support various operations like concatenation, slicing, and formatting. They are immutable, meaning once created, their contents cannot be changed.`,
    input: `#String data type
message = "Hello, World!"
print(message)`,
    output: `Output:

Hello, World!`,
  },
  {
    header: "Boolean",
    paragraph: `The boolean data type represents truth values: either True or False. Booleans are used to evaluate conditions in logical expressions and control flow statements. They are commonly used in conditional statements (if, elif, else), loops, and boolean operations. For example, True represents a condition being true, while False represents a condition being false. Booleans are essential for making decisions and controlling the flow of a program.`,
    input: `#Boolean data type
is_true = True
is_false = False
print(is_true)
print(is_false)`,
    output: `Output:

True
False`,
  },
  {
    header: "List",
    paragraph: `In Python, a list is a built-in data type used to store a collection of items. It is an ordered and mutable (modifiable) collection, meaning you can change, add, and remove elements after the list is created. Lists are denoted by square brackets <code>[ ]</code>, with comma-separated values inside.`,
    input: `#List data type
numbers = [1, 2, 3, 4, 5]
print(numbers)`,
    output: `Output:

[1, 2, 3, 4, 5]`,
  },
  {
    header: "Tuple",
    paragraph: `Tuple is another built-in data type used to store an ordered collection of items. Tuples are similar to lists, but unlike lists, tuples are immutable, meaning once they are created, their elements cannot be changed, added, or removed. Tuples are denoted by parentheses <code>( )</code>, with comma-separated values inside.`,
    input: `#Tuple data type
coordinates = (10, 20)
print(coordinates)`,
    output: `Output:

(10, 20)`,
  },
  {
    header: "Set",
    paragraph: `Sets are used to store an unordered collection of unique items. Sets are mutable, meaning you can add or remove elements after the set is created. Sets are denoted by curly braces <code>{ }</code>, or you can create a set using the built-in <code>set()</code> function.`,
    input: `#Set data type
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)`,
    output: `Output:

{1, 2, 3, 4, 5}`,
  },
  {
    header: "Dictionary",
    paragraph: `Python dictionary is a built-in data type used to store a collection of key-value pairs. Dictionaries are mutable, unordered, and indexed. Each key in a dictionary must be unique and immutable (such as strings, numbers, or tuples), and each key is associated with a value. Dictionaries are denoted by curly braces <code>{ }</code>, with key-value pairs separated by colons <code>:</code>.`,
    input: `#Dictionary data type
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person)`,
    output: `Output:

{'name': 'Alice', 'age': 30, 'city': 'New York'}`,
  },
];