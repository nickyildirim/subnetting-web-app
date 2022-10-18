"""
This is the main flask route module where its function defined along
with its route. The logic is defined under the question function.
"""

from random import randint
from flask import Flask, render_template
import yaml
from jinja2 import Template
from generator import q_maker, random_ipv4, ipaddress

app = Flask(__name__)

@app.route("/")

def question() :
    """
    This generates a random parameter for the question and renders it with
    the yaml file under questionlist then serves the question with its answer.
    """

    with open(r'questionlist.yml', encoding="utf-8") as file:

        q_number = randint(2, 2)
        q_list = yaml.full_load(file)
        random_ip_addr = ipaddress.ip_interface(random_ipv4())
        random_net_addr = ipaddress.ip_network(random_ipv4(), strict=False)

        q_parameters = {
            "hostAddress": random_ip_addr,
            "networkAddress": random_net_addr
        }

        j2_template = Template(q_list['Questions'][q_number])    
        renderred_question = j2_template.render(q_parameters)
        answer = q_maker(question_kind=q_number, random_ip=random_ip_addr, random_net=random_net_addr)

    return render_template('home.html', question = renderred_question, answer = answer)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
