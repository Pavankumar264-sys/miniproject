from flask import Flask,render_template
from utils.db import db
from models.add import Matches,Teams




flask_app=Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///add.db'
db.init_app(flask_app)

with flask_app.app_context():
    db.create_all()


@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/teams')
def teams():
    return render_template('teams.html')


@flask_app.route('/matches')
def matches():
    return render_template('matches.html')


@flask_app.route('/table')
def table():
    return render_template('table.html')


@flask_app.route('/contact')
def contact():
    return render_template('contact.html')

@flask_app.route('/news')
def news():
    return render_template('news.html')

@flask_app.route('/2023')
def season_23():
    return render_template('2023.html')

@flask_app.route('/2022')
def season_22():
    return render_template('2022.html')

@flask_app.route('/teams/2021')
def season_21():
    return render_template('2021.html')

@flask_app.route('/teams/2020')
def season_20():
    return render_template('2020.html')

@flask_app.route('/2019')
def season_19():
    return render_template('2019.html')

@flask_app.route('/2018')
def season_18():
    return render_template('2018.html')

@flask_app.route('/2017')
def season_17():
    return render_template('2017.html')

@flask_app.route('/2016')
def season_16():
    return render_template('2016.html')

@flask_app.route('/2015')
def season_15():
    return render_template('2015.html')

@flask_app.route('/2014')
def season_14():
    return render_template('2014.html')

@flask_app.route('/2013')
def season_13():
    return render_template('2013.html')

@flask_app.route('/2012')
def season_12():
    return render_template('2012.html')

@flask_app.route('/2011')
def season_11():
    return render_template('2011.html')

@flask_app.route('/2010')
def season_10():
    return render_template('2010.html')

@flask_app.route('/2009')
def season_09():
    return render_template('2009.html')

@flask_app.route('/2008')
def season_08():
    return render_template('2008.html')






















if __name__=='__main__':
    flask_app.run(
        host='127.0.0.1',
        port=4005,
        debug=True

    )