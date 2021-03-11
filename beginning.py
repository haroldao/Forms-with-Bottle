import bottle


@bottle.route('/')
def index():
  return """
<h1> Hello World </h1>
<p> First Try with Bottle. </p>

<button>
<a href="/page2">Go to Page 2</a>
</button>
"""


@bottle.route('/page2')
def page2():
  return """
<h1> Page 2. </h1>
<p> This is a second page </p>"""

bottle.run(host='0.0.0.0', port=8080, debug=True, reloader=True)