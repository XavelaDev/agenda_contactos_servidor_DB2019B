from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

bd = mysql.connector.connect(host='localhost', user='alumno',
passwd='12345',
database='agenda')

cursor = bd.cursor()

@app.route('/agenda/')#, methods=["GET","POST"])
def agenda():
	#if request.method == "GET":
	contactos = []
	query = "SELECT * FROM contacto"
	cursor.execute(query)

	for contacto in cursor.fetchall():
	    d = {
		    'id': contacto[0],
            'nombre': contacto[1],
            'avatar': contacto[2],
            'correo': contacto[3],
            'telefono': contacto[4],
            'facebook': contacto[5],
            'twitter': contacto[6],
            'instagram': contacto[7],
		}
	    contactos.append(d)
	    print(d)
	print(contactos)
	return jsonify(contactos)

app.run(debug=True)