#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import decimal
import copy
from vynimky import Vynimka

dataStack = None
helpStack = None
namespace = None
hlasky = ['\nVynimka v programe!',
          '\nZásobník dataStack je prázdny!',
          '\nZásobník helpStack je prázdny!',
          '\nZlý formát prvku v dataStack!',
          '\nIndex mimo rozsah vstupného reťazca!',
          '\nNesprávny počet zátvoriek!',
          '\nNesprávny počet apostrofov!',
          '\nSúbor nenájdený!']

def zDS():
  global dataStack
  try:
    x = dataStack.pop()
  except IndexError:
    raise Vynimka(hlasky[1])
  return x

def doDS(x):
  global dataStack
  dataStack.append(str(x))

def zHS():
  global helpStack
  try:
    x = helpStack.pop()
  except IndexError:
    raise Vynimka(hlasky[2])
  return x

def doHS(x):
  global helpStack
  helpStack.append(str(x))

def mov():
  a = zDS()
  doHS(a)

def rem():
  a = zHS()
  doDS(a)

def dup():
  a = zDS()
  doDS(a)
  doDS(a)

def swap():
  a = zDS()
  b = zDS()
  doDS(a)
  doDS(b)

def drop():
  zDS()

def over():
  a = zDS()
  b = zDS()
  doDS(b)
  doDS(a)
  doDS(b)

def dip():
  a = zDS()
  b = zDS()
  parse(a)
  doDS(b)

def _dip():
  a = zDS()
  b = zDS()
  c = zDS()
  parse(a)
  doDS(c)
  doDS(b)

def sip():
  a = zDS()
  b = zDS()
  doDS(b)
  parse(a)
  doDS(b)

def _sip():
  a = zDS()
  b = zDS()
  c = zDS()
  doDS(c)
  doDS(b)
  parse(a)
  doDS(c)
  doDS(b)

def sap():
  a = zDS()
  b = zDS()
  parse(a)
  parse(b)

def wrap():
  a = zDS()
  a = '[' + a + ']'
  doDS(a)

def bi():
  a = zDS()
  b = zDS()
  c = zDS()
  doDS(c)
  parse(b)
  doDS(c)
  parse(a)

def bi_():
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  doDS(d)
  parse(b)
  doDS(c)
  parse(a)

def _bi():
  a = zDS()
  b = zDS()
  c = zDS()
  doDS(c)
  parse(a)
  doDS(b)
  parse(a)

def tri():
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  doDS(d)
  parse(c)
  doDS(d)
  parse(b)
  doDS(d)
  parse(a)

def tri_():
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  e = zDS()
  f = zDS()
  doDS(f)
  parse(c)
  doDS(e)
  parse(b)
  doDS(d)
  parse(a)

def _tri():
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  doDS(d)
  parse(a)
  doDS(c)
  parse(a)
  doDS(b)
  parse(a)

def i():
  a = zDS()
  parse(a)

def sc():
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  doDS('[' + d + ']' + ' ' + c)
  parse(a)
  doDS(d)
  parse(b)

def j():
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  doDS('[' + c + ']' + ' ' + '[' + d + ']' + a)
  doDS(b)
  parse(a)

def jc():
  a = zDS()
  b = zDS()
  c = zDS()
  d = zDS()
  e = zDS()
  doDS('[' + d + ']' + ' ' + a + '[' + e + ']' + b)
  doDS(c)
  parse(b)

def curry():
  a = zDS()
  b = zDS()
  doDS('[' + b + ']' + ' ' + a)

def cons():
  a = zDS()
  b = zDS()
  doDS(b + ' ' + a)

def uncons():
  a = zDS()
  doDS(a)
  first()
  doDS(a)
  rest()

def first():
  a = zDS()
  for token in vratToken(a):
    doDS(token)
    break

def last():
  a = zDS()
  for token in vratToken(a):
    pass
  doDS(token)

def rest():
  a = zDS()
  vysledok = []
  for token in vratToken(a):
    vysledok.append(token)
  del vysledok[0]
  doDS(' '.join(vysledok))

def split():
  a = zDS()
  for token in vratToken(a):
    doDS(token)

def grup():
  a = ' '.join(dataStack)
  cleard()
  doDS(a)

def flat():
  a = zDS()
  b = a.replace('[', ' ')
  c = b.replace(']', ' ')
  doDS(c)
  
def cat():
  a = zDS()
  b = zDS()
  doDS(b + a)

def size():
  a = zDS()
  vysledok = []
  for token in vratToken(a):
    vysledok.append(token)
  doDS(len(vysledok))

