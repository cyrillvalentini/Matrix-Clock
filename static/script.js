document.addEventListener('DOMContentLoaded', () => {
    const matrix = document.getElementById('led-matrix');
    const colorPicker = document.getElementById('color-picker');
    const exportBtn = document.getElementById('export-btn');
    const downloadBtn = document.getElementById('download-btn');
    const uploadInput = document.getElementById('upload-input');
    const uploadBtn = document.getElementById('upload-btn');
    const modeSelect = document.getElementById('mode-select');
    const modeDialog = document.getElementById('mode-dialog');
    const closeModal = document.querySelector('.close');
    const confirmWhole = document.getElementById('confirm-whole');
    const confirmClock = document.getElementById('confirm-clock');
    const autoBrightnessBtn = document.getElementById('auto-brightness-btn');
    const manualBrightnessInput = document.getElementById('manual-brightness-input');
    const manualBrightnessBtn = document.getElementById('manual-brightness-btn');
    const standardColors = document.querySelectorAll('.standard-color');

    const rows = 8;
    const cols = 32;
    let ledArray = [];
    let uploadedMode = '';


    

standardColors.forEach(color => {
    color.addEventListener('click', () => {
        const colorValue = color.style.backgroundColor;
        colorPicker.value = rgbToHex(colorValue);
    });
});
    

autoBrightnessBtn.addEventListener('click', () => {
    sendBrightness(101);
});

manualBrightnessBtn.addEventListener('click', () => {
    const brightness = parseInt(manualBrightnessInput.value);
    if (!isNaN(brightness) && brightness >= 0 && brightness <= 100) {
        sendBrightness(brightness);
    } else {
        alert('Bitte geben Sie einen gültigen Helligkeitswert zwischen 0 und 100 ein.');
    }
});

function rgbToHex(rgb) {
    const [r, g, b] = rgb.match(/\d+/g);
    return "#" + ((1 << 24) + (parseInt(r) << 16) + (parseInt(g) << 8) + parseInt(b)).toString(16).slice(1);
}


function sendBrightness(brightness) {
    fetch('/api/brightness', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ brightness: brightness })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

    function createLedMatrix() {
        matrix.innerHTML = ''; // Clear existing matrix
        ledArray = [];
        for (let i = 0; i < rows; i++) {
            const row = [];
            for (let j = 0; j < cols; j++) {
                const led = document.createElement('div');
                led.classList.add('led');
                if (modeSelect.value === 'clock' && i >= 1 && i <= 6 && j >= 5 && j <= 26) {
                    led.classList.add('disabled');
                    row[j] = [0, 0, 0]; // Black color
                } else {
                    led.addEventListener('click', () => {
                        const color = colorPicker.value;
                        led.style.backgroundColor = color;
                        const rgbColor = hexToRgb(color);
                        row[j] = rgbColor;
                    });
                    row[j] = [0, 0, 0]; // Default black
                }
                matrix.appendChild(led);
            }
            ledArray.push(row);
        }
    }

    modeSelect.addEventListener('change', createLedMatrix);

    exportBtn.addEventListener('click', () => {
        const rgbValues = JSON.stringify(ledArray);
        sendRgbValues(rgbValues, modeSelect.value);
    });

    downloadBtn.addEventListener('click', () => {
        const rgbValues = JSON.stringify(ledArray);
        downloadJson(rgbValues, 'Matrix_Clock_config.json');
    });

    uploadBtn.addEventListener('click', () => {
        uploadInput.click();
    });

    uploadInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const content = e.target.result;
                ledArray = JSON.parse(content);
                showModeDialog();
            };
            reader.readAsText(file);
        }
    });

    confirmWhole.addEventListener('click', () => {
        uploadedMode = 'whole';
        modeSelect.value = 'whole';
        renderLedMatrix();
        closeModalDialog();
    });

    confirmClock.addEventListener('click', () => {
        uploadedMode = 'clock';
        modeSelect.value = 'clock';
        renderLedMatrix();
        closeModalDialog();
    });

    closeModal.addEventListener('click', closeModalDialog);

    function showModeDialog() {
        modeDialog.style.display = 'block';
    }

    function closeModalDialog() {
        modeDialog.style.display = 'none';
    }

    function hexToRgb(hex) {
        const bigint = parseInt(hex.slice(1), 16);
        const r = (bigint >> 16) & 255;
        const g = (bigint >> 8) & 255;
        const b = bigint & 255;
        return [r, g, b];
    }

    function sendRgbValues(rgbValues, mode) {
        const endpoint = mode === 'whole' ? '/api/rgb-image' : '/api/rgb-clock';
        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: rgbValues
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    }

    function downloadJson(content, fileName) {
        const a = document.createElement('a');
        const file = new Blob([content], { type: 'application/json' });
        a.href = URL.createObjectURL(file);
        a.download = fileName;
        a.click();
        URL.revokeObjectURL(a.href);
    }

    function renderLedMatrix() {
        matrix.innerHTML = ''; // Clear existing matrix
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                const led = document.createElement('div');
                led.classList.add('led');
                const [r, g, b] = ledArray[i][j];
                led.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
                if (uploadedMode === 'clock' && i >= 1 && i <= 6 && j >= 5 && j <= 26) {
                    led.classList.add('disabled');
                }
                matrix.appendChild(led);
            }
        }
    }

    createLedMatrix(); // Initial matrix creation
});
