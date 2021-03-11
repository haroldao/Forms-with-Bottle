import bottle

@bottle.route('/')
def index():
  return """
<h1> Hi </h1>
<p> First Page. </p>
"""
bottle.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
