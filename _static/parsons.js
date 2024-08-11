/**
 * Preprocesses the code by replacing semicolon-separated lines with a marker.
 * @param {string} codeString - The full code as a string.
 * @returns {Array} - An array of objects containing the code blocks with markers.
 */
function preprocessCode(codeString) {
    const lines = codeString.trim().split('\n').filter(line => line.trim() !== '');
    let processedBlocks = [];
    lines.forEach((line, index) => {
        if (line.includes(';')) {
            // Replace semicolon with a special marker to keep the lines together
            const parts = line.split(';').map(part => part.trim());
            parts.forEach((part, i) => {
                processedBlocks.push({
                    line: part,
                    order: index + i,
                    marker: i === parts.length - 1 ? null : `MARKER_${index}_${i}`
                });
            });
        } else {
            processedBlocks.push({ line, order: index, marker: null });
        }
    });
    return processedBlocks;
}



function checkSolution(dropArea, codeLineObjects, feedbackElement, fullCodeElement, solutionModal) {
    const droppedItems = Array.from(dropArea.children).filter(item => !item.classList.contains('placeholder'));
    const droppedOrder = droppedItems.map(item => item.dataset.order);
    const correctOrder = codeLineObjects.sort((a, b) => a.order - b.order).map(obj => obj.order.toString());

    if (JSON.stringify(droppedOrder) === JSON.stringify(correctOrder)) {
        feedbackElement.textContent = 'Riktig!';
        feedbackElement.style.color = 'green';

        // Combine the full code and show it in the modal, preserving indentation
        const fullCode = droppedItems.map(item => item.textContent).join('\n');
        fullCodeElement.textContent = fullCode;

        // Apply syntax highlighting to the full code
        hljs.highlightElement(fullCodeElement);

        solutionModal.style.display = 'block';
    } else {
        feedbackElement.textContent = 'Prøv igjen!';
        feedbackElement.style.color = 'red';
    }
}


/**
 * Initializes a Parsons puzzle by setting up the drag-and-drop elements,
 * the solution checking mechanism, and the reset functionality.
 * @param {string} puzzleContainerId - The ID of the puzzle container element.
 * @param {string} codeString - The code as a single string to be split and randomized.
 */
function initializeParsonsPuzzle(puzzleContainerId, codeString) {
    const puzzleContainer = document.getElementById(puzzleContainerId);
    const dropArea = puzzleContainer.querySelector('#drop-area');
    const checkButton = puzzleContainer.querySelector('#check-solution');
    const resetButton = puzzleContainer.querySelector('#reset-puzzle');
    const feedback = puzzleContainer.querySelector('#feedback');
    const draggableCodeContainer = puzzleContainer.querySelector('#draggable-code');
  
    // Create a unique modal for this puzzle
    const solutionModal = createSolutionModal(puzzleContainerId);
    const fullCodeElement = solutionModal.querySelector(`#fullCode-${puzzleContainerId}`);
    const closeModalButton = solutionModal.querySelector('.close');
    const copyCodeButton = solutionModal.querySelector(`#copyCodeButton-${puzzleContainerId}`);
  
    let codeLines = splitAndShuffleCode(codeString);
  
    renderDraggableCode(draggableCodeContainer, codeLines);
    createPlaceholder(dropArea);
    enableDragAndDrop(draggableCodeContainer, dropArea);
  
    checkButton.addEventListener('click', () => {
      checkSolution(dropArea, codeLines, feedback, fullCodeElement, solutionModal);
    });
  
    resetButton.addEventListener('click', () => {
      resetPuzzle(draggableCodeContainer, dropArea, codeString, feedback);
    });
  
    // Close the modal when the close button is clicked
    closeModalButton.addEventListener('click', () => {
      solutionModal.style.display = 'none';
    });
  
    // Copy code to clipboard when the copy button is clicked
    copyCodeButton.addEventListener('click', () => {
      navigator.clipboard.writeText(fullCodeElement.textContent).then(() => {
        alert('Code copied to clipboard!');
      });
    });
  }
  
  /**
   * Creates a solution modal dynamically for the given puzzle container.
   * @param {string} puzzleContainerId - The ID of the puzzle container.
   * @returns {HTMLElement} - The created modal element.
   */
  function createSolutionModal(puzzleContainerId) {
    const modal = document.createElement('div');
    modal.id = `solutionModal-${puzzleContainerId}`;
    modal.className = 'modal';
  
    modal.innerHTML = `
      <div class="modal-content">
        <span class="close">&times;</span>
        <pre><code id="fullCode-${puzzleContainerId}" class="python"></code></pre>
        <button id="copyCodeButton-${puzzleContainerId}">Copy Code</button>
      </div>
    `;
  
    document.body.appendChild(modal);
    return modal;
  }
  
/**
 * Splits the code into blocks separated by semicolons, preserves indentation, 
 * and shuffles the order while keeping blocks together.
 * @param {string} codeString - The full code as a string.
 * @returns {Array} - An array of objects containing the shuffled code blocks with their original order.
 */
