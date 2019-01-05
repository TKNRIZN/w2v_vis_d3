FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install nkf

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install flask

RUN apt-get update



RUN apt-get install -y  mecab 
RUN apt-get install mecab-ipadic 
RUN apt-get install curl 
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN cd mecab-ipadic-neologd


RUN pip install --upgrade gensim
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
