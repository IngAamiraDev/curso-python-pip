
def get_population(country_dict):
    """
    Extracts population data from a country dictionary using pandas.

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
            if year.isdigit(): # Check if 'year' is a valid integer
                population_value = int(value)
                labels.append(year)
                values.append(population_value)
    return labels, values

def population_by_country(data, country):
    """
    Retrieve population data for a specific country from a dataset.

    Args:
        data (list of dict): The dataset containing country information.
        country (str): The name of the country to retrieve population data for.

    Returns:
        list: A list of dictionaries containing population data for the specified country.
    """
    result = data[data['Country'].str.contains(country, case=False)]
    return result