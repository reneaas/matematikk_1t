
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
  
    const solutionModal = createSolutionModal(puzzleContainerId);
    const fullCodeElement = solutionModal.querySelector(`#fullCode-${puzzleContainerId}`);
    const closeModalButton = solutionModal.querySelector('.close');
    const copyCodeButton = solutionModal.querySelector(`#copyCodeButton-${puzzleContainerId}`);

  
    // Preprocess and shuffle the code once, then keep it stored in a variable
    let codeBlocks = preprocessCode(codeString);
    let shuffledCodeBlocks = shuffleArray(codeBlocks.slice()); // Shuffle and store the shuffled order
  
    renderDraggableCode(draggableCodeContainer, shuffledCodeBlocks);
    createPlaceholder(dropArea);
    enableDragAndDrop(draggableCodeContainer, dropArea);

  
    checkButton.addEventListener('click', () => {
        checkSolution(dropArea, codeBlocks, feedback, fullCodeElement, solutionModal);
    });
  
    resetButton.addEventListener('click', () => {
        //resetPuzzle(draggableCodeContainer, dropArea, shuffledCodeBlocks, feedback);
        reset();
        reshuffle();
    });
  
    closeModalButton.addEventListener('click', () => {
        solutionModal.style.display = 'none';
    });
  
    copyCodeButton.addEventListener('click', () => {
        navigator.clipboard.writeText(fullCodeElement.textContent).then(() => {
            alert('Du har kopiert koden!');
        });
    });



}

/**
 * Resets the puzzle to its shuffled state, clearing the drop area and feedback.
 * @param {HTMLElement} draggableContainer - The container holding the draggable elements.
 * @param {HTMLElement} dropArea - The drop area where elements were dropped.
 * @param {Array} shuffledCodeBlocks - The shuffled code block objects to reset to.
 * @param {HTMLElement} feedbackElement - The element displaying feedback.
 */


function reset() {
    console.log('Reset function called');

    const dropArea = document.querySelector('#drop-area');
    const draggableCodeContainer = document.querySelector('#draggable-code');
    const originalShuffledOrder = Array.from(draggableCodeContainer.querySelectorAll('.draggable')); // Store original order or reshuffle as needed
    const feedbackElement = document.querySelector('#feedback');

    // Clear feedback text
    feedbackElement.textContent = '';  // Reset the text content of the feedback element

    if (!dropArea) {
        console.error('Drop area not found');
        return;
    }

    if (!draggableCodeContainer) {
        console.error('Draggable code container not found');
        return;
    }

    // Move all draggable elements back to the original container
    const draggableElements = dropArea.querySelectorAll('.draggable');
    draggableElements.forEach(element => {
        console.log(`Moving element ${element.id} back to draggable code container`);
        draggableCodeContainer.appendChild(element);
    });

    shuffleArray(originalShuffledOrder).forEach(element => {
        draggableCodeContainer.appendChild(element);
    });

    // Reset placeholder visibility
    const placeholder = dropArea.querySelector('.placeholder');
    if (placeholder) {
        console.log('Showing placeholder');
        placeholder.style.display = '';
    } else {
        placeholder = createPlaceholder(dropArea);
    }

    // Additional reset logic if any
    console.log('Reset function completed');
}

function reshuffle() {
    const draggableCodeContainer = document.querySelector('#draggable-code');
    const originalShuffledOrder = Array.from(draggableCodeContainer.querySelectorAll('.draggable')); // Store original order or reshuffle as needed

    shuffleArray(originalShuffledOrder).forEach(element => {
        draggableCodeContainer.appendChild(element);
    });
}



function preprocessCode(codeString) {
    const lines = codeString.split('\n');
    return lines.map((line, index) => {
        let trimmedLine = line.trim();

        if (line.includes(';')) {
            // Split the line at each semicolon, preserving empty parts
            const parts = line.split(';');
            
            // Join the parts with newlines, keeping the original indentation or empty lines
            trimmedLine = parts.map(part => part.trim() === '' ? '' : part).join('\n');
        }

        return {
            block: line.includes(';') ? trimmedLine : line,
            order: index,
            isEmpty: line.trim() === '' // Add an `isEmpty` property to track empty lines
        };
    });
}



function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}



function renderDraggableCode(container, codeBlockObjects) {
    container.innerHTML = '';  // Clear the container
    codeBlockObjects.forEach((obj) => {
        if (!obj.isEmpty) { // Skip rendering for empty lines
            const lineElement = document.createElement('div');
            lineElement.className = 'draggable';
            lineElement.draggable = true;
            lineElement.dataset.order = obj.order;
            
            lineElement.innerHTML = `<pre class="highlight python"><code>${escapeHTML(obj.block)}</code></pre>`;
            
            container.appendChild(lineElement);
            hljs.highlightElement(lineElement.querySelector('code'));
        }
    });
}


