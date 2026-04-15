read_file = "read_file.txt"
write_file = "write_file.txt"
with open(read_file) as f1, open(write_file, "w") as f2:
    text = f1.read()
    print(f"Writing copy of '{read_file}' to '{write_file}', text: {text}")
    f2.write(text)
