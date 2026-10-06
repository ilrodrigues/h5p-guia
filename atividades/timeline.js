'use strict';
(async () => {
  const status = document.getElementById('player-status');
  try {
    const url = path => new URL(path, document.baseURI).href;
    await new H5PStandalone.H5P(document.getElementById('h5p-container'), {
      h5pJsonPath: url('./timeline-conteudo'),
      frameJs: url('../assets/h5p-player/frame.bundle.js'),
      frameCss: url('../assets/h5p-player/styles/h5p.css'),
      frame: false,
    });
    status.hidden = true;
  } catch (error) {
    status.textContent = 'Não foi possível carregar a linha do tempo. Leia os 12 marcos e suas referências abaixo.';
    console.error('Falha ao carregar Timeline:', error);
  }
})();
