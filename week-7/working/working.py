import re


def main():
  print(convert(input("Hours: ")))


def convert(s):
  if matches := re.match(r"(\d{1,2})(?::(\d{1,2}))? (AM|PM) to (\d{1,2})(?::(\d{1,2}))? (AM|PM)", s):
    start_hr, start_min, start_ap, end_hr, end_min, end_ap = matches.groups()
    start_min = 0 if start_min is None else int(start_min)
    end_min = 0 if end_min is None else int(end_min)
    start_hr = int(start_hr)
    end_hr = int(end_hr)
    if start_ap == "PM" and start_hr != 12:
        start_hr += 12
    elif start_ap == "AM" and start_hr == 12:
        start_hr = 0
    if end_ap == "PM" and end_hr != 12:
        end_hr += 12
    elif end_ap == "AM" and end_hr == 12:
        end_hr = 0
    if(not 1 <= start_hr <= 12
       or not 0 <= start_min <= 59
       or not 1 <= end_hr <= 12
       or not 0 <= end_min <= 59):
        raise ValueError("Invalid Arguments")
    return f"{start_hr:02d}:{start_min:02d} to {end_hr:02d}:{end_min:02d}"
  raise ValueError("Invalid Arguments")



if __name__ == "__main__":
    main()
