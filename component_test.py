import pytest
from pytest_assume import *
import requests
from uuid import UUID, uuid4
from datetime import datetime

base_url = 'http://localhost:80/'

def test_root_get():
    res = requests.get(base_url).json()
    assert ('id' in res.keys())
    assert ('name' in res.keys())
    assert (type(res['id']) == int)


def test_list_get():
    res = requests.get(base_url+'list/?q=795')
    # print(res.json())
    res = res.json()[0]
    print(res)
    assert (res['id']==795)
    assert (res['name']=='Palicki')
    assert (res['status']=="Alive")
    
test_list_get()
test_root_get()