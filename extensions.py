# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

#     .gif
#     .jpg
#     .jpeg
#     .png
#     .pdf
#     .txt
#     .zip

# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

# Asks user for the file name
file_name = input("File name: ").strip().lower()

# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:.gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default
if file_name.endswith((".gif", ".jpg", ".jpeg", ".png")):
  print("image/" + file_name.split(".")[-1].replace("jpg", "jpeg"))
elif file_name.endswith((".pdf", ".zip")):
  print("application/" + file_name.split(".")[-1])
elif file_name.endswith(".txt"):
  print("text/plain")
else:
  print("application/octet-stream")


