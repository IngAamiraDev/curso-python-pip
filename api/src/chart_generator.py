from src.utils import get_population
from src.charts import generate_bar_chart, generate_pie_chart


def generate_pie_chart_for_continent(data, continent):
    countries = data['Country'].values
    percentages = data['World Population Percentage'].values
    generate_pie_chart(countries, percentages, continent)


def generate_bar_chart_for_country(data, country):
    labels, values = get_population(data)
    generate_bar_chart(labels, values, country)