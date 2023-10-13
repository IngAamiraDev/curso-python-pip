from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse, FileResponse
from src.chart_generator import generate_pie_chart_for_continent, generate_bar_chart_for_country
import pandas as pd
import uvicorn
import matplotlib.pyplot as plt
from io import BytesIO
import json
import base64
from PIL import Image
import os
import tempfile

app = FastAPI()

# Load the data from the CSV file once when the application starts
df = pd.read_csv('./db/data.csv')
data = df.to_dict(orient='records')

# Define a function for the root endpoint
@app.get('/')
def get_routes():
    return {
        "routes": [
            "Full Data: http://localhost:8000/data",
            "Countries: http://localhost:8000/country/{name_country}",
            "Continent: http://localhost:8000/continent/{name_continent}",
            "Population in Year (YYYY): http://localhost:8000/population/{year}/{population}",
            "Visualize Data: http://localhost:8000/visualize",
            "Plot Population: http://localhost:8000/plot_population",
        ]
    }

@app.get('/data')
def get_data():
    return data

@app.get('/continent/{continent_name}')
def get_continent_data(continent_name: str):
    continent_name_upper = continent_name.capitalize()
    result = df[df['Continent'] == continent_name_upper]
    if result.empty:
        return {"message": f"No data found for the continent {continent_name}"}
    continent_data = result.to_dict(orient='records')
    return continent_data

@app.get('/country/{country_name}')
def get_country_data(country_name: str):
    country_name_upper = country_name.capitalize()
    result = df[df['Country'] == country_name_upper]
    if result.empty:
        return {"message": f"No data found for the country {country_name}"}
    country_data = result.to_dict(orient='records')
    return country_data

@app.get('/population/{year}/{population}')
def get_population_data(year: int, population: int):
    # Add validation for year and population here if needed
    column_name = f"{year} Population"
    result = df[df[column_name] >= population]
    if result.empty:
        raise HTTPException(status_code=404, detail="No countries or cities meet the population criteria.")
    population_data = result.to_dict(orient='records')
    return population_data

@app.get('/visualize')
def visualize_data():
    data_html = df.to_html()
    html_content = f"<html><head></head><body>{data_html}</body></html>"
    return HTMLResponse(content=html_content)

'''@app.get('/plot_population')
def plot_population():
    year = 2015  # Year for which you want to generate the graph
    column_name = f"{year} Population"
    plt.figure(figsize=(10, 6))
    plt.bar(df['Country'], df[column_name])
    plt.title(f'Population in {year}')
    plt.xlabel('Country')
    plt.ylabel('Population')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Crear un archivo temporal para guardar la imagen
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_filename = temp_file.name
        temp_file.write(buffer.read())

    return FileResponse(temp_filename, media_type="image/png")'''

@app.get('/generate_bar_chart/{country_name}')
def generate_bar_chart_route(country_name: str):
    country_name_upper = country_name.capitalize()
    result = df[df['Country'] == country_name_upper]
    if result.empty:
        raise HTTPException(status_code=404, detail=f"No data found for the country {country_name}")
    generate_bar_chart_for_country(df, country_name)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)