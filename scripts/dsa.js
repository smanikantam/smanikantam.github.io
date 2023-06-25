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
  async function generateResponse(userInput) {
    // Load the ONNX model
    const session = new onnx.InferenceSession();
    const modelPath = '../media/nxt_word.onnx'; // Replace with the path to your ONNX model file
    await session.loadModel(modelPath);
  
    // Prepare the input data
    const sequence = tokenizer.textsToSequences([userInput])[0];
    const paddedSequence = padSequences([sequence], 15);
    const tensor = new onnx.Tensor(paddedSequence, 'float32', [1, paddedSequence.length]);
  
    // Run the inference
    const outputMap = await session.run([tensor]);
    const outputTensor = outputMap.values().next().value;
    const outputData = outputTensor.data;
    const predictedIndex = outputData.indexOf(Math.max(...outputData));
    const predictedWord = tokenizer.indexToWord[predictedIndex];
  
    return predictedWord;
  }
  
  
  