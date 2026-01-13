document.addEventListener('DOMContentLoaded', () => {
    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
            navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
        } else {
            navbar.style.background = 'rgba(10, 10, 10, 0.8)';
            navbar.style.boxShadow = 'none';
        }
    });

    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('toggle');
        });
    }

    // Smooth Scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                if (navLinks.classList.contains('active')) {
                    navLinks.classList.remove('active');
                    hamburger.classList.remove('toggle');
                }
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });

    // Intersection Observer for Fade In
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');

                // Animate progress bars if within this section
                if (entry.target.querySelector('.progress-line')) {
                    const progressLines = entry.target.querySelectorAll('.progress-line');
                    progressLines.forEach(line => {
                        const width = line.getAttribute('data-width');
                        line.querySelector('span').style.width = width;
                    });
                }

                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.section-title, .capability-card, .project-card, .skill-group, .timeline-item').forEach(el => {
        el.classList.add('hidden');
        observer.observe(el);
    });

    // Typing Effect for Title
    const titleElement = document.querySelector('.typing-effect');
    if (titleElement) {
        const text = titleElement.textContent;
        titleElement.textContent = '';
        let i = 0;

        function typeWriter() {
            if (i < text.length) {
                titleElement.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        }

        // Start typing after a small delay
        setTimeout(typeWriter, 1000);
    }

    // Cursor Trail Effect
    const cursorTrail = document.getElementById('cursor-trail');
    let lastX = 0;
    let lastY = 0;
    let particleCount = 0;
    const maxParticles = 30;

    document.addEventListener('mousemove', (e) => {
        const dx = e.clientX - lastX;
        const dy = e.clientY - lastY;
        const distance = Math.sqrt(dx * dx + dy * dy);

        // Only create particles if mouse moved significantly
        if (distance > 10 && particleCount < maxParticles) {
            const particle = document.createElement('div');
            particle.className = 'cursor-particle';
            particle.style.left = e.clientX + 'px';
            particle.style.top = e.clientY + 'px';
            cursorTrail.appendChild(particle);
            particleCount++;

            setTimeout(() => {
                particle.remove();
                particleCount--;
            }, 1000);
        }

        lastX = e.clientX;
        lastY = e.clientY;
    });
});
