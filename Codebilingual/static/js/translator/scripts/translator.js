import { getCompletions } from "./actions/getCompletions.actions.js";

const translationForm = document.getElementById("translation-form");
const code = document.getElementById("code");
const source = document.getElementById("source");
const target = document.getElementById("target");
const translatedCode = document.querySelector(".code-result");

function isPythonCodeValid(code) {
  // Regular expression to match common Python syntax elements
  const syntaxRegex =
    /\bdef\s+\w+\s*\(.*\)|\bclass\s+\w+\s*\(.*\)|\bif\s+.*:|\belif\s+.*:|\belse:|\bwhile\s+.*:|\bfor\s+\w+\s+in\s+.*:|\btry:|\bexcept\s+(.*)?:|\bfinally:|\bwith\s+.*:|\breturn\s+.*|\byield\s+.*|\bimport\s+.+|\bfrom\s+.+\s+import\s+.+|\bfor\s+\w+\s+in\s+range\(\d+\):|\bprint\s*\(.+\)|\b\d+\b|"\w*"|'\w*'/g;

  // Check if the code contains any syntax elements
  const matches = code.match(syntaxRegex);

  // If there are matches, consider the code valid; otherwise, it's invalid
  return !!matches;
}

function isCppCodeValid(code) {
  // Check for empty code
  if (!code.trim()) {
    console.error("C++ Syntax Error: Empty code");
    return false;
  }

  // Check for missing semicolon or closing brace
  if (
    !/;\s*\n/.test(code) ||
    (code.split("{").length - 1 !== code.split("}").length - 1)
  ) {
    console.error("C++ Syntax Error: Missing semicolon or closing brace");
    return false;
  }

  // Regular expression to check for common C++ syntax elements
  const syntaxRegex = 
    /#include\s+<.*>|int\s+main\s*\(\s*\)|std::\w+|using\s+namespace\s+std|return\s+\d+;/;

  // Check if the code contains any C++ syntax elements
  return syntaxRegex.test(code);
}

translationForm.addEventListener("submit", async (e) => {
  e.preventDefault(); // Prevent the default form submission behavior

  // Check if code is empty
  if (code.value.trim() === "") {
    alert("Error: Please enter some code.");
    return;
  }

  // Validate source code based on selected language
  if (source.value === "python") {
    // Check if Python code is valid
    if (!isPythonCodeValid(code.value)) {
      alert("Error: Python code syntax is invalid.");
      return;
    }

    // Check if the code contains any C++ syntax elements
    // if (isCppCodeValid(code.value)) {
    //   alert("Error: C++ code detected. Please select Python as the source language.");
    //   return;
    // }
  } else if (source.value === "cpp") {
    // Check if C++ code is valid
    if (!isCppCodeValid(code.value)) {
      alert("Error: C++ code syntax is invalid.");
      return;
    }

    // // Check if the code contains any Python syntax elements
    // if (isPythonCodeValid(code.value)) {
    //   alert("Error: Python code detected. Please select C++ as the source language.");
    //   return;
    // }
  }

  try {
    const outputResponse = await getCompletions({
      code: `Translate this function from ${source.value} code to ${target.value}.
  
      ${code.value} 

      output code only`,
    });

    // Check if response is empty or undefined
    if (!outputResponse || outputResponse.length === 0) {
      alert("Error: Unable to get translation. Please try again later.");
      return;
    }

    translatedCode.innerText = outputResponse;
  } catch (error) {
    console.error("An error occurred:", error);
    alert("Error: An unexpected error occurred. Please try again later.");
  }
});

code.addEventListener("keydown", (e) => {
  if (e.key === "Tab") {
    e.preventDefault();
    const cursorPosition = code.selectionStart;
    const contentBeforeCursor = code.value.substring(0, cursorPosition);
    const contentAfterCursor = code.value.substring(cursorPosition);

    const updatedContent = contentBeforeCursor + "\t" + contentAfterCursor;

    code.value = updatedContent;
    code.selectionStart = cursorPosition + 1;
    code.selectionEnd = cursorPosition + 1;
  }
});