function splitAndShuffleCode(codeString) {
    // Split into blocks by semicolons
    const codeBlocks = codeString.split(';').map(block => block.trim());

    // Further split each block by newlines if it's not a semicolon-separated block
    const codeLineObjects = codeBlocks.flatMap((block, index) => {
        const lines = block.split('\n').filter(line => line.trim() !== '');
        return lines.map((line, lineIndex) => ({
            line: line,
            order: index * 100 + lineIndex + 1 // Ensure blocks stay in order, lines within blocks are ordered too
        }));
    });

    return shuffleArray(codeLineObjects);
}

  /**
   * Shuffles an array of code line objects using the Fisher-Yates algorithm.
   * @param {Array} array - The array to shuffle.
   * @returns {Array} - The shuffled array.
   */
  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }
  
  /**
   * Renders the shuffled code lines as draggable elements within the specified container.
   * @param {HTMLElement} container - The container where the draggable elements will be placed.
   * @param {Array} codeLineObjects - The array of code line objects to render.
   */
  function renderDraggableCode(container, codeLineObjects) {
    container.innerHTML = '';  // Clear the container
    codeLineObjects.forEach((obj) => {
      const lineElement = document.createElement('div');
      lineElement.className = 'draggable';
      lineElement.draggable = true;
      lineElement.dataset.order = obj.order;  // The correct order, based on original code
      
      // Wrap the code in <pre> and <code> tags with the appropriate class for Python
      lineElement.innerHTML = `<pre class="highlight"><code>${escapeHTML(obj.line)}</code></pre>`;
      
      container.appendChild(lineElement);
      hljs.highlightElement(lineElement.querySelector('code')); // Highlight this code element
    });
  }
  
  function escapeHTML(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  
  /**
   * Creates a placeholder element that is always visible at the bottom of the drop area.
   * @param {HTMLElement} dropArea - The drop area where the placeholder will be placed.
   */
  function createPlaceholder(dropArea) {
    const placeholder = document.createElement('div');
    placeholder.className = 'placeholder';
    dropArea.appendChild(placeholder);
  }
  
  /**
   * Enables drag-and-drop functionality for the draggable elements and the drop area.
   * @param {HTMLElement} draggableContainer - The container holding the draggable elements.
   * @param {HTMLElement} dropArea - The area where elements can be dropped.
   */
  function enableDragAndDrop(draggableContainer, dropArea) {
    const draggables = draggableContainer.querySelectorAll('.draggable');
    const placeholder = dropArea.querySelector('.placeholder');
  
    draggables.forEach(draggable => {
      draggable.addEventListener('dragstart', dragStart);
      draggable.addEventListener('dragend', dragEnd); // Remove feedback when dragging ends
    });
  
    dropArea.addEventListener('dragover', (e) => dragOver(e, dropArea, placeholder));
    dropArea.addEventListener('drop', drop);
  }
  
  /**
   * Handles the drag start event by applying a feedback style.
   * @param {Event} e - The dragstart event.
   */
  function dragStart(e) {
    e.dataTransfer.setData('text/plain', e.target.dataset.order);
    e.target.classList.add('dragging');
    setTimeout(() => {
      e.target.style.display = 'none';
    }, 0); // Hide the element briefly while dragging
  }
  
  /**
   * Handles the drag end event by removing the feedback style.
   * @param {Event} e - The dragend event.
   */
  function dragEnd(e) {
    e.target.style.display = 'block';
    e.target.classList.remove('dragging');
  }
  
  /**
   * Handles the drag over event to allow dropping, and calculates where to insert the item.
   * @param {Event} e - The dragover event.
   * @param {HTMLElement} dropArea - The drop area where the elements will be dropped.
   * @param {HTMLElement} placeholder - The placeholder element in the drop area.
   */
  function dragOver(e, dropArea, placeholder) {
    e.preventDefault();
    const afterElement = getDragAfterElement(e.clientY, dropArea);
    const draggable = document.querySelector('.dragging');
    if (afterElement == null) {
      dropArea.insertBefore(draggable, placeholder);
    } else {
      dropArea.insertBefore(draggable, afterElement);
    }
  
    // Ensure the placeholder is always at the bottom by appending it again
    dropArea.appendChild(placeholder);
  }
  
  /**
   * Handles the drop event by moving the dragged element to the correct position.
   * @param {Event} e - The drop event.
   */
  function drop(e) {
    e.preventDefault();
    const draggableElement = document.querySelector('.dragging');
    const dropArea = e.target.closest('#drop-area');
    dropArea.insertBefore(draggableElement, dropArea.querySelector('.placeholder'));
    draggableElement.classList.remove('dragging');
  }
  
  /**
   * Gets the element that the dragged item should be placed after based on mouse position.
   * @param {number} y - The vertical position of the mouse.
   * @param {HTMLElement} dropArea - The drop area where the elements are being dropped.
   * @returns {HTMLElement} - The element that the dragged item should be placed after.
   */
  function getDragAfterElement(y, dropArea) {
    const draggableElements = [...dropArea.querySelectorAll('.draggable:not(.dragging)')];
  
    return draggableElements.reduce((closest, child) => {
      const box = child.getBoundingClientRect();
      const offset = y - box.top - box.height / 2;
      if (offset < 0 && offset > closest.offset) {
        return { offset: offset, element: child };
      } else {
        return closest;
      }
    }, { offset: Number.NEGATIVE_INFINITY }).element;
  }
  


  
  /**
   * Resets the puzzle to its initial state, randomizing the code lines again
   * and clearing the drop area and feedback.
   * @param {HTMLElement} draggableContainer - The container holding the draggable elements.
   * @param {HTMLElement} dropArea - The drop area where elements were dropped.
   * @param {string} codeString - The original code string to reset.
   * @param {HTMLElement} feedbackElement - The element displaying feedback.
   */
  function resetPuzzle(draggableContainer, dropArea, codeString, feedbackElement) {
    feedbackElement.textContent = '';  // Clear feedback
    dropArea.innerHTML = '';  // Clear the drop area
    const codeLines = splitAndShuffleCode(codeString);
    renderDraggableCode(draggableContainer, codeLines);
    createPlaceholder(dropArea);
    enableDragAndDrop(draggableContainer, dropArea);
  }
