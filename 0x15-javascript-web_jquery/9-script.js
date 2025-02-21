$(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, (data) => {
    $('div#hello').text(data.hello);
  });
});
