import sqlalchemy as db

engine = db.create_engine('mysql+pymysql://root:@localhost/login')
connection = engine.connect()
metadata = db.MetaData()

census = db.Table('login_info', metadata,autoload=True,autoload_with=engine)

query = db.select([census])

ResultProxy = connection.execute(query)

ResultSet = ResultProxy.fetchall()

print(ResultSet[:3])


