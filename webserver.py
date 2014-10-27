# Sonya Hogan 2014.
import string,cgi,time
import urllib2
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

""" Update host and port values here to match your Seneca sever endpoint
"""
    host = "localhost"
    port = "10101"
    
    
    global serverurl
    serverurl = "http://%s:%s" % (host, port)
        
    #TODO: test get request
    def do_GET(self):
        try:
        	data = list(self.rfile)
        	
        	data = list(result)
            self.send_response(result.getcode())
            self.end_headers()
            self.wfile.write(data)
            self.wfile.close()
        except IOError:
            self.send_error(404,'Server Endpoint Not Found: %s' % self.path)
     

    def do_POST(self):
        try:
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            result = self.completeRequest(serverurl + self.path, data)
            data = list(result)
            self.send_response(result.getcode())
            self.end_headers()
            self.wfile.write(data)
            self.wfile.close()
        except :
            raise
    
    def completeRequest(self, fullurl, data):
        req = urllib2.Request(fullurl)
        result = urllib2.urlopen(req, data)
        return result
        

def main():
    try:
""" setup details of this server
"""
        server = HTTPServer(('', 8888), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()

