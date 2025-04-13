let secondContainerHTML = ''

strings.forEach((string) => {
  secondContainerHTML += 
  ` <div class="second-container">
        <h1>${string.heading}</h1>
        <p>${string.shortP}</p>
        <pre class="lang-python"><code class="lang-python">${string.inputCode}</code></pre>
        <p>${string.firstPar}</p>
        <ol>
          ${string.breakdown}
        </ol>
        <pre class="lang-"><code class="lang-">${string.outputCode}</code></pre>        
    </div>`;
});

document.querySelector('.js-second-container')
  .innerHTML = secondContainerHTML;