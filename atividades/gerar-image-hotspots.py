"""Empacota quatro pontos sobre segurança elétrica com bibliotecas oficiais do H5P Hub."""
from pathlib import Path
import json
import uuid
import zipfile
import html

PASTA = Path(__file__).resolve().parent
NORMA_URL = 'https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/arquivos/normas-regulamentadoras/nr-10-atualizada-2019-1.pdf'
NORMA_REF = f'BRASIL. Ministério do Trabalho e Emprego. NR-10: segurança em instalações e serviços em eletricidade. Brasília, DF: Ministério do Trabalho e Emprego, 2019. Disponível em: {NORMA_URL}. Acesso em: 6 out. 2026.'
IA_REF = 'OPENAI. Segurança do trabalho em uma sala elétrica: ilustração e conteúdo para Image Hotspots. [S. l.]: OpenAI, 2026. 1 ilustração digital e 1 conteúdo interativo H5P. Produzidos com inteligência artificial por meio do Codex e de sua ferramenta de geração de imagens, a partir de instruções do solicitante, em 6 out. 2026.'
PONTOS = [
    {'titulo':'1. Ponto positivo — bloqueio e etiqueta', 'x':17.8, 'y':27.0,
     'texto':'O cadeado e a etiqueta “NÃO LIGAR” representam medidas para impedir a reenergização e comunicar o bloqueio. São aspectos positivos, mas não comprovam, sozinhos, a desenergização nem a liberação para trabalho.',
     'itens':'10.5.1, alíneas b e f'},
    {'titulo':'2. Ponto positivo — delimitação da área', 'x':23.0, 'y':49.7,
     'texto':'A barreira demarca o espaço de trabalho e ajuda a restringir o acesso de pessoas não envolvidas. Sua instalação deve considerar os riscos e as condições do local. Na cena, a delimitação é um aspecto positivo.',
     'itens':'10.10.1, alíneas c e d'},
    {'titulo':'3. Ponto negativo — relógio metálico', 'x':74.0, 'y':42.2,
     'texto':'O eletricista usa um relógio com pulseira metálica. A NR-10 proíbe adornos pessoais em trabalhos com instalações elétricas ou em suas proximidades. O relógio deve ser retirado antes da atividade.',
     'itens':'10.2.9.3'},
    {'titulo':'4. Ponto negativo — armazenamento indevido', 'x':86.9, 'y':64.0,
     'texto':'As caixas e a vassoura estão guardadas na sala elétrica. Locais de serviços elétricos são destinados exclusivamente a essa finalidade e não devem servir de depósito. Esses objetos devem ser retirados e armazenados em local apropriado.',
     'itens':'10.4.4.1'},
]


def referencias_html():
    norma = html.escape(NORMA_REF).replace(NORMA_URL, f'<a href="{NORMA_URL}" target="_blank" rel="noopener noreferrer">{NORMA_URL}</a>')
    return f'<p><strong>Referência normativa:</strong> {norma}</p><p><strong>Produção com IA:</strong> {html.escape(IA_REF)}</p>'


