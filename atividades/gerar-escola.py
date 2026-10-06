"""Gera o segundo exemplo Image Hotspots com a imagem aprovada da escola."""
import html
import json
import uuid
import zipfile
from pathlib import Path

PASTA = Path(__file__).resolve().parent
REFERENCIA = 'OPENAI. Escola e seus espaços pedagógicos: mapa ilustrado em perspectiva. [S. l.]: OpenAI, 2026. 1 imagem digital. Imagem produzida e revisada com inteligência artificial, por meio da ferramenta de geração de imagens integrada ao Codex, a partir de instruções do solicitante, em 6 out. 2026.'
PONTOS = [
    ('Horta — investigar e cuidar', 85.8, 67.5, 'A horta pode integrar Ciências, Matemática e Educação Ambiental. Proponha que os estudantes acompanhem o crescimento de plantas, meçam sua altura e registrem os resultados em tabelas e gráficos. A turma pode discutir as necessidades de água e luz, os cuidados com o solo e a origem dos alimentos, organizando um diário de observações e uma rotina coletiva de cuidado.'),
    ('Laboratório de química — observar e explicar', 73.8, 19.0, 'O laboratório favorece a investigação de propriedades dos materiais. Sob orientação do professor e com os cuidados de segurança definidos para a atividade, os estudantes podem comparar misturas de água com sal, areia e óleo, registrar observações e discutir dissolução e separação de misturas. Solicite hipóteses antes da observação e uma explicação ao final, apoiada nas evidências coletadas.'),
    ('Sala de aula — dialogar e construir conhecimentos', 30.5, 18.5, 'A sala de aula pode acolher rodas de conversa, leitura compartilhada e resolução colaborativa de problemas. Organize grupos para analisar uma questão, comparar estratégias e apresentar seus argumentos à turma. Os registros individuais e coletivos ajudam o professor a acompanhar a compreensão dos estudantes e a planejar novas intervenções.'),
    ('Pátio — conviver e aprender em movimento', 44.8, 44.0, 'O pátio permite articular convivência, expressão corporal e investigação do ambiente. Uma proposta é mapear as áreas de sol e sombra em diferentes horários, discutir como elas afetam o uso do espaço e produzir um mapa coletivo. Também pode receber jogos cooperativos e assembleias da turma, com participação acessível e regras de cuidado construídas em conjunto.'),
]


def gerar():
    with zipfile.ZipFile(PASTA/'image-hotspots-base.h5p') as base:
        manifesto = json.loads(base.read('h5p.json'))
        manifesto.update(title='Explorar espaços de uma escola e suas funções pedagógicas', language='pt-br', defaultLanguage='pt-br', license='U')
        dados = {'image':{'path':'images/escola.png','mime':'image/png','width':1536,'height':1024,'copyright':{'title':'Escola e seus espaços pedagógicos — imagem produzida com IA','author':'OpenAI — ferramenta de geração de imagens','year':'2026','license':'U'}},'backgroundImageAltText':'Mapa ilustrado de uma escola em vista superior levemente inclinada. Salas e biblioteca se ligam a corredores, com saída sinalizada ao fundo. Quatro pontos destacam a horta à direita, o laboratório no alto à direita, a sala de aula no alto à esquerda e o pátio central com árvore e bancos.','iconType':'icon','icon':'plus','color':'#245a35','hotspotNumberLabel':'Espaço pedagógico #num','closeButtonLabel':'Fechar','containsAudioVideoLabel':'Contém áudio ou vídeo','hotspots':[]}
        for titulo,x,y,texto in PONTOS:
            dados['hotspots'].append({'position':{'x':x,'y':y,'legacyPositioning':False},'alwaysFullscreen':False,'header':titulo,'content':[{'library':'H5P.Text 1.1','params':{'text':f'<p>{html.escape(texto)}</p><p><strong>Referência da imagem:</strong> {html.escape(REFERENCIA)}</p>'},'metadata':{'title':titulo,'contentType':'Text','license':'U'},'subContentId':str(uuid.uuid4())}]})
        arquivos={n:base.read(n) for n in base.namelist() if not n.startswith('content/') and n!='h5p.json' and not n.endswith('/')}
    arquivos['h5p.json']=json.dumps(manifesto,ensure_ascii=False).encode('utf-8')
    arquivos['content/content.json']=json.dumps(dados,ensure_ascii=False).encode('utf-8')
    arquivos['content/images/escola.png']=(PASTA/'escola-mapa-proposta-v2.png').read_bytes()
    with zipfile.ZipFile(PASTA/'image-hotspots-escola.h5p','w',zipfile.ZIP_DEFLATED) as pacote:
        for nome,conteudo in arquivos.items():pacote.writestr(nome,conteudo)
    for nome,conteudo in arquivos.items():
        destino=PASTA/'escola-conteudo'/nome
        destino.parent.mkdir(parents=True,exist_ok=True)
        destino.write_bytes(conteudo)
    with zipfile.ZipFile(PASTA/'image-hotspots-escola.h5p') as pacote:
        assert pacote.testzip() is None
        assert len(json.loads(pacote.read('content/content.json'))['hotspots'])==4
        for nome in pacote.namelist():
            if nome.endswith('.json'):json.loads(pacote.read(nome))
    linhas=['# Explorar espaços de uma escola e suas funções pedagógicas','']
    for titulo,x,y,texto in PONTOS:linhas += ['## '+titulo,'',texto,'']
    linhas += ['## Referência da imagem em formato ABNT','',REFERENCIA,'','As sugestões pedagógicas foram elaboradas com auxílio de IA. A referência identifica a produção da imagem; não representa uma fonte teórica para as sugestões.','']
    (PASTA/'image-hotspots-escola.md').write_text('\n'.join(linhas),encoding='utf-8')
    print('Pacote da escola validado: quatro pontos e imagem aprovada incluídos.')


if __name__=='__main__':gerar()