function escapeHTML(str) {
    return str.replace(/&/g, "&amp;")
              .replace(/</g, "&lt;")
              .replace(/>/g, "&gt;")
              .replace(/"/g, "&quot;")
              .replace(/'/g, "&#039;");
}


function checkSolution(dropArea, codeBlockObjects, feedbackElement, fullCodeElement, solutionModal) {
    const droppedItems = Array.from(dropArea.children).filter(item => !item.classList.contains('placeholder'));
    const droppedOrder = droppedItems.map(item => parseInt(item.dataset.order));

    // Combine all code blocks based on their order to form the full code, including empty lines
    const fullCode = codeBlockObjects.sort((a, b) => a.order - b.order)
                         .map(obj => obj.block)
                         .join('\n');
    
    fullCodeElement.textContent = fullCode;
    hljs.highlightElement(fullCodeElement);

    // Solution correctness check remains unchanged
    const correctOrder = codeBlockObjects.filter(obj => !obj.isEmpty)
                                         .sort((a, b) => a.order - b.order)
                                         .map(obj => obj.order);
    if (JSON.stringify(droppedOrder) === JSON.stringify(correctOrder)) {
        feedbackElement.textContent = 'Riktig!';
        feedbackElement.style.color = 'green';
        solutionModal.style.display = 'block';
    } else {
        feedbackElement.textContent = 'Prøv igjen!';
        feedbackElement.style.color = 'red';
    }
}



function createSolutionModal(puzzleContainerId) {
    const modal = document.createElement('div');
    modal.id = `solutionModal-${puzzleContainerId}`;
    modal.className = 'modal';
  
    modal.innerHTML = `
      <div class="modal-content">
        <span class="close">&times;</span>
        <pre><code id="fullCode-${puzzleContainerId}" class="highlight python"></code></pre>
        <button id="copyCodeButton-${puzzleContainerId}" class="button button-check-solution">Bra jobba! 🔥 Kopier koden!</button>
      </div>
    `;
  
    document.body.appendChild(modal);
    return modal;
}


function createPlaceholder(dropArea) {
    // Always start fresh
    const placeholder = document.createElement('div');
    placeholder.className = 'placeholder';
    placeholder.textContent = 'Dra og dropp kode her!';
    dropArea.appendChild(placeholder);
}


function enableDragAndDrop(draggableContainer, dropArea) {
    const draggables = draggableContainer.querySelectorAll('.draggable');
    const placeholder = dropArea.querySelector('.placeholder');

    draggables.forEach(draggable => {
        draggable.addEventListener('dragstart', dragStart);
        draggable.addEventListener('dragend', dragEnd);
    });

    // Adding event listeners for drag and drop operations to both areas
    [dropArea, draggableContainer].forEach(container => {
        container.addEventListener('dragover', (e) => dragOver(e, container));
        container.addEventListener('drop', (e) => drop(e, container, dropArea, placeholder));
    });
}

function dragStart(e) {
    e.dataTransfer.setData('text/plain', e.target.dataset.order);
    e.target.classList.add('dragging');
    setTimeout(() => {
        e.target.style.display = 'none';
    }, 0); // Hide the element briefly while dragging
}

function dragEnd(e) {
    e.target.style.display = 'block';
    e.target.classList.remove('dragging');
}



function dragOver(e, dropArea, placeholder) {
    e.preventDefault();
    const draggable = document.querySelector('.dragging');
    const afterElement = getDragAfterElement(e.clientY, dropArea);

    if (afterElement == null) {
        dropArea.insertBefore(draggable, placeholder);
    } else {
        const box = afterElement.getBoundingClientRect();
        const offset = e.clientY - box.top;

        // If the mouse is in the upper half of the element, place the draggable above it
        if (offset < box.height / 2) {
            dropArea.insertBefore(draggable, afterElement);
        } else {
            dropArea.insertBefore(draggable, afterElement.nextSibling);
        }
    }

    // Always move the placeholder to the end
    dropArea.appendChild(placeholder);
}

function drop(e) {
    e.preventDefault();
    const draggableElement = document.querySelector('.dragging');
    const dropArea = e.target.closest('#drop-area') || e.target.closest('#draggable-code');
    const afterElement = getDragAfterElement(e.clientY, dropArea);
    const placeholder = dropArea.querySelector('.placeholder');

    if (afterElement == null) {
        dropArea.insertBefore(draggableElement, placeholder);
    } else {
        const box = afterElement.getBoundingClientRect();
        const offset = e.clientY - box.top;

        // If the mouse is in the upper half of the element, place the draggable above it
        if (offset < box.height / 2) {
            dropArea.insertBefore(draggableElement, afterElement);
        } else {
            dropArea.insertBefore(draggableElement, afterElement.nextSibling);
        }
    }

    draggableElement.classList.remove('dragging');

    // Always move the placeholder to the end
    dropArea.appendChild(placeholder);

    // Pass the draggableCodeContainer reference correctly
    const draggableCodeContainer = document.querySelector('#draggable-code');
    updatePlaceholderVisibility(dropArea, draggableCodeContainer);
}

function ensurePlaceholderAtBottom(dropArea, placeholder) {
    if (!dropArea.contains(placeholder)) {
        dropArea.appendChild(placeholder); // Append placeholder if it's not in the drop area
    }
}

function updatePlaceholderVisibility(dropArea, draggableCodeContainer) {
    const draggableItems = draggableCodeContainer.querySelectorAll('.draggable').length;
    console.log("draggableItems: ", draggableItems);
    // If all draggable elements are in the drop area, remove the placeholder
    if (draggableItems === 0) {
        const placeholder = dropArea.querySelector('.placeholder');
        if (placeholder) {
            placeholder.remove();
        }        
    } else {
        // Ensure placeholder is visible and at the end of the drop area
        const placeholder = dropArea.querySelector('.placeholder');
        if (placeholder) {
            dropArea.appendChild(placeholder);
        } else {
            createPlaceholder(dropArea);  // Recreate the placeholder if it was removed somehow
        }
    }
}


function getDragAfterElement(y, dropArea) {
    const draggableElements = [...dropArea.querySelectorAll('.draggable:not(.dragging)')];
    
    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const offset = y - box.top - box.height / 2;  // Get the middle point

        if (offset < 0 && offset > closest.offset) {
            return { offset: offset, element: child };
        } else {
            return closest;
        }
    }, { offset: Number.NEGATIVE_INFINITY }).element;  // Return element before which the new block will be inserted
}