import webapp2
from datetime import datetime

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/tsval" method="post">
      Timestamp as it appears : <div><input type="text" size="50" name="ts" value=""></div>
      <div><input type="submit" value="Validate "></div>
    </form>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class TSCheck(webapp2.RequestHandler):

    def post(self):
        tsval = self.request.get('ts')
        dt_formats = [
                '%m-%d-%Y',
                '%d-%m-%Y',
                '%Y-%m-%d',
                '%Y-%d-%m',
                '%m-%d-%y',
                '%d-%m-%y',
                '%y-%m-%d',
                '%y-%d-%m',
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%d %H:%M',
                '%Y-%m-%d %H:%M:%S.%f',
                '%m/%d/%Y %H:%M:%S',
                '%d/%m/%Y %H:%M:%S',
                '%d/%b/%Y:%H:%M:%S',
                '%m/%d/%Y %I:%M:%S %p',
                '%d/%m/%Y %I:%M:%S %p',
                '%m/%d/%Y %H:%M',
                '%d/%m/%Y %H:%M',
                '%d/%m/%Y %I:%M %p',
                '%m/%d/%Y %I:%M %p',
                '%m/%d/%Y',
                '%d/%m/%Y',
                '%m/%d/%y %H:%M:%S',
                '%d/%m/%y %H:%M:%S',
                '%m/%d/%y %I:%M:%S %p',
                '%d/%m/%y %I:%M:%S %p',
                '%m/%d/%y %H:%M',
                '%d/%m/%y %H:%M',
                '%m/%d/%y %I:%M %p',
                '%d/%m/%y %I:%M %p',
                '%m/%d/%y',
                '%d/%m/%y',
                '%Y-%m-%dT%H:%M:%S.%fZ',
                '%Y-%m-%dT%H:%M:%S%Z',
                '%Y%m%d %H:%M:%S',
                '%Y-%m-%dT%H:%M:%SZ',
                '%Y%m%d',
                '%Y%m%d%H%M%S',
                '%Y%m%dT%H%M%S',
        ]
        results = ''
        for dt in dt_formats:
           try:
                  if datetime.strptime(tsval, dt):
                        results="OK. Matches the pattern:  <b>" + dt + "</b>"
                        break
           except ValueError:
                        results="Possibly Not OK as it does not match any of these:<br>" + "<br>".join(dt_formats)
        self.response.write('<html><body>')
        self.response.write(results)
        self.response.write('</body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/tsval', TSCheck),
], debug=True)

