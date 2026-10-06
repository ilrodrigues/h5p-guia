"""Gera o exemplo a partir do pacote oficial do H5P Accordion, sem executar seu código."""
import html
import json
import uuid
import zipfile
from pathlib import Path

PASTA = Path(__file__).resolve().parent
PAINEIS = [
    {
        "titulo": "Jean Piaget",
        "texto": "Jean Piaget (1896–1980) foi um biólogo, psicólogo e epistemólogo suíço que investigou a formação do conhecimento e desenvolveu a epistemologia genética. Seus estudos sobre o pensamento infantil descrevem quatro estágios de desenvolvimento cognitivo: sensório-motor, pré-operatório, operatório concreto e operatório formal. Nessa perspectiva, o pensamento se transforma ao longo do desenvolvimento, passando das ações práticas à possibilidade de raciocinar sobre situações abstratas e formular hipóteses. Sua contribuição para a educação destaca a participação da criança no processo de descoberta e a atenção às formas de pensar próprias de seu desenvolvimento.",
        "verbete": "JEAN Piaget",
        "ano": "2026",
        "url": "https://pt.wikipedia.org/wiki/Jean_Piaget",
    },
    {
        "titulo": "Lev Vigotski",
        "texto": "Lev Vigotski (1896–1934) foi um psicólogo associado à psicologia histórico-cultural, cuja obra enfatiza as relações entre desenvolvimento humano, interação social e cultura. A linguagem e outros signos culturais participam da mediação da aprendizagem e da organização do pensamento. Entre os conceitos apresentados em sua obra está a zona de desenvolvimento proximal, que expressa a diferença entre aquilo que a criança consegue realizar sozinha e aquilo que pode realizar com a orientação de um adulto ou a colaboração de alguém mais experiente. Essa perspectiva ressalta a importância das relações sociais e da mediação no processo de aprender e desenvolver novas capacidades.",
        "verbete": "LEV Vygotsky",
        "ano": "2026",
        "url": "https://pt.wikipedia.org/wiki/Lev_Vygotsky",
    },
    {
        "titulo": "Henri Wallon",
        "texto": "Henri Wallon (1879–1962) foi um psicólogo, médico e filósofo francês que propôs compreender o desenvolvimento infantil considerando a pessoa em sua totalidade. Sua teoria articula movimento, afetividade, inteligência e pessoa, destacando tanto as condições orgânicas quanto as influências do meio social. As emoções e os movimentos participam das primeiras relações da criança com o ambiente, enquanto o desenvolvimento envolve mudanças e conflitos, com alternância entre a predominância afetiva e a cognitiva. Sua contribuição para a educação evidencia que compreender a criança exige considerar conjuntamente suas dimensões afetivas, motoras e intelectuais e suas relações com os outros.",
        "verbete": "HENRI Wallon (psicólogo)",
        "ano": "2025",
        "url": "https://pt.wikipedia.org/wiki/Henri_Wallon_(psic%C3%B3logo)",
    },
]


def referencia(painel, formato_html=False):
    obra = "<strong>Wikipédia: a enciclopédia livre</strong>" if formato_html else "Wikipédia: a enciclopédia livre"
    url = painel["url"]
    link = f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>' if formato_html else url
    return f'{painel["verbete"]}. In: {obra}. [S. l.]: Wikimedia Foundation, {painel["ano"]}. Disponível em: {link}. Acesso em: 6 out. 2026.'


