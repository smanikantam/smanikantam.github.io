function editCode() {
    // Get the current content from the website
    var currentContent = document.getElementById('code').innerHTML;

    // Prompt the user to enter the new content
    var newContent = prompt('Enter the new content:', currentContent);

    // Update the content on the website
    document.getElementById('code').innerHTML = newContent;
}

function copyCode() {
    const codeElement = document.getElementsByClassName('code-blok');
    const code = codeElement.textContent;

    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = code;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);

    alert('Code copied to clipboard!');
}
function changeTab(event, index,classname) {
    event.preventDefault(); // Prevents the default anchor tag behavior
    var codeBlocks = document.getElementsByClassName(classname);
    for (var i = 0; i < codeBlocks.length; i++) {
      if (i === index && codeBlocks[i].style.display != 'block') {
        codeBlocks[i].style.display = 'block';
      } else {
        codeBlocks[i].style.display = 'none';
      }
    }
  }
  