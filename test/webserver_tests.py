# Sonya Hogan 2014.
from nose.tools import *
import httplib, urllib

def test_post():
    headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
    conn = httplib.HTTPConnection("localhost:8888")
    conn.request("POST", "/act", '{"color": "red"}', headers)
    response = conn.getresponse()
    assert_equal(response.status, 200)
    data = response.read()
    assert_equal(data, '[\'{"hex":"#FF0000"}\']')
    conn.close()