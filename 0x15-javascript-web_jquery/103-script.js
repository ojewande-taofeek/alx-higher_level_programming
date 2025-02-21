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

  $('input#language_code').bind('keypress', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      translation();
    }
  });

  $('input#btn_translate').click(() => translation());
});
