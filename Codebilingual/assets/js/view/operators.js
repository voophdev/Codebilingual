let secondContainerHTML = ''

operators.forEach((operator) => {
  secondContainerHTML += 
`<div class="second-container">
  <h1>${operator.heading}</h1>
  <p>${operator.firstPar}</p>
  <pre class="lang-python"><code class="lang-python">${operator.inputCode}</code></pre>
  <p>${operator.example}</p>
  <ul>
    ${operator.breakdown}
  </ul>
  <p>${operator.secondPar}</p>
  <pre class="language-"><code class="language-">${operator.outputCode}</code></pre>
</div>`;
});

document.querySelector('.js-second-container')
  .innerHTML = secondContainerHTML;