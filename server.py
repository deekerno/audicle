import json
import os
import time
import tornado
import tornado.ioloop
import tornado.web

WEB_STUFF = os.path.join(os.path.dirname(__file__), 'web_stuff')
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'uploads')

class MainHandler(tornado.web.RequestHandler):
	"""Renders the landing page"""
	def get(self):
		self.render(os.path.join(WEB_STUFF, 'index.html'))

class UploadHandler(tornado.web.RequestHandler):
	def post(self):
		# Fill me in

if __name__ == "__main__":
	app = tornado.web.Application([
		(r'/', MainHandler),
		(r'/web_stuff/(.*)', tornado.web.StaticFileHandler, {'path': WEB_STUFF}),
		(r'/uploads/(.*)', tornado.web.StaticFileHandler, {'path': UPLOAD_DIR})
		])
	app.listen(9999)
	tornado.ioloop.IOLoop.current().start()