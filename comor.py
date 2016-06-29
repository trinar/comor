#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import decimal
import copy
from vynimky import Vynimka

dataStack = None
helpStack = None
#namespace = None
hlasky = ['\nVynimka v programe!',
          '\nZásobník dataStack je prázdny!',
          '\nZásobník helpStack je prázdny!',
          '\nZlý formát prvku v dataStack!',
          '\nIndex mimo rozsah vstupného reťazca!',
          '\nNesprávny počet zátvoriek!',
          '\nNesprávny počet apostrofov!',
          '\nSúbor nenájdený!'] #chybove hlasky

def zDS(): #vyberie vrchny prvok zo zasobnika dataStack
  global dataStack
  try:
    x = dataStack.pop()
  except IndexError:
    raise Vynimka(hlasky[1])
  return x

def doDS(x): #zapise prvok na vrch zasobnika dataStack
  global dataStack
  dataStack.append(str(x))

def zHS(): #vyberie vrchny prvok zo zasobnika helpStack
  global helpStack
  try:
    x = helpStack.pop()
  except IndexError:
    raise Vynimka(hlasky[2])
  return x

def doHS(x): #zapise prvok na vrch zasobnika helpStack
  global helpStack
  helpStack.append(str(x))

def mov(): #presunie prvok z dataStack do helpStack
  a = zDS()
  doHS(a)

def rem(): #presunie prvok z helpStack do dataStack
  a = zHS()
  doDS(a)

def dup(): #zduplikuje vrchny prvok
  a = zDS()
  doDS(a)
  doDS(a)

def swap(): #prevrati 2 vrchne prvky
  a = zDS()
  b = zDS()
  doDS(a)
  doDS(b)

def drop(): #vymaze vrchny prvok
  zDS()

def over(): #na vrch skopiruje 2 prvok od vrchu
  a = zDS()
  b = zDS()
  doDS(b)
  doDS(a)
  doDS(b)

def wrap(): #vlozi vrchny prvok dozatvoriek
  a = zDS()
  a = '[' + a + ']'
  doDS(a)

def i(): #vykona vrchny prvok
  a = zDS()
  parse(a)

def sc(): #vyberie prvky a, b, c, d a vlozi ich v poradi [[d] c], vykona a, vlozi d, vykona b
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  doDS('[' + d + ']' + ' ' + c)
  parse(a)
  doDS(d)
  parse(b)

def j(): #vyberie prvky a, b, c, d a vlozi ich v poradi [[c] [d] a][b] a vykona prvok a
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  doDS('[' + c + ']' + ' ' + '[' + d + '] ' + a)
  doDS(b)
  parse(a)

def jc(): #vyberie prvky a, b, c, d, e a vlozi ich v poradi [[d] a [e] b][c] a vykona prvok b
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  e = zDS()
  doDS('[' + d + ']' + ' ' + a + ' [' + e + '] ' + b)
  doDS(c)
  parse(b)

def cons(): #pripoji druhy prvok pred prvy
  a = zDS()
  b = zDS()
  doDS(b + ' ' + a)

def uncons(): #rozdeli prvok na prvu cast a zvysok
  a = zDS()
  doDS(a)
  first()
  doDS(a)
  rest()

def first(): #vrati prvu cast listu
  a = zDS()
  for token in vratToken(a):
    doDS(token)
    break

def last(): #vrati poslednu cast listu
  a = zDS()
  for token in vratToken(a):
    pass
  doDS(token)

def rest(): #vrati vsetko okrem prvej casti listu
  a = zDS()
  vysledok = []
  for token in vratToken(a):
    vysledok.append(token)
  del vysledok[0]
  doDS(' '.join(vysledok))

def split(): #rozdeli vrchny prvok na samostatne prvky
  a = zDS()
  for token in vratToken(a):
    doDS(token)

def grup(): #spoji vsetky prvky v zasobniku do sekvencie
  a = ' '.join(dataStack)
  cleard()
  doDS(a)

