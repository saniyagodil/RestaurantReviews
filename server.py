# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 14:35:12 2019

@author: Saniya
"""

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port: ", PORT)
    httpd.serve_forever()