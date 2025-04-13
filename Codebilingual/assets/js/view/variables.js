let secondContainerHTML = ''

data.forEach((item) => {
  secondContainerHTML += 
  `<div class="second-container">
    <h1>${item.header}</h1>
    <p>
      ${item.paragraph}
    </p>
    <div class="code-container">
      <div class="input-container">
<pre class="lang-python"><code class="lang-python">${item.input}</code></pre>
      </div>
      <div class="output-container">
<pre class="lang-"><code class="lang-">${item.output}</code></pre>
    </div>
  </div>
</div>`;
});

document.querySelector('.js-second-container')
  .innerHTML = secondContainerHTML;