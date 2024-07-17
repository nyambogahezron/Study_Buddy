// Menu

const dropdownMenu = document.querySelector('.dropdown-menu');
const dropdownButton = document.querySelector('.dropdown-button');

if (dropdownButton) {
  dropdownButton.addEventListener('click', () => {
    dropdownMenu.classList.toggle('show');
  });
}

// Upload Image
const photoInput = document.querySelector('#avatar');
const photoPreview = document.querySelector('#preview-avatar');
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector('.room__box');
if (conversationThread)
  conversationThread.scrollTop = conversationThread.scrollHeight;

// theme
let buttons = document.querySelectorAll('.bg-1, .bg-2, .bg-3');

buttons.forEach((button) => {
  button.addEventListener('click', function () {
    // Get the theme name from the h5 element inside the clicked div.
    let theme = this.querySelector('h5').textContent.toLowerCase();

    // Remove the "active" class from all buttons.
    buttons.forEach((btn) => btn.classList.remove('active'));

    // Add the "active" class to the clicked button.
    this.classList.add('active');

    // Remove the previous theme class from the HTML root element.
    let previousTheme = localStorage.getItem('theme');
    if (previousTheme) {
      document.documentElement.classList.remove(previousTheme);
    }

    // Add the new theme class to the HTML root element.
    document.documentElement.classList.add(theme);

    // Save the theme name in the local storage.
    localStorage.setItem('theme', theme);
  });
});

// On page load, get the theme from local storage and set it in the HTML root.
let theme = localStorage.getItem('theme') || 'light';
document.documentElement.className = theme;

let colorButtons = document.querySelectorAll(
  '.color-1, .color-2, .color-3, .color-4, .color-5'
);

colorButtons.forEach((button) => {
  button.addEventListener('click', function () {
    // Get the color name from the class of the clicked span.
    let color = this.className.split(' ')[0];

    // Remove the "active" class from all color buttons.
    colorButtons.forEach((btn) => btn.classList.remove('active'));

    // Add the "active" class to the clicked color button.
    this.classList.add('active');

    // Remove the previous color class from the HTML root element.
    let previousColor = localStorage.getItem('color');
    if (previousColor) {
      document.documentElement.classList.remove(previousColor);
    }

    // Add the new color class to the HTML root element.
    document.documentElement.classList.add(color);

    // Save the color name in the local storage.
    localStorage.setItem('color', color);
  });
});

// On page load, get the color from local storage and set it in the HTML root.
let color = localStorage.getItem('color') || 'color-1';
document.documentElement.classList.add(color);
