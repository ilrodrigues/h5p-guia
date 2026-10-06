'use strict';

async function carregarHotspots() {
  const status = document.getElementById('player-status');
  try {
    const relativo = caminho => new URL(caminho, document.baseURI).href;
    await new H5PStandalone.H5P(document.getElementById('h5p-container'), {
      h5pJsonPath: relativo('./escola-conteudo'),
      frameJs: relativo('../assets/h5p-player/frame.bundle.js'),
      frameCss: relativo('../assets/h5p-player/styles/h5p.css'),
      frame: false,
    });
    status.hidden = true;
  } catch (erro) {
    status.textContent = 'Não foi possível carregar a atividade. Recarregue a página ou leia a descrição dos quatro pontos abaixo.';
    console.error('Falha ao carregar Image Hotspots:', erro);
  }
}

carregarHotspots();
