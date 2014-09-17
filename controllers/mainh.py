#!/usr/bin/env python

import os
from datetime import datetime
from google.appengine.api import memcache
from models.models import *
import json
import webapp2
from google.appengine.ext.webapp import template
import logging
import pprint


class MainHandler(webapp2.RequestHandler):
	def get(self, id):
		print 'id is', id
		print '-----------------------------------'
		if len(id) == 0:
			s = 'home.html'
		else:
			s = id + '.html'

		# We are using the template module to output the page.
		path = os.path.join(os.path.dirname(__file__), '../templates' ,s)
		self.response.out.write(template.render( path, {}))