def flat(): #odstrani vsetky zatvorky
  a = zDS()
  b = a.replace('[', ' ')
  c = b.replace(']', ' ')
  doDS(c.strip())
  
def cat(): #pripoji druhy prvok pred prvy bez medzery
  a = zDS()
  b = zDS()
  doDS(b + a)

def size(): #zisti dlzku najvyssieho prvku
  a = zDS()
  vysledok = []
  for token in vratToken(a):
    vysledok.append(token)
  doDS(len(vysledok))

def reverse(): #prevrati postupnost v najvyssom prvku
  a = zDS()
  vysledok = []
  for token in vratToken(a):
    vysledok.append(token)
  doDS(' '.join(reversed(vysledok)))

def add(): #scita dva vrchne prvky
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b+a)

def sub(): #odcita vrchny prvok od spodneho
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b-a)

def mul(): #vynasobi dva vrchne prvky
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b*a)

def exp(): #umocni spodny prvok na vrchny
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b**a)

def div(): #vydeli spodny prvok vrchnym
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b/a)

def divint(): #celociselne vydeli spodny prvok vrchnym
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b//a)

def mod(): #vrati zostatok po celociselnom vydeleni spodneho prvku vrchnym
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b%a)

def divmod_(): #vrati vysledok a zostatok po celociselnom vydeleni spodneho prvku vrchnym
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b//a)
  doDS(b%a)

def and_(): #logicky sucin
  a = zDS()
  b = zDS()
  if a == 'true':
    a = True
  elif a == 'false':
    a = False
  else:
    raise Vynimka(hlasky[3])
  if b == 'true':
    b = True
  elif b == 'false':
    b = False
  else:
    raise Vynimka(hlasky[3])
  if a and b:
    doDS('true')
  else:
    doDS('false')

def or_(): #logicky sucet
  a = zDS()
  b = zDS()
  if a == 'true':
    a = True
  elif a == 'false':
    a = False
  else:
    raise Vynimka(hlasky[3])
  if b == 'true':
    b = True
  elif b == 'false':
    b = False
  else:
    raise Vynimka(hlasky[3])
  if a or b:
    doDS('true')
  else:
    doDS('false')

def xor_(): #logicky exkluzivny sucet
  a = zDS()
  b = zDS()
  if a == 'true':
    a = True
  elif a == 'false':
    a = False
  else:
    raise Vynimka(hlasky[3])
  if b == 'true':
    b = True
  elif b == 'false':
    b = False
  else:
    raise Vynimka(hlasky[3])
  if a != b:
    doDS('true')
  else:
    doDS('false')

def not_(): #logicka negacia
  a = zDS()
  if a == 'true':
    a = True
  elif a == 'false':
    a = False
  else:
    raise Vynimka(hlasky[3])
  if a:
    doDS('false')
  else:
    doDS('true')

def min_(): #minimum dvoch prvkov
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(min(a, b))

def max_(): #maximum dvoch prvkov
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(max(a, b))

def abs_(): #absolutna hodnota prvku
  a = zDS()
  try:
    a = decimal.Decimal(a)
  except:
    raise Vynimka(hlasky[3])
  doDS(abs(a))

def sign(): #znamienko prvku
  a = zDS()
  try:
    a = decimal.Decimal(a)
  except:
    raise Vynimka(hlasky[3])
  doDS((a >= 0) - (a < 0))
    
def if_(): #porovna piaty a stvrty prvok a ak je piaty mensi vykona treti prvok, ak su rovnake vykona druhy prvok a ak je piaty vacsi vykona prvy prvok
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  e = zDS()
  try:
    d = decimal.Decimal(d)
    e = decimal.Decimal(e)
  except:
    raise Vynimka(hlasky[3])
  if e > d:
    parse(a)
  elif e == d:
    parse(b)
  elif e < d:
    parse(c)

