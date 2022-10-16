from flask import Flask, render_template
import yaml
from random import randint
from jinja2 import Template
from generator import *

app = Flask(__name__)


@app.route("/")

def question():

    with open(r'questionlist.yml') as file:

        questionNumber = randint(4, 4)
        questionlist = yaml.full_load(file)
        randomIpAddr = ipaddress.ip_interface(random_ipv4())

        dataRandomizer = {
            "hostAddress": randomIpAddr,
        }

        j2_template = Template(questionlist['Questions']['Kinds'][questionNumber])        
        question = j2_template.render(dataRandomizer)

        
        answer = main(questionNumber, random_ipv4=randomIpAddr)


    return render_template('home.html', question = question, answer = answer)

if __name__ == '__main__':
   app.run(host="0.0.0.0")
