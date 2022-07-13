import string
import PyPDF2
import re


def abrindo_pdf():
  pdfFile = open('PedroRochaCamposJun22.pdf', 'rb')

  readr = PyPDF2.PdfReader(pdfFile)
  print(f'O PDF carregado tem {readr.numPages} paginas')

  return readr, readr.numPages


def get_all_text():
  rea, nP = abrindo_pdf()

  ltxt = []

  for n in range(0,nP):

    pagina = rea.getPage(n)
    #print(pagina.extractText())
    ltxt.append(str(pagina.extract_text()))
  
  ltxt = str(ltxt[0])

  return ltxt


def treating_text(txt=get_all_text()):

  txt = re.sub("[^\w @/.]", "",txt).lower()

  return txt


def getting_email(txt):
  em = re.findall('[\w]{0,40}@gmail.com', txt)
  return em


def acessando_chaves(txt):
  dc = {'analista de dados':('python', 'powerbi', 'sql','comunicação'), 'cientista de dados': ('python', 'banco de dados', 'machine learning', 'resolução de problemas','estatística')}

  prof_elegiveis, set_compet = set(), set()


  for parcv in dc.items():
    #print(parcv)
    for elemento_do_valor in parcv[1]:
      if elemento_do_valor in txt:
        set_compet.add(elemento_do_valor)
        prof_elegiveis.add(parcv[0])

  
  return set_compet, prof_elegiveis


def candidato():

  texto_str = treating_text()
  email = getting_email(texto_str)

  competencias, profissoes_elegiveis = acessando_chaves(texto_str)

  candidato = (f'''
O candidato identificado pelo email: {email}
está apto a se candidatar para as vagas de {" e ".join([i for i in profissoes_elegiveis])}.

Suas competências desejadas são {", ".join([a.capitalize() for a in competencias])}
''')

  return candidato

def main():
  print(candidato())


main()