def ift(): #ak je druhy prvok pravdivy vykona prvy prvok
  a = zDS()
  b = zDS()
  if b == 'true':
    parse(a)

def ifte(): #ak je treti prvok pravdivy vykona druhy prvok inak vykona prvy prvok
  a = zDS()
  b = zDS()
  c = zDS()
  if c == 'true':
    parse(b)
  else:
    parse(a)

def times(): #vykona druhy prvok dany pocet krat (v prvom prvku)
  a = zDS()
  b = zDS()
  try:
    a = int(a)
  except:
    raise Vynimka(hlasky[3])
  for i in range(a):
    parse(b)

def for_(): #cyklus for
  a = zDS()
  b = zDS()
  c = zDS()
  try:
    b = int(b)
    c = int(c)
  except:
    raise Vynimka(hlasky[3])
  if b > c:
    for i in range(c, b+1):
      parse(a)
  elif b < c:
    for i in range(c, b-1, -1):
      parse(a)

def fors(): #cyklus for s urcenim kroku
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  try:
    b = int(b)
    c = int(c)
    d = int(d)
  except:
    raise Vynimka(hlasky[3])
  if c > d:
    for i in range(d, c+1, b):
      parse(a)
  elif c < d:
    for i in range(d, c-1, b):
      parse(a)

def while_(): #ak je druhy prvok pravdivy vykona prvy prvok
  a = zDS()
  b = zDS()
  while True:
    parse(b)
    c = zDS()
    if c == 'true':
      parse(a)
    else:
      break

def rovne(): #vrati true ak su vrchne dva prvky rovne
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  if a == b:
    doDS('true')
  else:
    doDS('false')

def nerovne(): #vrati true ak su vrchne dva prvky nerovne
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  if a != b:
    doDS('true')
  else:
    doDS('false')

def vacsie(): #vrati true ak spodny prvok je vacsi ako vrchny
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  if b > a:
    doDS('true')
  else:
    doDS('false')

def mensie(): #vrati true ak spodny prvok je mensi ako vrchny
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  if b < a:
    doDS('true')
  else:
    doDS('false')

def vacsierovne(): #vrati true ak spodny prvok je vacsi alebo rovny ako vrchny
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  if b >= a:
    doDS('true')
  else:
    doDS('false')

def mensierovne(): #vrati true ak spodny prvok je mensi alebo rovny ako vrchny
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  if b <= a:
    doDS('true')
  else:
    doDS('false')

def list_(): #vytvori postupnost cisel od b po a
  a = zDS()
  b = zDS()
  try:
    a = int(a)
    b = int(b)
  except:
    raise Vynimka(hlasky[3])
  c = []
  for i in range(b, a+1):
    c.append(str(i))
  doDS(' '.join(c))

def infra_old(): #vykona prvok a na prvku b, ktory berie ako zasobnik
  global dataStack, helpStack
  a = zDS()
  b = zDS()
  dataStack_tmp = copy.deepcopy(dataStack)
  dataStack = []
  helpStack_tmp = copy.deepcopy(helpStack)
  helpStack = []
  for token in vratToken(b):
    doDS(token)
  parse(a)
  parse('height')
  c = zDS()
  while int(c) > 1:
    parse('cons')
    parse('height')
    c = zDS()
  d = zDS()
  dataStack = copy.deepcopy(dataStack_tmp)
  helpStack = copy.deepcopy(helpStack_tmp)
  doDS(d)

def infra(): #vykona prvok a na prvku b, ktory berie ako zasobnik
  a = zDS()
  b = zDS()
  grup()
  c = zDS()
  doDS(b)
  split()
  parse(a)
  grup()
  d = zDS()
  doDS(c)
  split()
  doDS(d)  

def map_(): #aplikuje funkciu v a na vsetky prvky v b
  a = zDS()
  b = zDS()
  vysledok = []
  for token in vratToken(b):
    doDS(token)
    parse(a)
    vysledok.append(zDS())
  doDS(' '.join(vysledok))

