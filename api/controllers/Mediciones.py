from flask import jsonify, request
from db.db import cnx

class Mediciones():
    global cur
    cur = cnx.cursor()

    def list():
        print("4")
        lista = []
        cur.execute("SELECT * FROM mediciones")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            print("3")
            registro = zip(columns,row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close
    
    def create(body):
        print("2")
        data = (body['fecha'], body['origen'], body['valor'], body['codigoSensor'], body['observacion'])
        sql = "INSERT INTO mediciones(fecha, origen, valor, codigoSensor, observacion) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Insertado'},200

