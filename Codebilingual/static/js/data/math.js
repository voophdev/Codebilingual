const mathPy = [
    {
        heading: "Basic Arithmetic Operations",
        firstPar: "In Python, the <code>math</code> module provides access to various mathematical functions and constants for performing mathematical operations. These functions cover a wide range of mathematical operations, including basic arithmetic, trigonometry, logarithms, exponentiation, and more.",
        inputCode: `import math

# Addition
num1 = 5
num2 = 3
add_result = num1 + num2

# Subtraction
num3 = 10
num4 = 3
sub_result = num3 - num4

# Multiplication
num5 = 7
num6 = 4
mul_result = num5 * num6 

# Division
num7 = 15
num8 = 3
div_result = num7 / num8 

# Floor Division
num9 = 20
num10 = 6
floor_div_result = num9 // num10

# Modulus
num11 = 17
num12 = 5
mod_result = num11 % num12

print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
print("Floor Division:", floor_div_result)
print("Modulus:", mod_result)`,
        secondPar: "Here are the basic arithmetic operators in Python:",
        breakdown: `
        <li><code>Addition(+)</code>: Adds two numbers together.</li>
        <li><code>Subtraction(-)</code>: Subtracts the second operand from the first.</li>
        <li><code>Multiplication(*)</code>: Multiplies two numbers.</li>
        <li><code>Division(/)</code>: Divides the first operand by the second. Returns a floating-point number.
        </li>
        <li><code>Floor Division(//)</code>: Divides the first operand by the second and returns the quotient as an integer, discarding any fractional part.</li>
        <li><code>Modulus(%)</code>: Returns the remainder of the division of the first operand by the second.</li>
        `,
        outputCode: `Output:

Addition: 8
Subtraction: 7
Multiplication: 28
Division: 5.0
Floor Division: 3
Modulus: 2`
    },
    {
        heading: "Trigonometric Functions",
        firstPar: "In Python, you can use trigonometric functions provided by the <code>Math</code> module for various trigonometric calculations.",
        inputCode: `import math

# Sine
angle_sine = math.pi / 6  # 30 degrees in radians
sin_result = math.sin(angle_sine)

# Cosine
angle_cosine = math.pi / 3  # 60 degrees in radians
cos_result = math.cos(angle_cosine)

# Tangent
angle_tangent = math.pi / 4  # 45 degrees in radians
tan_result = math.tan(angle_tangent)

# Inverse Sine
value_asin = 0.5
asin_result = math.asin(value_asin)

# Inverse Cosine
value_acos = 0.5
acos_result = math.acos(value_acos)

# Inverse Tangent
value_atan = 1.0
atan_result = math.atan(value_atan)

print("Sine:", sin_result)
print("Cosine:", cos_result)
print("Tangent:", tan_result)
print("Inverse Sine:", asin_result)
print("Inverse Cosine:", acos_result)
print("Inverse Tangent:", atan_result)`,
        secondPar: "Here are some commonly used trigonometric functions along with brief explanations:",
        breakdown: `
        <li>Sine<code>(sin)</code>: Returns the sine of a given angle in radians.</li>
        <li>Cosine <code>(cos)</code>: Returns the cosine of a given angle in radians.</li>
        <li>Tangent <code>(tan)</code>: Returns the tangent of a given angle in radians.</li>
        <li>Inverse Sine<code>(asin)</code>: Returns the inverse sine (in radians) of a given value.</li>
        <li>Inverse Cosine <code>(acos)</code>: Returns the inverse cosine (in radians) of a given value.</li>
        <li>Inverse Tangent<code>(atan)</code>: Returns the inverse tangent (in radians) of a given value.</li>
        `,
        outputCode: `Output:

Sine: 0.49999999999999994
Cosine: 0.5000000000000001
Tangent: 0.9999999999999999
Inverse Sine: 0.5235987755982989
Inverse Cosine: 1.0471975511965979
Inverse Tangent: 0.7853981633974483`
    },
    {
        heading: "Exponential and Logarithmic Functions",
        firstPar: "Exponential and logarithmic functions are demonstrated using <code> math.exp()</code>, <code>math.log()</code>, and <code>math.log10()</code>, for natural exponential, natural logarithm, and base 10 logarithm respectively.",
        inputCode: `import math

# Exponential
exp_value = math.exp(2)

# Natural logarithm
log_value = math.log(10)

# Logarithm base 10
log10_value = math.log10(100)

print("Exponential:", exp_value)
print("Natural Logarithm:", log_value)
print("Logarithm Base 10:", log10_value)`,
        secondPar: "These are the calculated values for each of the mathematical operations.",
        breakdown: `
        <li><code>math.exp(2)</code>: This calculates the exponential of 2, which is e^2 (where e is Euler's number, approximately 2.71828). The output for this line would be the value of e raised to the power of 2.</li>
        <li><code>math.log(10)</code>: This calculates the natural logarithm of 10. The output for this line would be the natural logarithm of 10, which is the power to which the base (e) must be raised to obtain 10.</li>
        <li><code>math.log10(100)</code>: ): This calculates the logarithm of 100 with base 10. The output for this line would be the logarithm of 100 to the base 10, which is simply 2 since 10^2 equals 100.</li>        
        `,
        outputCode: `Output:

Exponential: 7.3890560989306495
Natural Logarithm: 2.302585092994046
Logarithm Base 10: 2.0`
    },
    {
        heading: "Math Constants",
        firstPar: "This example introduces important mathematical constants like Pi (π) and Euler's number (e) using math.pi and math.e respectively.",
        inputCode: `import math

# Pi
pi_value = math.pi

# Euler's number
e_value = math.e

print("Pi:", pi_value)
print("Euler's Number:", e_value)`,
        secondPar: "These constants are commonly used in mathematical calculations and scientific programming. They're available in the math module, which provides a wide range of mathematical functions and constants for use in Python programs.",
        breakdown: `
        <li>
            <code>π (pi)</code>: π is a mathematical constant representing the ratio of a circle's circumference to its diameter, approximately 3.14159, and it's crucial in geometry and trigonometry.
        </li>
        <li>
            <code>Euler's number (e)</code>: Euler's number, denoted as 'e', is the base of the natural logarithm, approximately 2.71828, and it's essential in calculus and exponential growth models.
        </li>
        `,
        outputCode: `Output:

Pi: 3.141592653589793
Euler's Number: 2.718281828459045`
    },
]
