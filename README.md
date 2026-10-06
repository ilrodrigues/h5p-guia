# Guia de Funcionalidades H5P

Site HTML estático em português brasileiro com 54 recursos organizados em quatro grupos pedagógicos. Inclui tabelas comparativas, legenda com símbolos e textos, exemplos e links para demonstrações oficiais.

## Abrir

Abra `index.html` em um navegador. Os arquivos `index.html`, `styles.css` e `guide.js` devem ficar na mesma pasta, junto à pasta `images`, que contém os ícones oficiais dos recursos H5P. Inclua essa pasta na publicação. O guia não exige etapa de compilação para ser publicado. O exemplo H5P precisa ser servido por HTTP ou HTTPS; abrir seu HTML diretamente como arquivo local não é suficiente. O pequeno script `guide.js` ajusta o cabeçalho fixo à altura do menu; o conteúdo e os grupos expansíveis funcionam sem JavaScript.

## Publicar no GitHub Pages

1. Utilize o repositório `h5p-guia` na conta desejada. Para publicação com GitHub Free, o repositório deve ser público.
2. Envie os arquivos desta pasta à raiz do repositório e faça o commit na branch `main`.
3. Em **Settings → Pages → Build and deployment**, escolha **Deploy from a branch**.
4. Selecione a branch `main` e a pasta `/ (root)`, e salve.
5. Aguarde a publicação e use o endereço exibido em **Settings → Pages**. O formato usual é `https://USUARIO.github.io/h5p-guia/`.

Documentação: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Editar o conteúdo

Edite `catalogo.json` e execute `node build.mjs` para gerar novamente `index.html`. Node.js é necessário apenas para essa regeneração. A aparência é definida em `styles.css`. Inclua a versão atualizada de `index.html` no commit: o GitHub Pages não executa automaticamente esse gerador.

Cada recurso contém: nome em inglês, nome em português, URL oficial, facilidade, preparação, apresentação de informações, prática e feedback, avaliação, possibilidades da Taxonomia de Bloom e exemplo. Um último campo opcional contém a URL da imagem do recurso. Nas três colunas de classificação, os prefixos são `G` (adequado), `Y` (condicional) e `R` (não oferece diretamente), seguidos de `|` e da explicação.

## Critérios e fontes

As classificações e os exemplos são propostas pedagógicas, não classificações oficiais do H5P. Os níveis da Taxonomia de Bloom indicam possibilidades e dependem da tarefa. A verificação automática não garante registro de notas no Moodle. A disponibilidade e acessibilidade dos tipos de conteúdo dependem da versão e da instalação.

- Catálogo oficial: https://h5p.org/content-types-and-applications
- Atividade H5P no Moodle: https://docs.moodle.org/501/en/H5P_activity
- Referência de organização em matriz: https://moodletoolguide.net/pt-br/

A referência visual é o Guia de Ferramentas Moodle disponibilizado por Nicolas Martignoni, baseado na ideia de Joyce Seitzinger, com tradução e adaptação brasileira de Gilvan Marques. O texto e a matriz H5P foram elaborados para esta proposta.

Consulta das fontes: 30/09/2026.

## Exemplo Accordion com H5P Standalone

Abra `atividades/accordion.html` em um servidor HTTP. Para conferir localmente, execute `python -m http.server 8000` na raiz e acesse http://localhost:8000/atividades/accordion.html.

O player H5P Standalone 3.8.2 está incluído em `assets/h5p-player`, com arquivos de licença. Nenhum CDN ou instalação npm é necessário para servir o site. O pacote original `.h5p` está em `atividades`, e sua versão extraída em `atividades/accordion-conteudo`. Inclua `assets` e os arquivos da atividade na publicação, também no GitHub Pages.

Para atualizar os textos, execute `python atividades/gerar-accordion.py` e extraia novamente o pacote gerado para `atividades/accordion-conteudo`. O arquivo `accordion-base.h5p` é a base oficial utilizada pelo gerador. As referências e os créditos estão em `atividades/accordion-piaget-vigotski-wallon.md`.

## Atualizar o GitHub Pages com o exemplo

Publique `assets` e `atividades` junto com os arquivos do guia na branch configurada no GitHub Pages. A página do exemplo será `atividades/accordion.html`, e a tabela do Accordion inclui um link para abri-la. Os caminhos relativos também funcionam quando o site está em um subdiretório como `/h5p-guia/`.

Documentação do player: https://github.com/tunapanda/h5p-standalone
Documentação do Pages: https://docs.github.com/en/pages

## Exemplo Image Hotspots — segurança do trabalho

A página `atividades/image-hotspots.html` apresenta quatro pontos: bloqueio e etiqueta, delimitação da área, relógio metálico e armazenamento indevido. Os dois primeiros são positivos; os dois últimos são negativos. A base é a redação de 2019 da NR-10, vigente na data de elaboração (6 out. 2026). As referências em formato ABNT e a declaração de produção com IA estão na página, no pacote e em `atividades/image-hotspots-seguranca-eletrica.md`.

O arquivo para importação é `atividades/image-hotspots-seguranca-eletrica.h5p`; o conteúdo extraído está em `atividades/image-hotspots-conteudo`. O gerador é `atividades/gerar-image-hotspots.py`. A ilustração original está em `atividades/eletricista-seguranca.png`; o prompt final está em `atividades/image-hotspots-prompt.txt`. O gerador também atualiza a pasta extraída. As bibliotecas oficiais foram obtidas em https://api.h5p.org/v1/content-types/H5P.ImageHotspots.
