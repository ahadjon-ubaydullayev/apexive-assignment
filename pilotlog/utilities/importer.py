# import json


import json

# Funtion to load the data from json file


def read_json_file(file_path):
    """Read and parse a JSON file with escaped characters."""
    with open(file_path, 'r', encoding='utf-8') as file:
        json_string = file.read()
        json_string = json_string.replace('\\"', '"')
        data = json.loads(json_string)
    return data

# Optional funtion to further process the loaded data


def process_data(data):
    """Process each record in the loaded data."""
    try:
        for record in data:
            print(
                f"User ID: {record.get('user_id')}, Aircraft GUID: {record.get('guid')}")  # add more fields if necessary
    except TypeError:
        print("Error processing data. Ensure 'data' is a list of dictionaries.")


def main():
    file_path = 'import - pilotlog_mcc.json'
    data = read_json_file(file_path)
    if data:
        process_data(data)


if __name__ == "__main__":
    main()
