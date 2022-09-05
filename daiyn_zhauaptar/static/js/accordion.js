// var accordion = (function (element) {
//     var _getItem = function (elements, className) { // функция для получения элемента с указанным классом
//       var element = undefined;
//       elements.forEach(function (item) {
//         if (item.classList.contains(className)) {
//           element = item;
//         }
//       });
//       return element;
//     };
//     return function () {
//       var _mainElement = {}, // .accordion
//         _items = {}, // .accordion-item
//         _contents = {}; // .accordion-item-content
//       var _actionClick = function (e) {
//         if (!e.target.classList.contains('accordion-item-header')) { // прекращаем выполнение функции если кликнули не по заголовку
//           return;
//         }
//         e.preventDefault(); // отменям стандартное действие
//         // получаем необходимые данные
//         var header = e.target,
//           item = header.parentElement,
//           itemActive = _getItem(_items, 'show');
//         if (itemActive === undefined) { // добавляем класс show к элементу (в зависимости от выбранного заголовка)
//           item.classList.add('show');
//         } else {
//           // удаляем класс show у ткущего элемента
//           itemActive.classList.remove('show');
//           // если следующая вкладка не равна активной
//           if (itemActive !== item) {
//             // добавляем класс show к элементу (в зависимости от выбранного заголовка)
//             item.classList.add('show');
//           }
//         }
//       },
//       _setupListeners = function () {
//         // добавим к элементу аккордиона обработчик события click
//         _mainElement.addEventListener('click', _actionClick);
//       };
  
//       return {
//         init: function (element) {
//           _mainElement = (typeof element === 'string' ? document.querySelector(element) : element);
//           _items = _mainElement.querySelectorAll('.accordion-item');
//           _setupListeners();
//         }
//       }
//     }
//   })();
//   var accordion1 = accordion();
//   accordion1.init('#accordion');  


  $(".accordion-item").click(function () {
    $(this).toggleClass("show");
});


  $(function() {
	var tab = $('.tabs .tabs-items > div'); 
	tab.hide().filter('').show(); 
	
	// Клики по вкладкам.
	$('.tabs .tabs-nav a').click(function(){
		tab.hide(); 
		tab.filter(this.hash).show(); 
		$('.tabs .tabs-nav a').removeClass('active');
		$(this).addClass('active');
		return false;
	}).filter('').click();
 
	// Клики по якорным ссылкам.
	$('.tabs-target').click(function(){
		$('.tabs .tabs-nav a[href=' + $(this).attr('href')+ ']').click();
	});
	
	// Отрытие вкладки из хеша URL
	if(window.location.hash){
		$('.tabs-nav a[href=' + window.location.hash + ']').click();
		window.scrollTo(0, $("#" . window.location.hash).offset().top);
	}
});