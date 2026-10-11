'use strict';
(async () => {
  const container = document.getElementById('h5p-container');
  const status = document.getElementById('player-status');
  const relativo = p => new URL(p, document.baseURI).href;
  try {
    await new H5PStandalone.H5P(container, {
      h5pJsonPath: relativo('./' + container.dataset.content),
      frameJs: relativo('../assets/h5p-player/frame.bundle.js'),
      frameCss: relativo('../assets/h5p-player/styles/h5p.css'),
      frame: false,
    });
    status.hidden = true;
  } catch (error) {
    status.textContent = 'Não foi possível carregar a comparação. Recarregue a página ou consulte a descrição textual abaixo.';
    console.error(error);
  }
})();
