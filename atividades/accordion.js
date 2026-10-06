'use strict';

async function carregarAccordion() {
  const status = document.getElementById('player-status');
  try {
    const relativo = caminho => new URL(caminho, document.baseURI).href;
    await new H5PStandalone.H5P(document.getElementById('h5p-container'), {
      h5pJsonPath: relativo('./accordion-conteudo'),
      frameJs: relativo('../assets/h5p-player/frame.bundle.js'),
      frameCss: relativo('../assets/h5p-player/styles/h5p.css'),
      frame: false,
      copyright: false,
      export: false,
      downloadUrl: relativo('./accordion-piaget-vigotski-wallon.h5p'),
    });
    status.hidden = true;
  } catch (erro) {
    status.textContent = 'Não foi possível carregar a atividade. Recarregue a página ou baixe o arquivo H5P pelo link abaixo.';
    console.error('Falha ao carregar o Accordion H5P:', erro);
  }
}

carregarAccordion();
