'use strict';
// Executado no iframe do player; não altera as bibliotecas oficiais do H5P.
(() => {
  function atualizar() {
    const container = document.querySelector('.h5p-image-hotspots-container');
    const background = container?.querySelector('.h5p-image-hotspots-background');
    if (background && !container.querySelector('.seguranca-relogio-indicador')) {
      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.setAttribute('class', 'seguranca-relogio-indicador');
      svg.setAttribute('viewBox', '0 0 1536 1024');
      svg.setAttribute('preserveAspectRatio', 'none');
      svg.setAttribute('aria-hidden', 'true');
      // Ponta em 67,5%, junto à borda direita do relógio; origem no marcador.
      svg.innerHTML = '<path d="M1136.64 432.128 H1049" fill="none" stroke="white" stroke-width="3"/><path d="M1036.8 432.128 L1051 422 L1051 442 Z" fill="white"/>';
      background.after(svg);
    }
    document.querySelectorAll('.h5p-image-hotspots-overlay').forEach(overlay => {
      const header = overlay.querySelector('.h5p-image-hotspot-popup-header');
      if (header?.textContent.includes('relógio metálico') && !overlay.classList.contains('seguranca-relogio-popup')) {
        overlay.classList.add('seguranca-relogio-popup');
      }
    });
  }
  new MutationObserver(atualizar).observe(document.documentElement, {childList: true, subtree: true});
  atualizar();
})();
