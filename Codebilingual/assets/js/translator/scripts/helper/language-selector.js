document.getElementById("source").addEventListener("change", function() {
  var sourceValue = this.value;
  var targetDropdown = document.getElementById("target");
  
  if (sourceValue === "cpp") {
    if (targetDropdown.value === "cpp") {
      targetDropdown.value = "python";
    }
  } 
  else if (sourceValue === "python") {
    if (targetDropdown.value === "python") {
      targetDropdown.value = "cpp";
    }
  }
});

document.getElementById("target").addEventListener("change", function() {
  var targetValue = this.value;
  var sourceDropdown = document.getElementById("source");
  
  if (targetValue === "cpp") {
    if (sourceDropdown.value === "cpp") {
      sourceDropdown.value = "python";
    }
  } 
  else if (targetValue === "python") {
    if (sourceDropdown.value === "python") {
      sourceDropdown.value = "cpp";
    }
  }
});
