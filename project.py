import argparse

def main():
    parser = argparse.ArgumentParser(description="Convert data between .xml, .json, and .yml formats")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    input_format = input_file.split('.')[-1]
    output_format = output_file.split('.')[-1]

    data = read_data(input_file, input_format)
    if data is not None:
        write_data(data, output_file, output_format)

if __name__ == "__main__":
    main()
