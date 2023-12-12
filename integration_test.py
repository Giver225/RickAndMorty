import pytest
from uuid import uuid4
from time import sleep
from datetime import datetime
from main import root, get_list
import json
import asyncio
from fastapi import Query


def test_root_get():
    res = asyncio.run(root())
    assert('id' in res.keys())
    assert('name' in res.keys())
    assert(type(res['id']) == int)


def test_list_get():
    res = asyncio.run(get_list(q=[795]))
    res = res[0]
    assert (res['id']==795)
    assert (res['name']=='Palicki')
    assert(res['status']=="Alive")

test_root_get()
test_list_get()
    

