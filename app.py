from flask import Flask, render_template, url_for, redirect, request

from expression_comparison_calculator import exps_comp_cal
from function_time_complexity_calculator import func_time_comp_cal

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('exps'))


@app.route('/exps', methods=['GET', 'POST'])
def exps():
    if request.method == 'POST':
        data = request.form['content']
        report = exps_comp_cal(data)
        return render_template('views/exps.html', report=report, data=data)
    return render_template('views/exps.html', report=True)


@app.route('/func', methods=['GET', 'POST'])
def func():
    if request.method == 'POST':
        data = request.form['content']
        report = func_time_comp_cal(data)
        return render_template('views/func.html', report=report, data=data)
    return render_template('views/func.html', report=True)
