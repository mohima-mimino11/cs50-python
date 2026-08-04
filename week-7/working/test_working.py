import pytest
from working import convert


def test_hours():
  assert convert("9 AM to 5 PM") == "09:00 to 17:00"
  assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
  assert convert("8 PM to 8 AM") == "20:00 to 08:00"
  assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_invalid_format():
  with pytest.raises(ValueError):
    convert("9 AM 5 PM")          # missing "to"
  with pytest.raises(ValueError):
    convert("9 AM - 5 PM")
  with pytest.raises(ValueError):
    convert("09:00 to 17:00")


def test_invalid_time():
  with pytest.raises(ValueError):
    convert("8:60 AM to 4:60 PM")
  with pytest.raises(ValueError):
    convert("13 AM to 5 PM")
  with pytest.raises(ValueError):
    convert("9 AM to 13 PM")
