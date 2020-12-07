// Document Object Model
// Check these for mouse events on dom: https://developer.mozilla.org/en-US/docs/Web/Events
var one = document.querySelector('#one')
var two = document.querySelector('#two')
var three = document.querySelector('#three')
var originalOneText = one.textContent
var originalOneColor = one.style.color
var originalTwoText = two.textContent
var originalTwoColor = two.style.color
var originalThreeText = three.textContent
var originalThreeColor = three.style.color

// Changes on one h1 element
// one.addEventListener('mouseover', () => {
//   one.textContent = "You are mouseovering me :)"
//   one.style.color = 'blue'
// })

// Test if jquery works
console.log($("#one").text());

// If you want to do this function using jQuery
// Note: jQuery takes function in normal way with function keyword in it
// Arrow notation of function does not work with jQuery!
$('#one').on('mouseenter', function() {
  $(this).text("You are mouseovering me :)");
  $(this).css("color", "red");
})

// BTW, below also worked for me, TODO: check out the difference!
// $('#one').mouseenter(function() {
//   $(this).text("You are mouseovering me :)");
//   $(this).css("color", "red");
// })

// one.addEventListener('mouseout', () => {
//   one.textContent = originalOneText
//   one.style.color = originalOneColor
// })

// If you want to redo this function using jQuery
$('#one').mouseleave(function() {
  $(this).text(originalOneText)
  $(this).css('color', originalOneColor)
})

// More of jQuery event handlers: https://api.jquery.com/category/events/

// Changes on two h1 element
two.addEventListener('click', () => {
  two.textContent = "I am being clicked!"
  two.style.color = 'purple'
})

two.addEventListener('mouseleave', () => {
  two.textContent = originalTwoText
  two.style.color = originalTwoColor
})

// Changes on three h1 element
three.addEventListener('dblclick', () => {
  three.textContent = "I am being double clicked!"
  three.style.color = 'yellow'
})

three.addEventListener('mouseleave', () => {
  three.textContent = originalThreeText
  three.style.color = originalThreeColor
})
