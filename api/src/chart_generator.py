from src.utils import get_population
from src.charts import generate_bar_chart, generate_pie_chart


def generate_pie_chart_for_continent(data, continent):
    """
    Generate a pie chart for a specific continent's world population percentage.

    Args:
        data (DataFrame): The data containing country information.

    Returns:
        None
    """
    continent_data = data[data['Continent'] == continent] #continent_data = data[data['Continent'].str.contains(continent, case=False)]
    if continent_data.empty:
        print(f"No data found for {continent}.")
        return
    countries = continent_data['Country'].values
    percentages = continent_data['World Population Percentage'].values    
    generate_pie_chart(countries, percentages, continent)


def generate_bar_chart_for_country(data, country):
    """
    Generate a bar chart for a specific country's population over the years.

    Args:
        data (DataFrame): The data containing country information.

    Returns:
        None
    """
    result = data[data['Country'] == country]
    if result.empty:
        print(f"No data found for {country}.")
        return
    labels, values = get_population(result)
    generate_bar_chart(labels, values, country)