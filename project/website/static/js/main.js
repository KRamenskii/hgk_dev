// Main JavaScript file for HGK website

document.addEventListener('DOMContentLoaded', function() {
    // Header scroll effect for transparent header
    const header = document.getElementById('header');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            header.classList.remove('header--transparent');
            header.classList.add('header--scrolled');
        } else {
            header.classList.remove('header--scrolled');
            header.classList.add('header--transparent');
        }
        
        lastScrollTop = scrollTop;
    });

    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                // Учитываем высоту фиксированной шапки
                const headerHeight = header.offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    const animatedElements = document.querySelectorAll('.service-card, .advantage-card, .contact-card, .achievement-card, .coverage-stat-card, .employee-card, .city-card');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Button click effects
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Create ripple effect
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Statistics counter animation
    const statNumbers = document.querySelectorAll('.stat__number, .achievement-card__number, .coverage-stat-card__number');
    const statsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statNumbers.forEach(stat => {
        statsObserver.observe(stat);
    });

    // Mobile menu toggle (if needed)
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function() {
            const nav = document.querySelector('.header__nav');
            nav.classList.toggle('active');
            this.classList.toggle('active');
        });
    }

    // Lazy loading for images (if any)
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
});

// Global functions
function openContactModal(requestType) {
    // Здесь можно открыть модальное окно с формой
    // Пока что просто показываем уведомление
    showNotification(`Открываем форму для: ${getRequestTypeText(requestType)}`);
}

function getRequestTypeText(type) {
    const types = {
        'call': 'Заказать звонок',
        'consultation': 'Получить консультацию',
        'delivery': 'Заказать доставку'
    };
    return types[type] || 'Обратной связи';
}

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: var(--primary-color);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        z-index: 1000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
        word-wrap: break-word;
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (document.body.contains(notification)) {
                document.body.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

function animateCounter(element) {
    const target = parseInt(element.textContent.replace(/\D/g, ''));
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;
    
    const timer = setInterval(() => {
        current += step;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        
        const suffix = element.textContent.replace(/\d/g, '');
        element.textContent = Math.floor(current) + suffix;
    }, 16);
}

// Add CSS for ripple effect and notifications
const style = document.createElement('style');
style.textContent = `
    .btn {
        position: relative;
        overflow: hidden;
    }
    
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .notification {
        animation: slideIn 0.3s ease;
    }
    
    @keyframes slideIn {
        from {
            transform: translateX(100%);
        }
        to {
            transform: translateX(0);
        }
    }
    
    /* Adjust body padding for fixed header */
    body {
        padding-top: 80px;
    }
    
    /* Hero section adjustments */
    .hero {
        padding-top: calc(6rem + 80px);
    }
`;
document.head.appendChild(style);


document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menuToggle");
    const mobileMenu = document.getElementById("mobileMenu");

    menuToggle.addEventListener("click", function () {
        mobileMenu.classList.toggle("active");

        // Меняем иконку: ☰ → ✖
        const icon = menuToggle.querySelector("i");
        if (mobileMenu.classList.contains("active")) {
            icon.classList.remove("bi-list");
            icon.classList.add("bi-x");
        } else {
            icon.classList.remove("bi-x");
            icon.classList.add("bi-list");
        }
    });
});


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


document.addEventListener("DOMContentLoaded", () => {
    const isMobile = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);

    document.querySelectorAll(".contact-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const type = btn.dataset.type;
            const value = btn.dataset.value;

            if (type === "call") {
                if (isMobile) {
                    window.location.href = `tel:${value}`;
                } else {
                    window.location.href = `skype:${value.replace(/\D/g, "")}?call`;
                }
            }

            if (type === "whatsapp") {
                const num = value.replace(/\D/g, "");
                if (isMobile) {
                    window.location.href = `https://wa.me/${num}`;
                } else {
                    window.open(`https://web.whatsapp.com/send?phone=${num}`, "_blank");
                }
            }

            if (type === "email") {
                window.location.href = `mailto:${value}`;
            }

            if (type === "map") {
                if (isMobile) {
                    // Для мобильных открываем 2ГИС
                    window.location.href = `dgis://2gis.ru/search/${encodeURIComponent(value)}`;
                } else {
                    // Для десктопа открываем 2ГИС в браузере
                    window.open(`https://2gis.ru/search/${encodeURIComponent(value)}`, "_blank");
                }
            }
        });
    });
});