import webapp2
import json
import logging
from controllers import mainh


logging.getLogger().setLevel(logging.DEBUG)


app = webapp2.WSGIApplication([
	('/(.*)/?', mainh.MainHandler)
],debug=True)



