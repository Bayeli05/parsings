function copyAndChangeText() {
  var originalText = "490987";
  var outputElement = document.getElementById("myText");

  // Копирование текста
  navigator.clipboard.writeText(originalText)
    .then(function() {
      console.log("Текст скопирован в буфер обмена: " + originalText);

      // Изменение текста кнопки на "Copy"
      outputElement.textContent = "Copy";

      // Возврат исходного текста через 3 секунды
      setTimeout(function() {
        outputElement.textContent = originalText;
      }, 1700);
    })
    .catch(function(error) {
      console.error("Ошибка при копировании текста: ", error);
    });
}





function toggleBlock(blockId) {
  const block = document.getElementById(blockId);
  const openContent = block.querySelector('.open-content');

  block.classList.toggle('open');
  openContent.style.display = block.classList.contains('open') ? 'block' : 'none';
}

// Добавляем прослушиватели событий ко всем блокам
const blocks = document.querySelectorAll('.block');
blocks.forEach((block) => {
  const blockId = block.id;
  const blockWay = block.querySelector('.block__Way');
  blockWay.addEventListener('click', function() {
    toggleBlock(blockId);
  });
});

  
  function copyText(element) {
    var textElement = element.parentNode.querySelector("span");
    var text = textElement.textContent;
  
    navigator.clipboard.writeText(text)
      .then(function() {
        console.log("Текст скопирован в буфер обмена: " + text);
      })
      .catch(function(error) {
        console.error("Ошибка при копировании текста: ", error);
      });
  }
  


  let menuBtn = document.querySelector('.menu-btn');
  let menu = document.querySelector('.menu');
  let headerRightContent = document.querySelector('.header__right-content');
  
  menuBtn.addEventListener('click', function() {
      menuBtn.classList.toggle('active');
      menu.classList.toggle('active');
      headerRightContent.classList.toggle('active');
  });
  