def gerar():
    with zipfile.ZipFile(PASTA/'image-hotspots-base.h5p') as base:
        manifesto = json.loads(base.read('h5p.json'))
        manifesto.update(title='Segurança do trabalho: observação de uma sala elétrica', language='pt-br', defaultLanguage='pt-br', license='U', authors=[{'name':'OpenAI — produção com inteligência artificial', 'role':'Author'}])
        conteudo = {
            'image': {'path':'images/eletricista-seguranca.png', 'mime':'image/png', 'width':1536, 'height':1024, 'copyright':{'title':'Eletricista em sala elétrica — ilustração produzida com IA', 'author':'OpenAI — ferramenta de geração de imagens', 'year':'2026', 'license':'U'}},
            'backgroundImageAltText':'Ilustração de um eletricista preparando manutenção em uma sala elétrica. Um painel fechado tem chave desligada, cadeado e etiqueta NÃO LIGAR. Uma barreira delimita a área. O profissional usa relógio metálico. À direita há caixas e vassoura armazenadas no local.',
            'iconType':'icon', 'icon':'plus', 'color':'#245a35', 'hotspots':[],
            'hotspotNumberLabel':'Ponto de observação #num', 'closeButtonLabel':'Fechar', 'containsAudioVideoLabel':'Contém áudio ou vídeo',
        }
        for p in PONTOS:
            texto = f'<p>{html.escape(p["texto"])}</p><p><strong>Base normativa:</strong> NR-10, item {p["itens"]}, redação de 2019 vigente em 6 out. 2026.</p>'+referencias_html()
            conteudo['hotspots'].append({'position':{'x':p['x'],'y':p['y'],'legacyPositioning':False},'alwaysFullscreen':False,'header':p['titulo'],'content':[{'library':'H5P.Text 1.1','params':{'text':texto},'subContentId':str(uuid.uuid4()),'metadata':{'title':p['titulo'],'contentType':'Text','license':'U'}}]})
        arquivos = {n:base.read(n) for n in base.namelist() if not n.startswith('content/') and n != 'h5p.json' and not n.endswith('/')}
        arquivos['h5p.json'] = json.dumps(manifesto,ensure_ascii=False).encode('utf-8')
        arquivos['content/content.json'] = json.dumps(conteudo,ensure_ascii=False).encode('utf-8')
        arquivos['content/images/eletricista-seguranca.png'] = (PASTA/'eletricista-seguranca.png').read_bytes()
        with zipfile.ZipFile(PASTA/'image-hotspots-seguranca-eletrica.h5p','w',zipfile.ZIP_DEFLATED) as pacote:
            for nome,dados in arquivos.items(): pacote.writestr(nome,dados)
        destino = PASTA/'image-hotspots-conteudo'
        for nome,dados in arquivos.items():
            alvo = destino/nome
            alvo.parent.mkdir(parents=True,exist_ok=True)
            alvo.write_bytes(dados)

    assert len(conteudo['hotspots']) == 4
    for nome,dados in arquivos.items():
        if nome.endswith('.json'): json.loads(dados)
        if nome.endswith('/library.json'):
            lib=json.loads(dados); prefix=nome.rsplit('/',1)[0]
            for tipo in ('preloadedJs','preloadedCss'):
                for recurso in lib.get(tipo,[]): assert prefix+'/'+recurso['path'] in arquivos
            for tipo in ('preloadedDependencies','editorDependencies','dynamicDependencies'):
                for d in lib.get(tipo,[]): assert f'{d["machineName"]}-{d["majorVersion"]}.{d["minorVersion"]}/library.json' in arquivos
    with zipfile.ZipFile(PASTA/'image-hotspots-seguranca-eletrica.h5p') as pacote: assert pacote.testzip() is None
    texto=['# Segurança do trabalho — Image Hotspots','', 'Cena: preparação de manutenção em sala elétrica, com o painel fechado. Objetivo: identificar duas medidas positivas e duas condições que precisam ser corrigidas. A cena apresenta quatro aspectos para observação, sem representar a sequência completa de desenergização.','']
    for p in PONTOS: texto += ['## '+p['titulo'],'',p['texto'],'','Base: NR-10, item '+p['itens']+'.','']
    texto += ['## Referências em formato ABNT','',NORMA_REF,'',IA_REF,'','A referência da produção com IA descreve este material digital; não é uma fonte normativa. O conteúdo foi gerado com IA e conferido com os itens da NR-10 indicados. As bibliotecas são do pacote oficial https://api.h5p.org/v1/content-types/H5P.ImageHotspots e mantêm suas licenças originais.','']
    (PASTA/'image-hotspots-seguranca-eletrica.md').write_text('\n'.join(texto),encoding='utf-8')
    print('Pacote gerado e validado: quatro pontos, imagem, referências e bibliotecas incluídos.')


if __name__=='__main__': gerar()
