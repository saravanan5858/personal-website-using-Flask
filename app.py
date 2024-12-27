from flask import Flask, render_template, jsonify

app = Flask(__name__)

WORK_EXPERIENCE = [

{
    'title': 'SENIOR ENGINEER',
    'company': 'Bosch Global Software Technologies',
    'start_date': '09/2022',
    'end_date': 'Present',
    'location': 'Coimbatore, India',
    'description': ['''Automotive Aftermarket Diagnostic tool (CAN, UDS, GMLAN,
                    etc.) content authoring using Bosch specific framework to
                    support North America’s IAM Market by Reverse Engineering
                    from existing OEM diagnostic tool.''',
                    'Python automation of tasks with repetitive manual effort thus saving time.',
                    'Working on adopting GenAI (LLMs) into current workflow to automate the reverse engineering of OEM diagnostic tool.']
},

{
    'title': 'PROJECT ENGINEER',
    'company': 'Kumaraguru Centre for Industrial Research and Innovation',
    'start_date': '09/2021',
    'end_date': '09/2022',
    'location': 'Coimbatore, India',
    'description': ['''Design and development of 4-wheel drive, independent
                    steering industrial robot.''',
                    'Design and development of Autonomous All Terrain Electric Vehicle.']
},

{
    'title': 'RESEARCH ASSISTANT',
    'company': 'Kumaraguru Centre for Industrial Research and Innovation',
    'start_date': '10/2018',
    'end_date': '08/2021',
    'location': 'Coimbatore, India',
    'description': ['''Successfully converted a traditional diesel engine tractor
                    into an electric tractor.''',
                    '''Successfully converted a manual-driven electric golfcart into
                    a complete drive-by-wire golfcart - First step to Self-driving
                    vehicle.''',
                    '''PID controller for speed control of DC motor for UV robot.''']
}

]

@app.route("/")
def hello():
    return render_template('home.html', work_exp = WORK_EXPERIENCE)

@app.route("/api/work_experience")
def work_exp():
    return jsonify(WORK_EXPERIENCE)    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


