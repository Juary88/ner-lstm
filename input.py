import random
import numpy as np
import pickle


def get_dummy_data(num):
    emb = [[[random.random() for _ in range(300)] for i in range(50)] for j in range(num)]
    tag = [np.array([ [0 for i in range(5)] for j in range(50)]) for i in range(num)]
    for t in tag:
        t[random.randint(0,len(t)-1)] = 1
    return emb,tag

def get_train_data():
    emb = pickle.load(open('50_train_tvec','rb'))
    tag = pickle.load(open('50_train_tag','rb'))
    return emb,tag

def get_test_data():
    emb = pickle.load(open('50_testa_tvec','rb'))
    tag = pickle.load(open('50_testa_tag','rb'))
    return emb,tag

def get_final_data():
    emb = pickle.load(open('50_testb_tvec','rb'))
    tag = pickle.load(open('50_testb_tag','rb'))
    return emb,tag

def get_indi_data():
    emb = pickle.load(open('t','rb'))
    tag = pickle.load(open('tag','rb'))
    return emb,tag
