document.addEventListener("DOMContentLoaded", function () {
    ymaps.ready(init);

    function init() {
        var map = new ymaps.Map("yandex-map", {
            center: [53.7200, 91.4296],
            zoom: 7,
            controls: ['zoomControl', 'fullscreenControl']
        });

        // Загружаем точки из скрытого JSON
        var points = JSON.parse(document.getElementById('delivery-points-data').textContent || '[]');
        console.log(points);

        points.forEach(function(p) {
            var placemark = new ymaps.Placemark(
                [p.latitude, p.longitude],
                {
                    balloonContent: `<strong>${p.name}</strong><br>${p.description || 'Зона доставки активна'}`
                },
                { preset: 'islands#redIcon' }
            );
            map.geoObjects.add(placemark);
        });

        if (map.geoObjects.getLength()) {
            map.setBounds(map.geoObjects.getBounds(), { checkZoomRange: true, zoomMargin: 20 });
        }
    }
});