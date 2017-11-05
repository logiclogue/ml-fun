(function() {
    var canvas = document.querySelector('#paint');
    var button = document.querySelector('#button');
    var ctx = canvas.getContext('2d');

    button.addEventListener('click', function () {
        let data = ctx.getImageData(0, 0, 28, 28).data;
        let output = [];

        for (let i = 0; i < data.length; i += 4) {
            output.push(data[i + 2] == 0 ? 0 : 1);
        }

        axios.post('/result', output).then(function (response) {
            console.log("Result: ", response.data);
        });
    });

    var sketch = document.querySelector('#sketch');
    var sketch_style = getComputedStyle(sketch);

    canvas.width = parseInt(sketch_style.getPropertyValue('width'));
    canvas.height = parseInt(sketch_style.getPropertyValue('height'));

    var mouse = {x: 0, y: 0};
    var last_mouse = {x: 0, y: 0};

    /* Mouse Capturing Work */
    canvas.addEventListener('mousemove', function(e) {
        last_mouse.x = mouse.x;
        last_mouse.y = mouse.y;

        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
    }, false);

    /* Drawing on Paint App */
    ctx.lineWidth = 1;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'blue';

    canvas.addEventListener('mousedown', function(e) {
        canvas.addEventListener('mousemove', onPaint, false);
    }, false);

    canvas.addEventListener('mouseup', function() {
        canvas.removeEventListener('mousemove', onPaint, false);
    }, false);

    var onPaint = function() {
        ctx.beginPath();
        ctx.moveTo(last_mouse.x, last_mouse.y);
        ctx.lineTo(mouse.x, mouse.y);
        ctx.closePath();
        ctx.stroke();
    };
}());
