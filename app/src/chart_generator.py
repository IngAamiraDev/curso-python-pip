from src.utils import get_population, population_by_country
from src.charts import generate_bar_chart, generate_pie_chart

def generate_pie_chart_for_continent(data):
    """
    Generate a pie chart for a specific continent's world population percentage.

    Args:
        data (list of dict): The data containing country information.

    Returns:
        None
    """
    continent = input('Type Continent => ')
    continent_data = list(filter(lambda item: item['Continent'] == continent, data))
    if not continent_data:
        print(f"No data found for {continent}.")
        return
    countries = [item['Country'] for item in continent_data]
    percentages = [item['World Population Percentage'] for item in continent_data]
    generate_pie_chart(countries, percentages, continent)

def generate_bar_chart_for_country(data):
    """
    Generate a bar chart for a specific country's population over the years.

    Args:
        data (list of dict): The data containing country information.

    Returns:
        None
    """
    country = input('Type Country => ')
    result = population_by_country(data, country)
    if not result:
        print(f"No data found for {country}.")
        return
    country_dict = result[0]
    labels, values = get_population(country_dict)
    generate_bar_chart(labels, values, country)