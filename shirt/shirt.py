import sys
from PIL import Image, ImageOps



if len(sys.argv) < 2:
  sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
  sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".png"):
  sys.exit("Input and output have different extensions")

if not sys.argv[2].endswith(".jpg") or  sys.argv[2].endswith(".png"):
  sys.exit("Invalid output")


try:
  with Image.open(sys.argv[1]) as img:
    shirt = Image.open("shirt.png")
    size = shirt.size
    img = ImageOps.fit(img, size)
    img.paste(shirt, shirt)
    img.save(sys.argv[2])

except FileNotFoundError:
  sys.exit("Input does not exist")

