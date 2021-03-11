import bottle

@bottle.route('/')
def index():
  nom = bottle.request.query.nom
  prenom = bottle.request.query.prenom
#   return """
# <h1> Hi </h1>
# <p> First Page. </p>
# """
  # return bottle.template(
  #   'Hi {{nom}} {{prenom}}'
  #   , nom=nom, prenom=prenom)

  return bottle.template("exo1.html", nom=nom, prenom=prenom)

bottle.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