def gerar():
    with zipfile.ZipFile(PASTA / "accordion-base.h5p") as base:
        manifesto = json.loads(base.read("h5p.json"))
        manifesto.update({
            "title": "Pensadores do desenvolvimento infantil: Piaget, Vigotski e Wallon",
            "language": "pt-br",
            "defaultLanguage": "pt-br",
            "license": "CC BY-SA",
            "licenseVersion": "4.0",
            "authors": [{"name": "Colaboradores da Wikipédia em português", "role": "Author"}],
            "changes": [{"date": "2026-10-06", "author": "Equipe do Guia H5P", "log": "Síntese e adaptação dos verbetes em três painéis; referências em formato ABNT."}],
        })
        conteudo = {"panels": [], "hTag": "h2"}
        for painel in PAINEIS:
            conteudo["panels"].append({
                "title": painel["titulo"],
                "content": {
                    "library": "H5P.AdvancedText 1.1",
                    "params": {"text": f'<p>{html.escape(painel["texto"])}</p><p><strong>Referência:</strong> {referencia(painel, True)}</p>'},
                    "subContentId": str(uuid.uuid4()),
                    "metadata": {"contentType": "Text", "title": painel["titulo"], "license": "CC BY-SA", "licenseVersion": "4.0", "authors": [{"name": "Colaboradores da Wikipédia em português", "role": "Author"}], "source": painel["url"]},
                },
            })
        destino = PASTA / "accordion-piaget-vigotski-wallon.h5p"
        with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as pacote:
            for nome in base.namelist():
                if not nome.startswith("content/") and nome != "h5p.json":
                    pacote.writestr(nome, base.read(nome))
            pacote.writestr("h5p.json", json.dumps(manifesto, ensure_ascii=False))
            pacote.writestr("content/content.json", json.dumps(conteudo, ensure_ascii=False))

    linhas = ["# Pensadores do desenvolvimento infantil", "", "Conteúdo do H5P Accordion: três painéis, com um parágrafo de síntese por pensador e a referência correspondente.", ""]
    for painel in PAINEIS:
        linhas.extend([f'## {painel["titulo"]}', "", painel["texto"], "", referencia(painel), ""])
    linhas.extend(["## Créditos e licença", "", "Sínteses e adaptações dos verbetes da Wikipédia em português. Textos sob licença Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional (CC BY-SA 4.0): https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br. A autoria original é dos colaboradores da Wikipédia; seus históricos estão disponíveis nos respectivos verbetes. Os anos nas referências correspondem à última atualização exibida nas páginas consultadas.", "", "Bibliotecas obtidas do exemplo oficial: https://h5p.org/sites/default/files/h5p/exports/accordion-6-7138.h5p. As bibliotecas mantêm seus metadados e licenças originais.", "", "O pacote inclui H5P.Accordion, H5P.AdvancedText e FontAwesome. A estrutura e as dependências foram verificadas; a importação e a execução em um ambiente H5P ainda precisam ser verificadas.", ""])
    (PASTA / "accordion-piaget-vigotski-wallon.md").write_text("\n".join(linhas), encoding="utf-8")

    with zipfile.ZipFile(destino) as pacote:
        assert pacote.testzip() is None
        nomes = set(pacote.namelist())
        dados = json.loads(pacote.read("content/content.json"))
        assert len(dados["panels"]) == 3
        assert [p["title"] for p in dados["panels"]] == [p["titulo"] for p in PAINEIS]
        for p in dados["panels"]:
            assert p["content"]["params"]["text"].count("<p>") == 2
            assert "Acesso em: 6 out. 2026." in p["content"]["params"]["text"]
        for nome in nomes:
            if nome.endswith(".json"):
                json.loads(pacote.read(nome))
            if nome.endswith("/library.json"):
                biblioteca = json.loads(pacote.read(nome))
                pasta = nome.rsplit("/", 1)[0]
                for tipo in ("preloadedJs", "preloadedCss"):
                    for recurso in biblioteca.get(tipo, []):
                        assert f'{pasta}/{recurso["path"]}' in nomes
                for tipo in ("preloadedDependencies", "dynamicDependencies", "editorDependencies"):
                    for dependencia in biblioteca.get(tipo, []):
                        caminho = f'{dependencia["machineName"]}-{dependencia["majorVersion"]}.{dependencia["minorVersion"]}/library.json'
                        assert caminho in nomes, caminho
        for dependencia in manifesto["preloadedDependencies"]:
            assert f'{dependencia["machineName"]}-{dependencia["majorVersion"]}.{dependencia["minorVersion"]}/library.json' in nomes
    print(f"Pacote validado: {destino.name} ({destino.stat().st_size:,} bytes); três painéis e todas as dependências incluídas.")


if __name__ == "__main__":
    gerar()
