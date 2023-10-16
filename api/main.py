from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, FileResponse
from src.chart_generator import generate_pie_chart_for_continent, generate_bar_chart_for_country
from src.utils import delete_images_in_directory
import pandas as pd
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
df = pd.read_csv('./db/data.csv')
data = df.to_dict(orient='records')
delete_images_in_directory('./img/')


@app.get('/', response_class=HTMLResponse, name="root")
async def get_routes(request: Request):
    route_items = [
        {"name": "Full Data", "url": request.url_for("get_data")},
        {"name": "Countries", "url": request.url_for("get_country_data", country_name="colombia")},
        {"name": "Continent", "url": request.url_for("get_continent_data", continent_name="south_america")},
        {"name": "Population in Year (YYYY)", "url": request.url_for("get_population_data", year=2022, population=50000000)},
        {"name": "Visualize Data", "url": request.url_for("visualize_data")},
        {"name": "Generate Bar Chart", "url": request.url_for("generate_bar_chart_route", country_name="colombia")},
        {"name": "Generate Pie Chart", "url": request.url_for("generate_pie_chart_route", continent_name="south_america")},
    ]
    return templates.TemplateResponse("routes.html", {"request": request, "routes": route_items})


@app.get('/data')
def get_data():
    return data


@app.get('/continent/{continent_name}')
def get_continent_data(continent_name: str):
    continent_name = continent_name.replace("_", " ").title()
    result = df[df['Continent'].str.contains(continent_name, case=False)]
    if result.empty:
        return {"message": f"No data found for the continent {continent_name}"}
    continent_data = result.to_dict(orient='records')
    return continent_data


@app.get('/country/{country_name}')
def get_country_data(country_name: str):
    country_name = country_name.replace("_", " ").title()
    result = df[df['Country'].str.contains(country_name, case=False)]
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
    country_name = country_name.replace("_", " ").title()
    result = df[df['Country'] == country_name]
    print(result)
    if result.empty:
        raise HTTPException(status_code=404, detail=f"No data found for the country {country_name}")
    print(result)
    generate_bar_chart_for_country(result, country_name)
    country_name = country_name.replace(" ", "_")
    image_path = f'./img/bar_{country_name}.png'
    return FileResponse(image_path, media_type="image/png")


@app.get('/generate_pie_chart/{continent_name}')
def generate_pie_chart_route(continent_name: str):
    continent_name = continent_name.replace("_", " ").title()
    result = df[df['Continent'] == continent_name]
    if result.empty:
        raise HTTPException(status_code=404, detail=f"No data found for the continent {continent_name}")
    generate_pie_chart_for_continent(result, continent_name)
    continent_name = continent_name.replace(" ", "_")
    image_path = f'./img/pie_{continent_name}.png'
    return FileResponse(image_path, media_type="image/png")


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)