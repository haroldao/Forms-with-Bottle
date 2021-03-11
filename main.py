import bottle
@bottle.route('/')

def index():
  return """
<h1> Coucou </h1>
<p> Première tentative Bottle. </p>
"""
bottle.run(host='localhost', port=8080, debug=True, reloader=True)