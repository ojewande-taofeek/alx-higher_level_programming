$('div#toggle_header').click(() => {
  if ($('header').hasClass('red')) {
    $('header').toggleClass('green');
  } else {
    $('header').toggleClass('red');
  }
});
