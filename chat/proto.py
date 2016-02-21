#!/usr/bin/python3
import re

person = ['\si\s', '\syou\s', '\she\s', '\sshe\s', '\sit\s', '\sthey\s', '\swe\s']
person_possessive = ['\smy\s', '\smine\s', '\syours\s', '\sours\s', '\stheirs\s', '\shis\s', '\shers\s']
pronoun = ['\sme\s', '\syou\s', '\shim\s', '\sher\s', '\sus\s', '\sthem\s']
verbs = ['\s' + verb.rstrip('\n') for verb in open('verbs.txt')]

pat_person = '(' + '|'.join(person) + ')'
pat_person_possessive = '(' + '|'.join(person_possessive) + ')'
pat_pronoun = '(' + '|'.join(pronoun) + ')'
pat_verb = '(( have )?( not )?(' + '|'.join(verbs) + ')(\s|ed\s)( not )?)'

pat_end = '(.*)\.?'
pat_start = '(.*)'

modal = ['\smust\s', '\sshould\s', '\scould\s', '\scan\s', '\sshall\s', '\swill\s', '\swould\s']
pat_modal = '(' + '|'.join(modal) + ')?'

pat_text = pat_start + '(' +pat_person+ pat_modal +pat_verb + ')' +pat_end
pat = re.compile(pat_text)

pat_question_text = pat_start + pat_verb + pat_person + pat_end
pat_question = re.compile(pat_question_text)

pat_no_person_text = pat_start + '(' + pat_modal + pat_verb + ')' + pat_end
pat_no_person = re.compile(pat_no_person_text)

while True:
  text = ' ' + input()
  text = re.sub(' ', '  ', text)
  print(text)
  match = re.search(pat, text)
  if match:
    n = len(match.groups())
    for i in range(n+1):
      print(i, " : ",  match.group(i))
    result = match.group(1) + ' ' + match.group(11) + ' ' + match.group(2)
    print(result)
    result = re.sub('\s+', ' ', result)
    print(result)
    continue
  match = re.search(pat_question, text)
  if match:
    #question
    n = len(match.groups())
    for i in range(n+1):
      print(i, " : ",  match.group(i))
    result = match.group(6) + ' ' + match.group(2) + ' ' + match.group(5)
    print(result)
    result = re.sub('\s+', ' ', result)
    print(result)
    continue
  match = re.search(pat_no_person, text)
  if match:
    # no person
    n = len(match.groups())
    for i in range(n+1):
      print(i, " : ",  match.group(i))
    result = match.group(10) + ' ' + match.group(2) + ' ' + match.group(1)
    print(result)
    result = re.sub('\s+', ' ', result)
    print(result)
    continue
  print(text)
