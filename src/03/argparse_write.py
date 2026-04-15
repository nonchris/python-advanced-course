# example how to execute:
# python3 argparse_write.py output.txt -s "Hello, world!" -n 5
import argparse

def write_lines_to_file(file_path, sentence, num_lines):
    with open(file_path, "w") as file:
        file.write("\n".join([sentence] * num_lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Write lines to a file")
    # positional (first) parameter
    parser.add_argument("file", type=str, help="file path to write to")
    # required named parameter
    parser.add_argument("-s", "--sentence", type=str, help="sentence to write", required=True)
    # optional named parameter with default value
    parser.add_argument("-n", "--num_lines", type=int, help="number of lines to write", default=1)

    args = parser.parse_args()  # trigger the parsing
    # we receive a class that contains all given parameters as attributes
    # if a --name is given then that's the arguments name not the -name
    write_lines_to_file(args.file, args.sentence, args.num_lines)#
