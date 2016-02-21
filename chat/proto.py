#!/usr/bin/python3
import re

person = ['\si\s', '\syou\s', '\she\s', '\sshe\s', '\sit\s', '\sthey\s', '\swe\s']
person_possessive = ['my\s', 'mine\s', 'yours\s', 'ours\s', 'theirs\s', 'his\s', 'hers\s']
pronoun = ['me\s', 'you\s', 'him\s', 'her\s', 'us\s', 'them\s']
verbs = ['\s' + verb.rstrip('\n') + '\s' for verb in open('verbs.txt')]

pat_person = '(' + '|'.join(person) + ')'
pat_person_possessive = '(' + '|'.join(person_possessive) + ')'
pat_pronoun = '(' + '|'.join(pronoun) + ')'
pat_verb = '(( have )?(' + '|'.join(verbs) + '))'

pat_end = '(.*)\.?'
pat_start = '(.*)'

modal = ['\smust\s', '\sshould\s', '\scould\s', '\scan\s', '\sshall\s', '\swill\s', '\swould\s']
pat_modal = '(' + '|'.join(modal) + ')?'

pat_text = pat_start + '(' +pat_person+ pat_modal +pat_verb + ')' +pat_end
pat = re.compile(pat_text)

while True:
  text = ' ' + input()
  text = re.sub(' ', '  ', text)
  print(text)
  match = re.search(pat, text)
  n = len(match.groups())
  if match:
    #print(match.groups())
    for i in range(n+1):
      print(i, " : ",  match.group(i))
    result = match.group(1) + ' ' + match.group(8) + ' ' + match.group(2)
    print(result)
    result = re.sub('\s+', ' ', result)
    print(result)
  else:
    print(text)
