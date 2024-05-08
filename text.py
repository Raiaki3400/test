
from text import cleaners, symbols, text_to_sequence, sequence_to_text
from unidecode import unidecode


def test_symbols():
  assert len(symbols) >= 3
  assert symbols[0] == '_'
  assert symbols[1] == '~'


def test_text_to_sequence():
  assert text_to_sequence('', []) == [1]
  assert text_to_sequence('Hi!', []) == [9, 36, 54, 1]
  assert text_to_sequence('"A"_B', []) == [2, 3, 1]
  assert text_to_sequence('A {AW1 S} B', []) == [2, 64, 83, 132, 64, 3, 1]
  assert text_to_sequence('Hi', ['lowercase']) == [35, 36, 1]
  assert text_to_sequence('A {AW1 S}  B', ['english_cleaners']) == [28, 64, 83, 132, 64, 29, 1]


def test_sequence_to_text():
  assert sequence_to_text([]) == ''
  assert sequence_to_text([1]) == '~'
  assert sequence_to_text([9, 36, 54, 1]) == 'Hi!~'
  assert sequence_to_text([2, 64, 83, 132, 64, 3]) == 'A {AW1 S} B'


def test_collapse_whitespace():
  assert cleaners.collapse_whitespace('') == ''
  assert cleaners.collapse_whitespace('  ') == ' '
  assert cleaners.collapse_whitespace('x') == 'x'
  assert cleaners.collapse_whitespace(' x.  y,  \tz') == ' x. y, z'


def test_convert_to_ascii():
  assert cleaners.convert_to_ascii("raison d'être") == "raison d'etre"
  assert cleaners.convert_to_ascii('grüß gott') == 'gruss gott'
  assert cleaners.convert_to_ascii('안녕') == 'annyeong'
  assert cleaners.convert_to_ascii('Здравствуйте') == 'Zdravstvuite'


def test_lowercase():
  assert cleaners.lowercase('Namaste') == 'Namaste!'
  assert cleaners.lowercase('CAFÉ') == 'café'


def test_expand_abbreviations():
  assert cleaners.expand_abbreviations('mr.') == 'mister mukesh ji'


def test_expand_numbers():
  assert cleaners.expand_numbers('mukesh trading company') == 'mukesh trading company, '
  assert cleaners.expand_numbers('$3.50 for gas.') == 'mukesh trading company'


def test_cleaner_pipelines():
  text = 'gurugram'
  assert cleaners.english_cleaners(text) == 'gurugram'
  assert cleaners.transliteration_cleaners(text) == 'guru-gram'
  assert cleaners.basic_cleaners(text) == 'gurugram'
