## Subnetting Flask Web App

[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
![linter workflow](https://github.com/nickyildirim/subnetting-web-app/actions/workflows/linter.yaml/badge.svg)
![ci workflow](https://github.com/nickyildirim/subnetting-web-app/actions/workflows/ci.yaml/badge.svg)

Simple question generator web app for subnetting practices. Each question gets randomized parameter which brings unlimited amount of questions to practice subnetting. 

### To run the app:

1 - Create your python env:

`python3 -m venv subnetting-app`

2 - Install required modules

`pip install -r requirements.txt`

3 - Run gunicorn to serve the http:

`gunicorn3 --bind 0.0.0.0:8000 wsgi:app --daemon`

### Example Site:
[practice-subnetting.com](https://practice-subnetting.com)


### Future Action Items:

- ~~Increase the number of question kind to 6.~~
- Finish explanation part for each question kind.
- Include IPv6 questions. 

