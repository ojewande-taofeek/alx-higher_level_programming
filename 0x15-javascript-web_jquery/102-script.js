$(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('input#btn_translate').click(() => {
    const lang = $('input#language_code').val();
    const endpoint = `${url}${lang}`;
    $.get(endpoint, (data) => {
      $('div#hello').text(data.hello);
    }
    );
  });
});
