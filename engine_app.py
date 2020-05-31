'''
Created on 2020/05/30

@author: ChiamingMike
'''

from flask import Flask, render_template, request, redirect, url_for
from engine_factory.Engine_switch import EngineSwitch
from engine_factory.logger.Log import log
from engine_factory.utils.Ini_creater import IniCreater

import time


app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    """
    if request.method == 'POST':
        is_exist = bool()
        country = request.form['country']
        code_1 = request.form['code_1']
        code_2 = request.form['code_2']
        columns = ['col1', 'col2', 'col3']
        # parameter1 : country (str)
        # parameter2 : codes (str)
        # parameter3 : data ([{codes:XXX}, {high:XXX}, {low:XXX}])
        # data = [{'col1': 'v1', 'col2': 'v2', 'col3': 'v3'}]
        data = [['v1', 'v2', 'N/A', 'v4']]

        try:
            country = 'JAPAN'
            target_code = ['1605']

            obj = IniCreater(country)
            obj.create_ini_file(target_code)

            start_time = time.time()
            engine_switch = EngineSwitch()
            engine_switch.switching_engine_to(country)
            end_time = time.time() - start_time
            log.i(f'TIME : {end_time} (s)')
            is_exist = True

        except Exception as e:
            log.e(e)
            log.e('Failed to boot engine.')

        return render_template('index.html',
                               code=is_exist,
                               columns=columns,
                               data=data,
                               country=country)
    else:

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
