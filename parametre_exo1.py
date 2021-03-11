import bottle

#### Index
@bottle.route('/')
def index():
  nom = bottle.request.query.nom
  prenom = bottle.request.query.prenom
  #Age
  age =bottle.request.query.age
  #Bin Age
  age_2 = bin(int(bottle.request.query.age))
  age_bin = age_2.replace("0b","")

  # Render
  return bottle.template("exo1.html", 
    nom = nom,
    prenom = prenom,
    age = age,
    age_bin = age_bin
  )

#### Page2
@bottle.route('/page2')
def page2():
  return "test"

# Run
bottle.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
