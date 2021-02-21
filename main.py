import argparse

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("file_path", help="ps file output to parse")
    args = argument_parser.parse_args()
    print(args.file_path)