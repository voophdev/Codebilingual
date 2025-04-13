let secondContainerHTML = ''

mathPy.forEach((math) => {
  secondContainerHTML += 
`
<div class="second-container">
  <h1>${math.heading}</h1>
  <p>${math.firstPar}</p>
  <pre class="lang-python"><code class="lang-python">${math.inputCode}</code></pre>
  <p>${math.secondPar}</p>
  <ul>${math.breakdown}</ul>
  <pre class="lang-"><code class="lang-">${math.outputCode}</code></pre>
</div>`;
});

document.querySelector('.js-second-container')
  .innerHTML = secondContainerHTML;