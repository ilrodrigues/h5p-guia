'use strict';
(async()=>{
 const status=document.getElementById('player-status');
 const relativo=p=>new URL(p,document.baseURI).href;
 try{
  await new H5PStandalone.H5P(document.getElementById('h5p-container'),{
   h5pJsonPath:relativo('./course-presentation-navegacao-conteudo'),
   frameJs:relativo('../assets/h5p-player/frame.bundle.js'),
   frameCss:relativo('../assets/h5p-player/styles/h5p.css'),frame:false,
  });status.hidden=true;
 }catch(e){status.textContent='Não foi possível carregar. Recarregue a página ou consulte o conteúdo abaixo.';console.error(e);}
})();
