#main.py
# the import section
import webapp2

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!') #the response

class SecretPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "html"
        self.response.write("<h1> You found the secret! </h1>")

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/secret', SecretPage) #this maps the root url to the Main Page Handler
], debug=True)
