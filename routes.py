
from flask_restful import Api,Resource, reqparse
import postgres_controller as pgcontrl
import constants as sql

names= {
    "tim":{"age":19, "gender":"male" },
}

videos = {}

vendor_args = reqparse.RequestParser()
vendor_args.add_argument("name", type=str, help = "Name of the vendor", required = True)




class Vendor(Resource):
    def get(self,name):
        try:
            pgcontrl.connect()
            data = pgcontrl.selectSql(sql.selectDrink,name)
            return data
        except:
            data = {"status":500 , "msg":"Route Failed"}
            return 
        finally:
            pgcontrl.disconnect()

