document.addEventListener('DOMContentLoaded', (event) => {
    const codeBlocks = document.querySelectorAll('.highlight .c');
    codeBlocks.forEach(block => {
        if (block.textContent.includes('TODO')) {
            block.style.color = '#f85149';
            block.style.fontWeight = 'bold';
        }
    });
});