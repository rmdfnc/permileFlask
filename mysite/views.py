from flask import render_template
from flask import jsonify
from flask import url_for
from mysite import app
from mysite.a_Model import ModelIt
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
import pickle
from flask import request

with open('/Users/ahakso/Documents/gitDir/permileFlask/mysite/static/car_data.pkl','rb') as f:
    car_dict, car_data = pickle.load(f)

#staticfile_path = '/static'
#app.config['jsonfiles'] = staticfile_path

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )
@app.route('/input', methods=['GET','POST'])
def cesareans_input():
    return render_template("input.html", car_dict = car_dict)

@app.route('/output')
def cesareans_output():
  #pull the user make from input field and store it
  user_make = request.args.get('user_make')
  print(user_make)
  return render_template("output.html", births = user_make, the_result = user_make)

@app.route('/get_models')
def get_models():
    make = request.args.get('make')
    if make:
        models = list(car_dict[make])
        data = [{"id": str(x), "name": str(x)} for x in models]
        
        print(data)
    return jsonify(data)

@app.route('/get_years')
def get_years():
    model = request.args.get('model')
    if model:
        models = list(car_dict[make][model])
        data = [{"id": str(x), "name": str(x)} for x in models]
        
        print(data)
    return jsonify(data)


#@app.route('/get_model_array')
#def read_txt_file():
  #read it in
#  make = read_csv()
# return car_dict[make]