def foldl(): #aplikuje funkciu v a na prvky v c postupne z lava, zaciatocna hodnota je v b
  a = zDS()
  b = zDS()
  c = zDS()
  doDS(b)
  for token in vratToken(c):
    doDS(token)
    parse(a)

def foldr(): #aplikuje funkciu v a na prvky v c postupne z prava, zaciatocna hodnota je v b
  a = zDS()
  b = zDS()
  reverse()
  c = zDS()
  vysledok = []
  doDS(b)
  for token in vratToken(c):
    doDS(token)
    parse(a)

def filter_(): #vytvori postupnost z prvkov v b ak splnaju podmienku v A
  a = zDS()
  b = zDS()
  vysledok = []
  for token in vratToken(b):
    doDS(token)
    parse(a)
    if zDS() == 'true':
      vysledok.append(token)
  doDS(' '.join(vysledok))

def import_(): #importuje prikazy z externeho suboru
  #global namespace
  a = zDS()
  #namespace = a
  a = a + '.cmr'
  source = ''
  try:
    s = open(a, encoding='utf-8') #otvori subor na citanie
    try:
      source = s.read() #nacita subor
    finally:
      s.close() #zatvori subor
  except IOError as e:
    raise Vynimka(hlasky[7]) 
  if source: #ak bol nacitany subor
    parse(source)
  #namespace = None

def define(): #zadefinuje novu funkciu v userDictionary alebo funkciu vymaze
  global userDictionary
  a = zDS()
  #if namespace: #ak je to definicia funkcie z nejakeho namespace, predpojim nazov toho namespace pred nazov funkcie
    #a = namespace + '.' + a
  b = zDS()
  if b:
    if a in userDictionary:
      userDictionary[a].append(b) #prida nove telo na koniec listu
    else:
      userDictionary[a] = [b] #vytvori novy list
  else:
    if a in userDictionary:
      if len(userDictionary[a]) > 1:
        del userDictionary[a][-1] #vymaze naposledy pridane telo funkcie
      else:
        del userDictionary[a]

def show(): #vrati vnutro funkcie v userDictionary
  a = zDS()
  if a in userDictionary:
    doDS(userDictionary[a])
  elif a in sysDictionary:
    doDS(sysDictionary[a])

def exist(): #zisti, ci funkcia s danym menom existuje v nejakom slovniku
  a = zDS()
  if a in userDictionary or a in sysDictionary or a in coreDictionary:
    doDS('true')
  else:
    doDS('false')

def empty(): #zisti, ci je zasobnik prazdny
  a = len(dataStack)
  if a == 0:
    doDS('true')
  else:
    doDS('false')

def cleard(): #vymaze dataStack
  global dataStack
  dataStack = []

def clearh(): #vymaze helpStack
  global helpStack
  helpStack = []

def del_(): #reinicializuje uzivatelsky slovnik
  global userDictionary
  userDictionary = copy.deepcopy(userDictionary_orig)

def height(): #zisti hlbku zasobnika dataStack
  l = len(dataStack)
  doDS(str(l))

def print_(): #vypise vrchny prvok v zasobniku dataStack na obrazovku bez noveho riadku
  a = zDS()
  print(a, end='')

def read(): #nacita prvok z klavesnice
  text = zDS()
  doDS(input(text))

