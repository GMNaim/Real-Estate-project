const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// for remove the message automatically after 3 seconds
setTimeout(function () {
   $('#message').fadeOut('slow');
}, 9000);