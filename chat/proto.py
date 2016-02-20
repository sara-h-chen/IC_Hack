import re

person = ['i', 'you', 'he', 'she', 'it', 'they', 'we']
person_possessive = ['my', 'mine', 'yours', 'ours', 'theirs', 'his', 'hers']
pronoun = ['me', 'you', 'him', 'her', 'us', 'them']
verbs = ['\s' + verb.rstrip('\n') + '\s' for verb in open('verbs.txt')]

pat_person = '(' + '|'.join(person) + ')'
pat_person_possessive = '(' + '|'.join(person_possessive) + ')'
pat_pronoun = '(' + '|'.join(pronoun) + ')'
pat_verb = '(' + '|'.join(verbs) + ')'

pat_end = '(.*)\.?'
pat_start = '(.*)'

pat_text = pat_start + '(' +pat_person+pat_verb + ')' +pat_end
pat = re.compile(pat_text)

while True:
  text = input()
  match = re.search(pat, text)
  if match:
    #print(match.groups())
    offset = 0
    if not match.group(5):
      # no 'to'
      offset = 1
    print(match.group(1) + ' ' + match.group(5+offset) + ' ' + match.group(2))
