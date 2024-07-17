// document.addEventListener('DOMContentLoaded', (event) => {
//     const codeBlocks = document.querySelectorAll('.highlight .c');
//     codeBlocks.forEach(block => {
//         if (block.textContent.includes('TODO')) {
//             block.style.color = '#f85149';
//             block.style.fontWeight = 'bold';
//         }
//     });
// });

// custom.js

document.addEventListener("DOMContentLoaded", function() {
    // Select all code blocks
    const codeBlocks = document.querySelectorAll('.highlight .c1');

    codeBlocks.forEach(function(block) {
        // Check if the comment starts with "# TODO"
        if (block.textContent.trim().startsWith('# TODO')) {
            block.style.color = '#ff7b72'; // Red color for TODO comments
            block.style.fontWeight = 'bold';
        }
    });
});