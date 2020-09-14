#!/usr/bin/env python3
import argparse
import csv
import json


def parse_csv(input_file: str, tsv=False) -> list():
    """
    Args
    :input_file Path to a CSV file. CSV file MUST have headers, or this doesn't make sense.
    Returns
    :output_list A list of dictionaries representing the CSV that was read
    """
    output_list = list()
    with open(input_file, 'r') as file_handle:
        if tsv:
            reader = csv.DictReader(file_handle, delimiter='\t')
        else:
            reader = csv.DictReader(file_handle)
        for row in reader:
            output_list.append(row)
    return output_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', required=True, help='Input CSV file')
    parser.add_argument('-t', required=False, action='store_true', help="Convert TSV to JSON instead of CSV.")
    parser.add_argument('--to-stdout', required=False, action='store_true', help='Write output to console')
    parser.add_argument('-o', required=False, help='Output JSON file')
    args = parser.parse_args()

    input_file = args.i
    output_file = args.o
    is_tsv = args.t
    to_stdout = args.to_stdout

    parsed_csv_data = parse_csv(input_file, tsv=is_tsv)

    if to_stdout is True:
        print(json.dumps(parsed_csv_data, indent=4, sort_keys=True))

    if output_file is not None:
        with open(output_file, 'w') as file_handle:
            json.dump(parsed_csv_data, file_handle)


if __name__ == '__main__':
    main()
