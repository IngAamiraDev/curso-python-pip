from src.utils import get_population
from src.charts import generate_bar_chart, generate_pie_chart

def generate_pie_chart_for_continent(data, continent):
    """
    Generate a pie chart to visualize population distribution for a continent.

    Args:
        data (DataFrame): The data containing population data for the continent.
        continent (str): The name of the continent.

    Returns:
        None
    """
    countries = data['Country'].values
    percentages = data['World Population Percentage'].values
    generate_pie_chart(countries, percentages, continent)

def generate_bar_chart_for_country(data, country):
    """
    Generate a bar chart to visualize the population of a specific country over the years.

    Args:
        data (DataFrame): The data containing country-specific population information.
        country (str): The name of the country.

    Returns:
        None
    """
    labels, values = get_population(data)
    generate_bar_chart(labels, values, country)