coreDictionary = {
  'mov':mov, #presunie vrchny prvok v dataStack na vrch helpStack
  'rem':rem, #presunie vrchny prvok v helpStack na vrch dataStack
  'dup':dup, #duplikuje vrchny prvok
  'swap':swap, #vymeni dva vrchne prvky
  'drop':drop, #vymaze vrchny prvok
  'over':over, #skopiruje druhy prvok na vrch
  'wrap':wrap, #zabali vrchny prvok do zatvoriek
  'i':i,
  's\'':sc,
  'j':j,
  'j\'':jc,
  'cons':cons, #pripoji vrchny prvok na koniec sekvencie
  'uncons':uncons, #rozlozi vrchnu sekvenciu na first a rest
  'first':first, #vrati prvy prvok v sekvencii najvyssieho prvku
  'last':last, #vrati posledny prvok v sekvencii najvyssieho prvku
  'rest':rest, #vrati vsetky prvky v sekvencii okrem prveho prvku v najvyssom prvku
  'split':split, #rozdeli vrchny prvok na viacero prvkov
  'grup':grup, #spoji vsetky prvky v zasobniku do sekvencie
  'flat':flat, #odstrani vsetky zatvorky z vrchneho prvku
  'cat':cat, #spoji dva vrchne prvky bez medzery
  'size':size, #vrati pocet prvkov v sekvencii v najvyssom prvku
  'reverse':reverse, #prevrati postupnost prvkov vo vrchnej sekvencii
  '+':add,
  '-':sub,
  '*':mul,
  '**':exp,
  '/':div,
  '//':divint,
  '%':mod,
  '/%':divmod_,
  'and':and_,
  'or':or_,
  'not':not_,
  'xor':xor_,
  'min':min_,
  'max':max_,
  'abs':abs_,
  'sign':sign,
  'map':map_, #aplikuje funkciu a na kazdy prvok v b
  'foldl':foldl, #aplikuje binarnu funkciu a postupne na vsetky prvky v b z lava
  'foldr':foldr, #aplikuje binarnu funkciu a postupne na vsetky prvky v b z prava
  'filter':filter_, #vytvori sekvenciu z prvkov b ak splnaju podmienku v a
  'import':import_, #importuje slovnik funkcii s nazvom v najvyssom prvku (subor bez koncovky .cmr)
  'del':del_, #vymaze uzivatelsky slovnik funkcii
  'exist':exist, #ak funkcia a existuje v nejakom slovniku vrati true, inak vrati false
  'print':print_, #vypise na obrazovku vrchny prvok
  'read':read, #nacita prvok z klavesnice
  'empty':empty, #zisti, ci je zasobnik prazdny
  'cleard':cleard, #vyprazdni dataStack
  'clearh':clearh, #vyprazdni helpStack
  'height':height, #zisti hlbku zasobnika
  'list':list_, #vytvori sekvenciu cisel od n1 po n2 (vratane krajnych hodnot)
  'infra':infra, #vykona funkciu tak, ze za zasobnik povazuje sekvenciu b
  'show':show, #vratenie vnutrajska funkcie
  '=':rovne,
  '!=':nerovne,
  '<':mensie,
  '>':vacsie,
  '<=':mensierovne,
  '>=':vacsierovne,
  'def':define, #vytvori podprogram
  'if':if_, #porovna dva prvky v dataStack a vykona patricnu operaciu [<][=][>]
  'ift':ift, #vykona podprogram, ak hodnota bude true
  'ifte':ifte, #vykona podprogram1, ak je hodnota true, inak vykona podprogram2
  'while':while_, #vykona podprogram, kym je podmienka true
  'times':times, #vykona podprogram zadany pocet krat
  'for':for_, #vykona podprogam stop-start krat
  'fors':fors #vykona podprogam od start po stop po krokoch
}

