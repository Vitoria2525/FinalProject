import argparse
import json

def read_data(file_path, file_format):
    with open(file_path, "r") as file:
        if file_format == "json":
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Invalid JSON format or file does not exist.")
                return None
        elif file_format == "yml" or file_format == "yaml":
            try:
                data = yaml.load(file)
                return data
            except yaml.YAMLError as e:
                print(f"Error while parsing YAML file: {e}")
                return None
        elif file_format == "xml":
            data = ET.parse(file).getroot()
        else:
            print("Unsupported file format.")
            return None

def write_data(data, file_path, file_format):
    with open(file_path, "w") as file:
        if file_format == "json":
            json.dump(data, file)
        elif file_format == "yml" or file_format == "yaml":
            yaml.dump(data, file)
        else:
            raise ValueError("Unsupported file format")

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
