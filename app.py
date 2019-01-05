#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:56:06 2018

@author: takanori
"""

from flask import Flask, render_template, request, redirect, url_for,jsonify
import numpy as np
from gensim.models import word2vec


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

class find_word:

    def __init__(self):
        self.model = word2vec.Word2Vec.load('wiki.model')
        
    def get_similarword(self,key):
    
        results = self.model.wv.most_similar(positive=[key])
    
        return results


@app.route('/')
def init():
    return "CONNECTED"

@app.route('/result')
def result():
    
    keyword = request.args.get('keyword')
    res = w2v.get_similarword(keyword)


    return jsonify(res)

@app.route('/v1/find/similarwords/')
def asyn():
    name = "INPUT KEYWORD"
    title = "word2vec"
        
    return render_template('index.html',name = name,title = title)

@app.route('/v1/find/similarwords/correlationdiagram')
def correlation_diagram():

    keyword = request.args.get('keyword')
    res = w2v.get_similarword(keyword)
    
    dataset = create_dataset(keyword,res)

    
    return render_template('visualiza.html',dataset= dataset)
    
    

def create_dataset(keyword,res):
    
    data_dict = {"nodes":[{"id":0,"name":keyword,"value":1}],"links":[]}
    
    for idx,item in enumerate(res):
        tmpdict_node = {"id":idx+1,"name":item[0],"value":item[1]}
        tmpdict_link = {"id":idx+1,"source":keyword,"target":item[0],"value":item[1]}
        data_dict["nodes"].append(tmpdict_node)
        data_dict["links"].append(tmpdict_link)
        

    res = data_dict
    
    return res


if __name__ == '__main__':
    w2v = find_word()
    app.run(host='0.0.0.0',debug=True)