sysDictionary = {
  'dup2':'[dup] dip', #zduplikuje druhy najvyssi prvok
  '2dup':'[dup] dip dup [swap] dip', #zduplikuje vrchne dva prvky
  'swap2':'[swap] dip', #vymeni druhy a treti prvok
  '2swap':'[swap] dip swap [[swap] dip swap] dip', #vymeni treti a stvrty prvok s prvym a druhym prvkom
  'drop2':'[drop] dip', #vymaze druhy najvyssi prvok
  '2drop':'drop drop', #vymaze dva vrchne prvky
  'over2':'[over] dip', #skopiruje treti prvok od vrchu pod prvy prvok
  '2over':'[over] dip swap [over] dip swap', #skopiruje druhy a treti prvok na vrch
  'burry':'swap over', #skopiruje vrchny prvok pod druhy prvok
  'rold':'[swap] dip swap', #orotuje trojicu vrchnych prvkov smerom nadol
  'rolu':'swap [swap] dip', #orotuje trojicu vrchnych prvkov smerom nahor
  'flip':'swap [swap] dip swap', #zmeni poradie vrchnych troch prvkov
  'rep':'dup [i] dip i', #vyberie a a potom vykona dvakrat a
  'poke':'[[drop] dip] dip swap', #vymaze treti prvok od vrchu a vymeni poradie vrchnych dvoch
  'dip':'swap mov i rem', #odstrani b, vykona a a nasledne b da na vrch
  '2dip':'wrap dip [dip] dip', #odstrani c, b, vykona a a nasledne c, b vrati na vrch
  'sip':'over mov i rem', #skopiruje b, vykona a a ulozi b na vrch
  '2sip':'[over] dip swap [over] dip swap wrap dip [dip] dip', #skopiruje c, b, vykona a a ulozi c, b na vrch
  'sap':'swap [i] dip i', #vyberie a, b, vykona a, potom vykona b
  'swat':'swap cons', #pripoji druhy prvok od vrchu na koniec sekvencie
  'unswat':'reverse uncons reverse', #rozlozi vrchnu sekvenciu na last a rest
  'curry':'[wrap] dip cons', #spoji prvky a a b tak, ze prvok b vlozi v zatvorkach pred prvok a
  '2curry':'curry curry', #spoji prvky a, b, c tak, ze prvky c, b vlozi v zatvorkach pred a
  'uncurry':'dup [first i] dip rest', #rozpoji prvky tak, ze prvy prvok sekvencie oddeli od zvysku a odzatvorkuje ho
  'take':'curry reverse', #spoji dva prvky tak, ze druhy prvok vlozi v zatvorkach na koniec sekvencie
  'cake':'curry dup reverse', #skombinuje curry a take
  'coup':'[curry] dip dup', #treti prvok vlozi v zatvorkach na zaciatok druhej sekvencie a zduplikuje vrchny prvok
  'bi':'[sip] dip i', #aplikuje b na c a nasledne a na c
  'bi*':'[dip] dip i', #aplikuje b na d a nasledne a na c
  'bi@':'dup [dip] dip i', #aplikuje a na c a nasledne a na b
  'tri':'[[sip] dip sip] dip i', #aplikuje c na d, nasledne b na d, a nasledne a na d
  'tri*':'[[wrap dip [dip] dip] dip dip] dip i', #aplikuje c na f, nasledne b na e, a nasledne a na d
  'tri@':'dup dup [[wrap dip [dip] dip] dip dip] dip i', #aplikuje a na d, nasledne a na c a nasledne a na b
  'm':'dup i',
  'z':'drop i',
  't':'swap i',
  'w':'[dup] dip i',
  'k':'[drop] dip i',
  'c':'[swap] dip i',
  'b':'[curry] dip i',
  'b\'':'swap [curry] dip i',
  'd':'[[curry] dip] dip i ',
  'l':'[dup curry] dip i',
  'o':'[dup] dip swap [curry] dip i',
  'p':'[swap] dip swap i',
  'q':'swap [curry] dip i',
  'q\'':'curry swap i',
  'r':'swap [swap] dip i',
  's':'[[dup] dip swap [curry] dip] dip i',
  'v':'[swap] dip swap i',
  'e':'[[[[wrap] dip wrap cons] dip cons] dip] dip i',
  'fix':'[dup curry] swap cons dup curry',
  'y':'fix i',
  'u':'dup curry over [curry] dip i',
  'println':'[\n] cat print'
}

