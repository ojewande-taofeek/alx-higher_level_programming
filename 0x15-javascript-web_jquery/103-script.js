$(() => {
  const translation = () => {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
    const lang = $('input#language_code').val().trim();
    const endpoint = `${url}${lang}`;
    $.get(endpoint, (data) => {
      $('div#hello').text(data.hello);
    }
    );
  };
// Keypress of Enter in the language input
  $('input#language_code').bind('keypress', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      translation();
    }
  });

  // When the translate button is clicked
  $('input#btn_translate').click(() => translation());
});
