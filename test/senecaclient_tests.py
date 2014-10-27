from nose.tools import *
from seneca_python_driver.senecaclient import Client

def test_act():
    c1 = Client("localhost", 10101, "act")
    result = c1.act({"color": "red"})
    assert_equal(result, ['{"hex":"#FF0000"}'])