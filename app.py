import postgres_controller as db
import constants as qry

db.connect()
db.insertSql(qry.sql1,'CDW1')
db.disconnect()