function editCode() {
    // Get the current content from the website
    var currentContent = document.getElementById('code').innerHTML;

    // Prompt the user to enter the new content
    var newContent = prompt('Enter the new content:', currentContent);

    // Update the content on the website
    document.getElementById('code').innerHTML = newContent;
}

function copyCode() {
    const codeElement = document.getElementById('code');
    const code = codeElement.textContent;

    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = code;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);

    alert('Code copied to clipboard!');
}