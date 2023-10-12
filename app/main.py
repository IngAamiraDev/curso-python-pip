# Import the necessary modules
from src.chart_generator import generate_pie_chart_for_continent, generate_bar_chart_for_country
from src.read_csv import read_csv

def run():
    data = read_csv('./app/db/data.csv')    
    while True:
        type_chart = input('Type Chart "pie", "bar" or "exit" to quit => ')
        if type_chart == 'exit':
            break
        elif type_chart == 'pie':
            print('pie => (%) Continent/WorldPopulation')
            generate_pie_chart_for_continent(data)
        elif type_chart == 'bar':
            print('bar => Country/Population for year')
            generate_bar_chart_for_country(data)
        else:
            print("Invalid chart type. Please choose 'pie' or 'bar'.")

if __name__ == '__main__':
    run()