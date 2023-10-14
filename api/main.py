from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse, FileResponse
from src.chart_generator import generate_pie_chart_for_continent, generate_bar_chart_for_country
import pandas as pd
import uvicorn

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
            "Generate Bar Chart: http://localhost:8000/generate_bar_chart/{country_name}",
            "Generate Pie Chart: http://localhost:8000/generate_pie_chart/{continent_name}",
            "Note: Use underscores (_) instead of spaces in continent_name for pie charts (e.g., 'South_America' or 'North_America').",
        ]
    }

@app.get('/data')
def get_data():
    return data

@app.get('/continent/{continent_name}')
def get_continent_data(continent_name: str):
    continent_name_upper = continent_name.title()
    result = df[df['Continent'].str.contains(continent_name_upper, case=False)]
    if result.empty:
        return {"message": f"No data found for the continent {continent_name}"}
    continent_data = result.to_dict(orient='records')
    return continent_data

@app.get('/country/{country_name}')
def get_country_data(country_name: str):
    country_name_upper = country_name.title()
    result = df[df['Country'].str.contains(country_name_upper, case=False)]
    if result.empty:
        return {"message": f"No data found for the country {country_name}"}
    country_data = result.to_dict(orient='records')
    return country_data

@app.get('/population/{year}/{population}')
def get_population_data(year: int, population: int):
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

@app.get('/generate_bar_chart/{country_name}')
def generate_bar_chart_route(country_name: str):
    country_name = country_name.replace("_", " ").title()  # Formatea el nombre del país
    result = df[df['Country'].str.contains(country_name, case=False)]
    if result.empty:
        raise HTTPException(status_code=404, detail=f"No data found for the country {country_name}")
    generate_bar_chart_for_country(df, country_name)
    image_path = f'./img/bar_{country_name}.png'
    return FileResponse(image_path, media_type="image/png")

@app.get('/generate_pie_chart/{continent_name}')
def generate_pie_chart_route(continent_name: str):
    continent_name_formatted = continent_name.replace("_", " ").title()
    result = df[df['Continent'].str.contains(continent_name_formatted, case=False)]
    if result.empty:
        raise HTTPException(status_code=404, detail=f"No data found for the continent {continent_name_formatted}")
    generate_pie_chart_for_continent(df, continent_name_formatted)
    image_path = f'./img/pie_{continent_name}.png'
    return FileResponse(image_path, media_type="image/png")

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)