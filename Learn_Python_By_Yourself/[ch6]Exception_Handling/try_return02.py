def write_text_file(filename, text):
  try:
    file = open(filename, "w")
    return
    file.write(text)
  except Exception as e:
    print(e)
  finally:
    file.close()

write_text_file("test.txt", "It's file write test code")
