#!/usr/bin/env python

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('calculate'))

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method == "GET":

        data = [
            [[4.98, -0.26, 45486, 'DOGA', 'Low-evaluation'],
                [6.69, -2.27, 10969, 'POS', 'Low-evaluation'],
                [9.97, -0.59, 3610, 'AILab(202007-09)', 'Low-evaluation'],
                [9.96, -1.0, 4413, 'ReAILab(202007-09)', 'Low-evaluation'],
                [9.92, 0.0, 1109, 'DB', 'Low-evaluation'],
                [15.63, 0.76, 11253, 'QDStep3', 'Low-evaluation'],
                [5.91, 0.0, 37967, 'SX', 'Low-evaluation'],
                [19.8, 1.08, 4366, 'MC', 'Low-evaluation'],
                [4.92, 0.0, 23560, 'PACER', 'Low-evaluation'],
                [6.98, 1.0, 180057, 'FS', 'Low-evaluation'],
                [14.97, -1.0, 11170, 'ST', 'Low-evaluation'],
                [4.89, 0.0, 19536, 'PACER', 'Low-evaluation'],
                [13.68, 5.06, 5644, 'DP', 'Low-evaluation'],
                [10.92, -3.75, 22551, 'ZG', 'Low-evaluation'],
                [13.09, -6.37, 44172, 'AI', 'Low-evaluation'],
                [5.0, 0.02, 51739, 'DOGA', 'Low-evaluation'],
                [5.0, 2.09, 40986, 'DOGA', 'Low-evaluation'],
                [15.0, 0.0, 1280, 'ZDH', 'Low-evaluation'],
                [4.97, 0.0, 69110, 'ZDH', 'Low-evaluation'],
                [4.93, 1.81, 82366, 'CRM', 'Low-evaluation'],
                [6.96, 0.0, 40083, 'AS', 'Low-evaluation'],
                [8.96, 0.0, 44289, 'AS', 'Low-evaluation'],
                [13.08, -6.71, 44197, 'SFStep2', 'Low-evaluation'],
                [4.93, 0.0, 82508, 'PX', 'Low-evaluation']
            ], [
                [11.99, 0.0, 17236, 'QDStep3', 'General-evaluation'],
                [14.95, 0.0, 11854, 'QDStep3', 'General-evaluation'],
                [14.79, 0.0, 4757, 'TJ', 'General-evaluation'],
                [10.0, 0.0, 0, 'PX', 'General-evaluation'],
                [10.97, 1.0, 86955, 'FS', 'General-evaluation'],
                [10.0, 0.0, 0, 'FS', 'General-evaluation'],
                [14.97, -0.61, 14336, 'POS', 'General-evaluation'],
                [15.09, -1.0, 11626, 'POS', 'General-evaluation'],
                [6.98, 1.3, 180914, 'MS', 'General-evaluation'],
                [14.92, 0.0, 2441, 'MDLINK', 'General-evaluation'],
                [15.0, 0.0, 2011, 'TFS_CP', 'General-evaluation'],
                [14.94, -2.0, 5527, 'AS', 'General-evaluation'],
                [13.13, -2.0, 4893, 'API', 'General-evaluation'],
                [10.0, 0.0, 0, 'BY', 'General-evaluation'],
                [10.0, 0.0, 0, 'BY', 'General-evaluation'],
                [14.91, 0.0, 13633, 'WZ', 'General-evaluation'],
                [10.97, 5.61, 88595, 'MS', 'General-evaluation'],
                [14.92, -0.35, 2561, 'SP', 'General-evaluation'],
                [10.0, 0.0, 0, 'DS', 'General-evaluation'],
                [14.97, -2.0, 33885, 'DS', 'General-evaluation'],
                [11.98, -3.54, 3919, 'JG', 'General-evaluation'],
                [14.72, -3.28, 3131, 'JG', 'General-evaluation'],
                [13.05, 0.15, 1697, 'JG', 'General-evaluation'],
                [14.94, 0.0, 1526, 'JG', 'General-evaluation'],
                [12.0, 2.0, 3795, 'JG', 'General-evaluation'],
                [15.01, -3.0, 4223, 'JG', 'General-evaluation'],
                [14.51, 0.89, 1713, 'SP', 'General-evaluation'],
                [14.98, 0.0, 2379, 'SP', 'General-evaluation'],
                [14.74, 0.0, 2209, 'SP', 'General-evaluation'],
                [14.74, 0.0, 2192, 'SP', 'General-evaluation']
            ],
            [
                [20.0, 2.05, 2093, 'DP', 'High-estimation'],
                [16.55, 0.63, 91588, 'ReAILabAI', 'High-estimation'],
                [18.36, 5.0, 313, 'TJ', 'High-estimation'],
                [16.29, 1.0, 2630, 'SP', 'High-estimation'],
                [16.55, 0.0, 91516, 'ReAILabAI', 'High-estimation'],
                [8.22, -3.74, 13304, 'QDStep3', 'High-estimation'],
                [12.0, 2.41, 1721, 'SR', 'High-estimation'],
                [7.8, 3.67, 8758, 'POS', 'High-estimation'],
                [20.0, 0.0, 36259, 'POS', 'High-estimation'],
                [15.52, 0.0, 242, 'TJ', 'High-estimation'],
                [20.0, 0.0, 100, 'TJ', 'High-estimation'],
                [15.21, 0.0, 8464, 'POS', 'High-estimation'],
                [18.02, -5.0, 1427, 'LITE', 'High-estimation'],
                [15.01, 0.0, 1110, 'BS', 'High-estimation'],
                [15.97, -4.91, 18147, 'ZP', 'High-estimation'],
                [15.01, 0.0, 1055, 'TFS_CP', 'High-estimation'],
                [15.01, 0.0, 591, 'RP', 'High-estimation'],
                [20.0, 0.0, 11, 'BY', 'High-estimation'],
                [15.01, 0.0, 2700, 'MDLINK', 'High-estimation'],
                [16.17, 0.0, 2671, 'MDLINK', 'High-estimation'],
                [16.0, -9.51, 18181, 'SFStep2', 'High-estimation'],
                [15.01, -0.43, 2197, 'JG', 'High-estimation'],
                [15.01, 0.0, 2782, 'JG', 'High-estimation']
            ]
        ]
        constructionSpecificity = data
        return render_template('index.html', constructionSpecificity=constructionSpecificity)

    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")



if __name__ == '__main__':
    app.run(host='localhost', port=8083)



