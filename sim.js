class BlackHole {
    constructor(canvas, centerX, centerY, mass, color) {
        this.canvas = canvas;
        this.ctx = canvas.getContext("2d");
        this.centerX = centerX;
        this.centerY = centerY;
        this.mass = mass;
        this.color = color;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, this.mass, 0, 2 * Math.PI);
        this.ctx.fillStyle = this.color;
        this.ctx.fill();
    }
}