userDictionary_orig = {
  'fact':['[[dup 1 <=] dip swap [drop drop 1] [[dup 1 -] dip i *] ifte] y'],
  'fibo':['[[dup 2 <] dip swap [drop] [[1 - dup 1 -] dip bi@ +] ifte] y'],
  'gcd':['[[dup 0 =] dip swap [drop drop] [[swap over %] dip i] ifte] y'],
  'lcm':['over over gcd [* abs] dip //'],
  'trin':['dup [1 +] dip * 2 /']
}

userDictionary = copy.deepcopy(userDictionary_orig)

def vratToken(retazec):
  token = ''
  zatvoriek = 0
  uvodzovky = False
  komentar = False

  retazec = retazec.strip()

  if retazec == '': #je to prazdny token?
    return
  for znak in retazec: #pre kazdy znak v retazci
    if znak == '[' and not uvodzovky and not komentar: #je to otvaracia zatvorka mimo uvodzoviek a komentara?
      zatvoriek += 1 #poznaci si otvaraciu zatvorku
      if zatvoriek == 1 and len(token) > 0: #je to otvaracia zatvorka pre nasledujuci token?
        yield token
        token = ''
      token += znak

    elif znak == ']' and not uvodzovky and not komentar: #je to uzatvaracia zatvorka mimo uvodzoviek a komentara?
      zatvoriek -= 1
      token += znak
      if zatvoriek == 0: #je to ukoncovacia zatvorka aktualneho tokenu?
        yield token
        token = ''
      elif zatvoriek < 0:
        raise Vynimka(hlasky[5]) #Vynimka poctu zatvoriek

    elif znak == '"' and zatvoriek == 0 and not komentar: #je to zaciatok alebo koniec viacslovneho retazca mimo zatvoriek a komentara
      uvodzovky = not uvodzovky
      if uvodzovky and len(token) > 0: #je to otvaracia uvodzovka pre nasledujuci token?
        yield token
        token = ''
      token += znak
      if not uvodzovky:
        yield token
        token = ''

    elif znak.isspace() and zatvoriek == 0 and not uvodzovky and not komentar: #je to prazdny znak mimo zatvoriek, uvodzoviek a komentara?
      if len(token) > 0: #je uz nieco v tokene?
        yield token
        token = ''

    elif znak == '#' or (znak == '\n' and komentar): # je to znak zacinajuci komentar alebo znak konca riadku v komentari XXX: and zatvoriek == 0 and not uvodzovky: #je to znak zacinajuci komentar mimo zatvoriek a uvodzoviek?
      komentar = not komentar

    else: #je to iny token ako zatvorky, uvodzovky, prazdny znak alebo komentar?
      if not komentar: #je to znak mimo komentara?
        token += znak
  else:
    if len(token) > 0:
      yield token

def parse(retazec):
  for token in vratToken(retazec):
    print('d:', dataStack)
    print('t:', token)
    if token in userDictionary: #je token v userDictionary?
      parse(userDictionary[token][-1])
    elif token in sysDictionary: #je token v sysDictionary?
      parse(sysDictionary[token])
    elif token in coreDictionary: #je token v coreDictionary?
      coreDictionary[token]()
    elif token[0] == '[' and token[-1] == ']': #je token v zatvorkach?
      doDS(token[1:-1])
    elif token[0] == '"' and token[-1] == '"': #je token v uvodzovkach?
      doDS(token[1:-1])
    else: #je to nieco ine
      doDS(token)

def run(subor):
  global dataStack, helpStack
  if not subor:
    print('Nebol zadaný vstupný súbor s programom alebo program.')
    return
  source = ''
  try:
    s = open(subor, encoding='utf-8') #otvori subor na citanie
    try:
      source = s.read() #nacita subor
    finally:
      s.close() #zatvori subor
  except IOError as e:
    source = subor
  if source: #ak bol nacitany subor
    dataStack = []
    helpStack = []
    try:
      parse(source)
    except Vynimka as e:
      print(e)
    print('dataStack:', dataStack)
    print('helpStack:', helpStack)

def demo():
  run('Documents/zdrojaky/python/prog.cmr')

if __name__ == '__main__':
  demo()
