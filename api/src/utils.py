import os

def delete_images_in_directory(directory_path):
    """
    Delete all PNG images in the specified directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        None
    """
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(".png"):
                file_path = os.path.join(directory_path, filename)
                os.remove(file_path)
                print(f"Deleted image: {filename}")
    except Exception as e:
        print(f"Error while deleting images: {str(e)}")

def get_population(country_dict):
    """
    Extract population data from a country dictionary using pandas.

    Args:
        country_dict (dict): A dictionary containing population data.

    Returns:
        tuple: A tuple containing two lists - labels and values.
            - labels (list): A list of years.
            - values (list): A list of corresponding population values.
    """
    labels = []
    values = []
    for label, value in country_dict.items():
        if 'Population' in label:
            year = label.split(' ')[0]
            if year.isdigit():
                population_value = int(value)
                labels.append(year)
                values.append(population_value)
    return labels, values

def population_by_country(data, country):
    """
    Get population data for a specific country from the dataset.

    Args:
        data (DataFrame): The dataset containing country information.
        country (str): The name of the country.

    Returns:
        DataFrame: A DataFrame containing population data for the specified country.
    """
    result = data[data['Country'] == country]
    return result