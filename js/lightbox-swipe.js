document.addEventListener('DOMContentLoaded', () => {
  const lightboxes = document.querySelectorAll('.lightbox');

  lightboxes.forEach((lightbox) => {
    const hammer = new Hammer(lightbox);

    hammer.on('swipeleft', () => {
      const nextLink = lightbox.querySelector('.nav-arrow.next');
      if (nextLink) {
        window.location.hash = nextLink.getAttribute('href');
      }
    });

    hammer.on('swiperight', () => {
      const prevLink = lightbox.querySelector('.nav-arrow.prev');
      if (prevLink) {
        window.location.hash = prevLink.getAttribute('href');
      }
    });
  });
});
