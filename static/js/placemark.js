ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [55.6886, 37.8658],
            zoom: 14
        });

    myMap.geoObjects
        .add(new ymaps.Placemark([55.688604, 37.865890], {
            balloonContent: 'Школа StartIT'
        }));
}
