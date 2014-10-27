# Sonya Hogan 2014.
import urllib2
import json

class Client(object):

    def __init__(self, host, port, path):
    """ Setup Client object with details of Seneca of server
    """
        self.host = host
        self.port = port
        self.path = path
        self.url = "http://%s:%i/%s" % (self.host, self.port, self.path)
    
    def act(self, data):
    """ Send http request to the Seneca server and return the result.
    """
        json_data = json.dumps(data)
        req = urllib2.Request(self.url)
        result = urllib2.urlopen(req, json_data)
        return list(result)    	