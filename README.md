# Subnetting Flask Web App
Simple question generator web app for subnetting practices 

## Required libraries
`pip3 install flask gunicorn3 jinja2`

## To run the app
`gunicorn3 --bind 0.0.0.0:8000 wsgi:app --daemon`