def reverse():
  a = zDS()
  vysledok = []
  for token in vratToken(a):
    vysledok.append(token)
  doDS(' '.join(reversed(vysledok)))

def add():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b+a)

def sub():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b-a)

def mul():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b*a)

def exp():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b**a)

def div():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b/a)

def divint():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b//a)

def mod():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b%a)

def divmod_():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(b//a)
  doDS(b%a)

def and_():
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

def or_():
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

def xor_():
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

def not_():
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

def min_():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(min(a, b))

def max_():
  a = zDS()
  b = zDS()
  try:
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
  except:
    raise Vynimka(hlasky[3])
  doDS(max(a, b))

def abs_():
  a = zDS()
  try:
    a = decimal.Decimal(a)
  except:
    raise Vynimka(hlasky[3])
  doDS(abs(a))

def sign():
  a = zDS()
  try:
    a = decimal.Decimal(a)
  except:
    raise Vynimka(hlasky[3])
  doDS((a >= 0) - (a < 0))
    
def if_():
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

def ift():
  a = zDS()
  b = zDS()
  if b == 'true':
    parse(a)

def ifte():
  a = zDS()
  b = zDS()
  c = zDS()
  if c == 'true':
    parse(b)
  else:
    parse(a)

def times():
  a = zDS()
  b = zDS()
  try:
    a = int(a)
  except:
    raise Vynimka(hlasky[3])
  for i in range(a):
    parse(b)

def for_():
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

def fors():
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

def while_():
  a = zDS()
  b = zDS()
  while True:
    parse(b)
    c = zDS()
    if c == 'true':
      parse(a)
    else:
      break

def rovne():
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

def nerovne():
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

def vacsie():
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

def mensie():
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

def vacsierovne():
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

def mensierovne():
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

def list_():
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

def infra_old():
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

def infra():
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

def map_():
  a = zDS()
  b = zDS()
  vysledok = []
  for token in vratToken(b):
    doDS(token)
    parse(a)
    vysledok.append(zDS())
  doDS(' '.join(vysledok))

def foldl():
  a = zDS()
  b = zDS()
  c = zDS()
  doDS(b)
  for token in vratToken(c):
    doDS(token)
    parse(a)

def foldr():
  a = zDS()
  b = zDS()
  reverse()
  c = zDS()
  vysledok = []
  doDS(b)
  for token in vratToken(c):
    doDS(token)
    parse(a)

def filter_():
  a = zDS()
  b = zDS()
  vysledok = []
  for token in vratToken(b):
    doDS(token)
    parse(a)
    if zDS() == 'true':
      vysledok.append(token)
  doDS(' '.join(vysledok))

def import_():
  global namespace
  a = zDS()
  namespace = a
  a = a + '.cmr'
  source = ''
  try:
    s = open(a, encoding='utf-8')
    try:
      source = s.read()
    finally:
      s.close()
  except IOError as e:
    raise Vynimka(hlasky[7]) 
  if source:
    parse(source)
  namespace = None

def define():
  global userDictionary
  a = zDS()
  if namespace:
    a = namespace + '.' + a
  b = zDS()
  if b:
    if a in userDictionary:
      userDictionary[a].append(b)
    else:
      userDictionary[a] = [b]
  else:
    if a in userDictionary:
      if len(userDictionary[a]) > 1:
        del userDictionary[a][-1]
      else:
        del userDictionary[a]

def show():
  a = zDS()
  if a in userDictionary:
    doDS(userDictionary[a])
  elif a in sysDictionary:
    doDS(sysDictionary[a])

def exist():
  a = zDS()
  if a in userDictionary or a in sysDictionary or a in coreDictionary:
    doDS('true')
  else:
    doDS('false')

def empty():
  a = len(dataStack)
  if a == 0:
    doDS('true')
  else:
    doDS('false')

def cleard():
  global dataStack
  dataStack = []

def clearh():
  global helpStack
  helpStack = []

def del_():
  global userDictionary
  userDictionary = copy.deepcopy(userDictionary_orig)

def height():
  l = len(dataStack)
  doDS(str(l))

def print_():
  a = zDS()
  print(a, end='')

def read():
  text = zDS()
  doDS(input(text))

coreDictionary = {
  'mov':mov,
  'rem':rem,
  'dup':dup,
  'swap':swap,
  'drop':drop,
  'over':over,
  'bi':bi,
  'bi*':bi_,
  'bi@':_bi,
  'tri':tri,
  'tri*':tri_,
  'tri@':_tri,
  'dip':dip,
  '2dip':_dip,
  'sip':sip,
  '2sip':_sip,
  'sap':sap,
  'wrap':wrap,
  'i':i,
  's\'':sc,
  'j':j,
  'j\'':jc,
  'curry':curry,
  'cons':cons,
  'uncons':uncons,
  'first':first,
  'last':last,
  'rest':rest,
  'split':split,
  'grup':grup,
  'flat':flat,
  'cat':cat,
  'size':size,
  'reverse':reverse,
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
  'map':map_,
  'foldl':foldl,
  'foldr':foldr,
  'filter':filter_,
  'import':import_,
  'del':del_,
  'exist':exist,
  'print':print_,
  'read':read,
  'empty':empty,
  'cleard':cleard,
  'clearh':clearh,
  'height':height,
  'list':list_,
  'infra':infra,
  'show':show,
  '=':rovne,
  '!=':nerovne,
  '<':mensie,
  '>':vacsie,
  '<=':mensierovne,
  '>=':vacsierovne,
  'def':define,
  'if':if_,
  'ift':ift,
  'ifte':ifte,
  'while':while_,
  'times':times,
  'for':for_,
  'fors':fors
}

sysDictionary = {
  'dupd':'[dup] dip',
  'swapd':'[swap] dip',
  'dropd':'[drop] dip',
  'overd':'[over] dip',
  '2over':'overd swap',
  'burry':'swap over',
  'rold':'[swap] dip swap',
  'rolu':'swap [swap] dip',
  'rotate':'swap [swap] dip swap',
  'w':'[dup] dip i',
  'k':'[drop] dip i',
  'b':'[curry] dip i',
  'c':'[swap] dip i',
  'l':'[dup curry] dip i',
  'm':'dup i',
  'o':'[dup] dip swap [curry] dip i',
  'q':'swap [curry] dip i',
  'q\'':'curry swap i',
  'r':'rolu i',
  's':'[[dup] dip swap [curry] dip] dip i',
  't':'swap i',
  'v':'rold i',
  'fix':'[dup curry] swap cons dup curry',
  'y':'fix i',
  'u':'dup curry over [curry] dip i',
  'printn':'[\n] cat print'
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
  apostrofy = False
  komentar = False

  retazec = retazec.strip()

  if retazec == '':
    return
  for znak in retazec:
    if znak == '[' and not apostrofy and not komentar:
      zatvoriek += 1
      if zatvoriek == 1 and len(token) > 0:
        yield token
        token = ''
      token += znak

    elif znak == ']' and not apostrofy and not komentar:
      zatvoriek -= 1
      token += znak
      if zatvoriek == 0:
        yield token
        token = ''
      elif zatvoriek < 0:
        raise Vynimka(hlasky[5])

    elif znak == "'" and zatvoriek == 0 and not komentar:
      apostrofy = not apostrofy
      if apostrofy and len(token) > 0:
        yield token
        token = ''
      token += znak
      if not apostrofy:
        yield token
        token = ''

    elif znak.isspace() and zatvoriek == 0 and not apostrofy and not komentar:
      if len(token) > 0:
        yield token
        token = ''

    elif znak == '#' or (znak == '\n' and komentar): # XXX: and zatvoriek == 0 and not apostrofy:
      komentar = not komentar

    else:
      if not komentar:
        token += znak
  else:
    if len(token) > 0:
      yield token

def parse(retazec):
  for token in vratToken(retazec):
    print('d:', dataStack)
    print('t:', token)
    if token in userDictionary:
      parse(userDictionary[token][-1])
    elif token in sysDictionary:
      parse(sysDictionary[token])
    elif token in coreDictionary:
      coreDictionary[token]()
    elif token[0] == '[' and token[-1] == ']':
      doDS(token[1:-1])
    elif token[0] == '"' and token[-1] == '"':
      doDS(token[1:-1])
    else:
      doDS(token)

def run(subor):
  global dataStack, helpStack
  if not subor:
    print('Nebol zadaný vstupný súbor s programom alebo program.')
    return
  source = ''
  try:
    s = open(subor, encoding='utf-8')
    try:
      source = s.read()
    finally:
      s.close()
  except IOError as e:
    source = subor
  if source:
    dataStack = []
    helpStack = []
    try:
      parse(source)
    except Vynimka as e:
      print(e)
    print('dataStack:', dataStack)
    print('helpStack:', helpStack)

def demo():
  run('prog.cmr')

if __name__ == '__main__':
  demo()
