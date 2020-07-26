from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'biostatsData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Chika"s Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsData')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, biostats=result)


@app.route('/view/<int:stat_id>', methods=['GET'])
def record_view(stat_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsData WHERE id=%s', stat_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', city=result[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
