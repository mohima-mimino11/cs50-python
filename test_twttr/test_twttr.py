from twttr import shorten

def test_empty():
  assert shorten(" ") == " "
def test_str_capital():
  assert shorten("Whatever") == "Whtvr"
  assert shorten("What's Your Name?") == "Wht's Yr Nm?"
def test_str_lower():
  assert shorten("whatever") == "whtvr"
  assert shorten("mimino") == "mmn"

def test_str_upper():
  assert shorten("WHATEVER") == "WHTVR"
  assert shorten("MIMINO") == "MMN"

def test_num():
  assert shorten("23") == "23"



