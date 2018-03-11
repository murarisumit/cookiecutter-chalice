import os
from chalice import Chalice
from chalice import CORSConfig
from ruamel.yaml import YAML
import requests

app = Chalice(app_name='{{cookiecutter.api_name}}')


# Read YAML file
filename = os.path.join(
    os.path.dirname(__file__), 'chalicelib', 'config.yml')
with open(filename) as f:
    yaml=YAML(typ='safe')
    config = yaml.load(f)

CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR',
}

cors_config = CORSConfig(
    allow_origin='https://test.slashsumit.com',
    allow_headers=['X-Special-Header'],
    max_age=600,
    expose_headers=['X-Special-Header'],
    allow_credentials=True
)

@app.route('/', cors=cors_config)
def index():
    # We can access ``config`` here if we want.
    return {"hello": config['name']}


@app.route('/cities/{city}')
def state_of_city(city):
    return {'state': CITIES_TO_STATE[city]}

