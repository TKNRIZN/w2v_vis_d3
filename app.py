#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:56:06 2018

@author: takanori
"""

from flask import Flask, render_template, request, redirect, url_for,jsonify
import numpy as np


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route('/')
def init():
    return "CONNECTED"

@app.route('/result')
def result():
    
    keyword = request.args.get('keyword')
    
    res = {"result":keyword}
    return jsonify(res)


@app.route('/asyn')
def asyn():
    name = "INPUT KEYWORD"
    title = "word2vec"
    return render_template('index.html',name = name,title = title)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)