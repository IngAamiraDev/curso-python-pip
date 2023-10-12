import csv

def read_csv(path):
    """
    Reads data from a CSV file and returns it as a list of dictionaries.

    Args:
        path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries where each dictionary represents a row in the CSV file.
    """
    try:
        data = []
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                country_dict = dict(zip(header, row))
                data.append(country_dict)
        return data
    except FileNotFoundError:
        print(f"The file {path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {str(e)}")

if __name__ == '__main__':
    data = read_csv('./app/db/data.csv')
    if data:
        print(data[0])