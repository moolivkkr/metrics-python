from behave import *
import requests

@given('the Python Metrics application is running')
def step_impl(context):
    # Start the application server
    context.server = subprocess.Popen(['uvicorn', 'my_app:app'])

@given('the "/metrics" endpoint is available')
def step_impl(context):
    # Make a GET request to the /metrics endpoint
    response = requests.get('http://localhost:8000/metrics')

    # Check that the response status code is 200
    assert response.status_code == 200

@when('I make a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    # Make a GET request to the specified endpoint
    context.response = requests.get(f'http://localhost:8000{endpoint}')

@then('the response body contains "{metric}"')
def step_impl(context, metric):
    # Check that the specified metric is present in the response body
    assert metric in context.response.text
