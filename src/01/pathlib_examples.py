import os
import shutil
from pathlib import Path

read_file = Path("read_file.txt")
write_file = Path("write_file.txt")

text = read_file.read_text()
print(f"Writing copy of '{read_file}' to '{write_file}', text: {text}")
write_file.write_text(text)

print(read_file.resolve())
print(read_file.absolute())
print(read_file.as_posix())

downloads = Path(Path(Path.home()/ "Downloads").resolve())
documents = Path("../01")

weird_concat = downloads / documents
# https://discuss.python.org/t/pathlib-absolute-vs-resolve/2573/10
# When several absolute paths are given, the last is taken as an anchor (mimicking os.path.join() ’s behaviour)

print(downloads)
print(documents)
print(weird_concat.exists())

print(Path.cwd())
print("---")
p = Path("~/Downloads")
print(p.expanduser())
print(p.absolute())
print(p.resolve())
file = p.resolve() / "file.txt"

print("---")
to_write = Path("./to_write.txt")
to_write.touch()
to_write.write_text("hello world")

# Create Path
p = Path("file.txt")  # >> file.txt, verhält sich wie ein string
p.touch()
p.write_text("Hello World")
abs_path = p.absolute()
text = p.read_text()  # >> "Hello World"
print(text)
print(abs_path)

print(Path.cwd())

p1 = Path("cwd_file.txt")
print(p1.absolute())
p_abs = Path(p1.absolute())
os.chdir("../02")
print("---")
print(p_abs)
print(p1.absolute())



