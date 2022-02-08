from flask import Flask, jsonify
from flask import request
import mysql.connector

# Criando a API em Flask

app = Flask(__name__)


@app.route("/pessoa", methods=['GET','POST','PUT','DELETE'])
def pessoa():

  # Método GET
    if request.method == 'GET':
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        # password="[INSIRA SUA SENHA DO BANCO DE DADOS]",
        database="crud")

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM crud.pessoa")

        myresult = mycursor.fetchall()

        print(myresult)
        return jsonify(myresult)    


  # Método POST
    if request.method == 'POST':

      mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      # password="[INSIRA SUA SENHA DO BANCO DE DADOS]",
      database="crud")

      dados = request.get_json()

      id = dados["id"]
      nome = dados["nome"]
      sobrenome = dados["sobrenome"]
      datadenascimento = dados["datadenascimento"]
      naturalidade = dados["naturalidade"]
      hobby = dados ["hobby"]

      mycursor = mydb.cursor()

      sql = "INSERT INTO pessoa (id, nome, sobrenome, datadenascimento, naturalidade, hobby) VALUES (%s, %s, %s, %s, %s, %s)"
      val = (id, nome, sobrenome, datadenascimento, naturalidade, hobby)
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")

      return dados
    

    # Método PUT
    if request.method == 'PUT':
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        # password="[INSIRA SUA SENHA DO BANCO DE DADOS]",
        database="crud")

      dados = request.get_json()

      id = dados["id"]
      nome = dados["nome"]
      sobrenome = dados["sobrenome"]
      datadenascimento = dados["datadenascimento"]
      naturalidade = dados["naturalidade"]
      hobby = dados ["hobby"]

      mycursor = mydb.cursor()

      sql = "UPDATE pessoa SET nome = %s, sobrenome = %s, datadenascimento = %s, naturalidade = %s, hobby = %s WHERE id = %s"
      val = (nome, sobrenome, datadenascimento, naturalidade, hobby, id)
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record affected.")

      return dados
      

    # Método DELETE
    if request.method == 'DELETE':
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        # password="[INSIRA SUA SENHA DO BANCO DE DADOS]",
        database="crud")

      dados = request.get_json()

      id = dados["id"]

      mycursor = mydb.cursor()
      sql = "DELETE FROM pessoa WHERE id = %s"

      val=(id,)

      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record(s) deleted")

      return("Dado deletado com sucesso!")