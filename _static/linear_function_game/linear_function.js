class Graph {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;
        this.width = canvas.width;
        this.height = canvas.height;
        this.centerX = this.width / 2;
        this.centerY = this.height / 2;
        this.scale = 40; // scaling factor for the graph units
    }

    // Draw grid and axes
    drawGrid() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        this.ctx.beginPath();
        this.ctx.strokeStyle = "#ddd";
        this.ctx.lineWidth = 1;

        for (let x = 0; x <= this.width; x += this.scale) {
            this.ctx.moveTo(x, 0);
            this.ctx.lineTo(x, this.height);
        }

        for (let y = 0; y <= this.height; y += this.scale) {
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(this.width, y);
        }

        this.ctx.stroke();
        this.ctx.closePath();

        // Draw x and y axes
        this.ctx.beginPath();
        this.ctx.strokeStyle = "black";
        this.ctx.lineWidth = 2;

        // X axis
        this.ctx.moveTo(0, this.centerY);
        this.ctx.lineTo(this.width, this.centerY);

        // Y axis
        this.ctx.moveTo(this.centerX, 0);
        this.ctx.lineTo(this.centerX, this.height);

        this.ctx.stroke();
        this.ctx.closePath();
    }

    // Plot a point
    plotPoint(x, y, color = "red") {
        this.ctx.beginPath();
        this.ctx.arc(this.centerX + x * this.scale, this.centerY - y * this.scale, 5, 0, Math.PI * 2);
        this.ctx.fillStyle = color;
        this.ctx.fill();
        this.ctx.closePath();
    }

    // Draw a line for a given linear equation y = ax + b
    drawLine(a, b) {
        this.ctx.beginPath();
        this.ctx.strokeStyle = "blue";
        this.ctx.lineWidth = 2;

        let x1 = -this.centerX / this.scale;
        let y1 = a * x1 + b;
        let x2 = (this.width - this.centerX) / this.scale;
        let y2 = a * x2 + b;

        this.ctx.moveTo(this.centerX + x1 * this.scale, this.centerY - y1 * this.scale);
        this.ctx.lineTo(this.centerX + x2 * this.scale, this.centerY - y2 * this.scale);

        this.ctx.stroke();
        this.ctx.closePath();
    }
}

class DraggableNode {
    constructor(x, y, graph) {
        this.x = x;
        this.y = y;
        this.radius = 10;
        this.dragging = false;
        this.graph = graph;

        this.initDrag();
    }

    initDrag() {
        const canvas = this.graph.canvas;

        canvas.addEventListener('mousedown', (e) => {
            const mousePos = this.getMousePos(canvas, e);
            if (this.isMouseInNode(mousePos)) {
                this.dragging = true;
            }
        });

        canvas.addEventListener('mouseup', () => {
            this.dragging = false;
        });

        canvas.addEventListener('mousemove', (e) => {
            if (this.dragging) {
                const mousePos = this.getMousePos(canvas, e);
                this.x = (mousePos.x - this.graph.centerX) / this.graph.scale;
                this.y = (this.graph.centerY - mousePos.y) / this.graph.scale;
                this.graph.drawGrid();
                this.graph.plotPoint(this.x, this.y, "red");
            }
        });
    }

    getMousePos(canvas, event) {
        const rect = canvas.getBoundingClientRect();
        return {
            x: event.clientX - rect.left,
            y: event.clientY - rect.top
        };
    }

    isMouseInNode(mousePos) {
        const dx = mousePos.x - (this.graph.centerX + this.x * this.graph.scale);
        const dy = mousePos.y - (this.graph.centerY - this.y * this.graph.scale);
        return dx * dx + dy * dy <= this.radius * this.radius;
    }
}

class LinearGraph {
    constructor(a, b, graph) {
        this.a = a; // slope
        this.b = b; // y-intercept
        this.graph = graph;
        this.node = new DraggableNode(0, b, graph); // start at the y-intercept

        this.setup();
    }

    setup() {
        this.graph.drawGrid();
        this.graph.drawLine(this.a, this.b);
        this.graph.plotPoint(this.node.x, this.node.y, "red");

        const checkButton = document.getElementById('checkSolution');
        checkButton.addEventListener('click', () => this.checkSolution());
    }

    checkSolution() {
        const expectedSlope = this.a;
        const actualSlope = (this.node.y - this.b) / this.node.x;

        if (Math.abs(expectedSlope - actualSlope) < 0.01) {
            document.getElementById('feedback').innerText = "Correct!";
        } else {
            document.getElementById('feedback').innerText = "Try again.";
        }
    }
}

// Instantiate the game
const canvas = document.getElementById('graphCanvas');
const ctx = canvas.getContext('2d');
const graph = new Graph(canvas, ctx);
const puzzle = new LinearGraph(3, -4, graph); // Puzzle for f(x) = 3x - 4
