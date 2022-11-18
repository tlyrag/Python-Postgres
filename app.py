import postgres_controller as db
import constants as qry
from flask import Flask
from flask_restful import Api,Resource, reqparse
import routes as rts

app = Flask (__name__)
api = Api(app)



api.add_resource(rts.Vendor , "/helloworld/<string:name>")



print('Server is up and Running')
if __name__ =="__main__":
    app.run(debug = True)