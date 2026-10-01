# Guia de Funcionalidades H5P

Site HTML estático em português brasileiro com 54 recursos organizados em quatro grupos pedagógicos. Inclui tabelas comparativas, legenda com símbolos e textos, exemplos e links para demonstrações oficiais.

## Abrir

Abra `index.html` em um navegador. Os arquivos `index.html`, `styles.css` e `guide.js` devem ficar na mesma pasta, junto à pasta `images`, que contém os ícones oficiais dos recursos H5P. Inclua essa pasta na publicação. O site não exige servidor, dependências ou etapa de compilação para ser publicado. O pequeno script `guide.js` ajusta o cabeçalho fixo à altura do menu; o conteúdo e os grupos expansíveis funcionam sem JavaScript.

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
