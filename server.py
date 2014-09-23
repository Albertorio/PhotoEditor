#redirect= redirect to another wesite or another page
# request= For GET POST PUT request
# render_template= Generate html pages
from flask import Flask, redirect, request, render_template, jsonify

app = Flask(__name__) #init flask

#array acting as DB
postcards = {}

@app.route('/')
def new_post():
  #Id for post card
  ID = len(postcards)
  postcards[ID] = {}
  return redirect('/edit/%s' % ID, code=302)

@app.route('/edit/<int:ID>', methods=['GET', 'PUT'])
def edit_handler(ID):
  if request.method =='GET':
    
    return render_template("postcard.html", post=postcards[ID], editor=True)
  else:
    postcard[ID] = request.get_json()
    return jsonify(**postcard[ID])
  
@app.route('/view/<int:ID>')
def view_handler(ID):
    return render_template("postcard.html", post=postcards[ID])
  
app.run(host='0.0.0.0',port=3000,debug=True)


