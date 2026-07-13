// ===== NAVBAR SCROLL =====
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// ===== HAMBURGER MENU =====
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');
hamburger.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
});
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
  });
});

// ===== SMOOTH SCROLL for all anchor links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    if (href === '#' || href.length < 2) return;
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      const offset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// ===== INTERSECTION OBSERVER — FADE UP =====
const fadeEls = document.querySelectorAll(
  '.service-card, .testimonial-card, .pillar, .about-grid, .contact-grid, .price-card, .faq-item, .gallery-item, .schedule-wrap'
);
fadeEls.forEach(el => el.classList.add('fade-up'));

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), (i % 6) * 70);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

fadeEls.forEach(el => observer.observe(el));

// ===== FAQ ACCORDION =====
document.querySelectorAll('.faq-question').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const answer = item.querySelector('.faq-answer');
    const isActive = item.classList.contains('active');

    // Close all
    document.querySelectorAll('.faq-item').forEach(it => {
      it.classList.remove('active');
      it.querySelector('.faq-answer').style.maxHeight = null;
      it.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
    });

    // Open clicked (if it wasn't already)
    if (!isActive) {
      item.classList.add('active');
      answer.style.maxHeight = answer.scrollHeight + 40 + 'px';
      btn.setAttribute('aria-expanded', 'true');
    }
  });
});

// ===== GALLERY LIGHTBOX =====
const galleryItems = Array.from(document.querySelectorAll('.gallery-item'));
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightboxImg');
const lightboxClose = document.getElementById('lightboxClose');
const lightboxPrev = document.getElementById('lightboxPrev');
const lightboxNext = document.getElementById('lightboxNext');
let currentIndex = 0;

function openLightbox(index) {
  currentIndex = index;
  const src = galleryItems[index].getAttribute('data-full');
  lightboxImg.src = src;
  lightbox.classList.add('open');
  lightbox.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}
function closeLightbox() {
  lightbox.classList.remove('open');
  lightbox.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}
function showRelative(step) {
  currentIndex = (currentIndex + step + galleryItems.length) % galleryItems.length;
  lightboxImg.src = galleryItems[currentIndex].getAttribute('data-full');
}

galleryItems.forEach((item, i) => item.addEventListener('click', () => openLightbox(i)));
if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
if (lightboxPrev) lightboxPrev.addEventListener('click', () => showRelative(-1));
if (lightboxNext) lightboxNext.addEventListener('click', () => showRelative(1));
if (lightbox) {
  lightbox.addEventListener('click', (e) => { if (e.target === lightbox) closeLightbox(); });
}
document.addEventListener('keydown', (e) => {
  if (!lightbox.classList.contains('open')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') showRelative(-1);
  if (e.key === 'ArrowRight') showRelative(1);
});

// ===== BACK TO TOP =====
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
  backToTop.classList.toggle('show', window.scrollY > 500);
});
backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

// ===== DYNAMIC YEAR =====
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

// ===== CONTACT FORM =====
// ------------------------------------------------------------------
// TO RECEIVE REAL SUBMISSIONS — pick ONE option:
//
// OPTION A · FORMSPREE (easiest, no code):
//   1. Create a free form at https://formspree.io
//   2. In index.html set: <form ... action="https://formspree.io/f/YOUR_ID" method="POST">
//   3. Delete/return early from the mock handler below (submissions will POST normally).
//
// OPTION B · EMAILJS (send straight to your inbox):
//   1. Sign up at https://www.emailjs.com and create a service + template.
//   2. Add this in index.html <head>:
//        <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
//   3. Uncomment & fill the EmailJS block below.
// ------------------------------------------------------------------
const USE_EMAILJS = false; // set true after adding your EmailJS keys below
const EMAILJS_PUBLIC_KEY = 'YOUR_PUBLIC_KEY';
const EMAILJS_SERVICE_ID = 'YOUR_SERVICE_ID';
const EMAILJS_TEMPLATE_ID = 'YOUR_TEMPLATE_ID';

const form = document.getElementById('contactForm');
const formNote = document.getElementById('formNote');

function resetButton(btn, original) {
  setTimeout(() => {
    btn.textContent = original;
    btn.disabled = false;
    btn.style.background = '';
    if (formNote) formNote.textContent = '';
  }, 5000);
}

if (form) {
  // If a real Formspree action is set, let the browser handle it natively.
  const action = form.getAttribute('action') || '';
  const isFormspree = action.includes('formspree.io');

  if (!isFormspree) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      const original = 'Send Message';
      btn.textContent = 'Sending...';
      btn.disabled = true;

      if (USE_EMAILJS && window.emailjs) {
        // Real send via EmailJS
        emailjs.init(EMAILJS_PUBLIC_KEY);
        emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, form)
          .then(() => {
            btn.textContent = 'Message Sent ✓';
            btn.style.background = 'var(--accent)';
            if (formNote) formNote.textContent = "Thank you! Monica will be in touch within 24–48 hours.";
            form.reset();
            resetButton(btn, original);
          })
          .catch(() => {
            btn.textContent = 'Something went wrong';
            if (formNote) formNote.textContent = "Please email hello@monicafelan.com directly.";
            resetButton(btn, original);
          });
      } else {
        // Demo mock (no backend configured yet)
        setTimeout(() => {
          btn.textContent = 'Message Sent ✓';
          btn.style.background = 'var(--accent)';
          if (formNote) formNote.textContent = "Thank you! (Demo mode — connect Formspree or EmailJS to receive messages.)";
          form.reset();
          resetButton(btn, original);
        }, 1200);
      }
    });
  }
}

// ===== ACTIVE NAV LINK on scroll =====
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 120) {
      current = section.getAttribute('id');
    }
  });
  document.querySelectorAll('.nav-links a').forEach(link => {
    link.style.color = '';
    if (link.getAttribute('href') === `#${current}`) {
      link.style.color = 'var(--accent)';
    }
  });
});
