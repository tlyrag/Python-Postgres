import postgres_controller as db
sql1 = """
    INSERT INTO public."Test"("Vendor")
	VALUES (%s);
"""
db.connect()
db.insertSql(sql1,'CDW1')
db.disconnect()