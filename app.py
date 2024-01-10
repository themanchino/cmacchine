import pymssql

conn = pymssql.connect(
    server='127.0.0.1',
    port='1433',
    user='cmacchine',
    password='ligh',
    database='cmacchine',
    as_dict=True
) 
cursor = conn.cursor()

class usuario:
    def __init__(self,user,password):
        self.user = user
        self.password = password

    def __str__(self):
        return f"{self.user}({self.password})"
    
    def insert(user,password):
        query = "INSERT INTO usuarios VALUES ('"+user+"','"+password+"')"
        return query
    def login(user,password):
        query = "SELECT * FROM usuarios WHERE usuario = '"+user+"' AND pass = '"+password+"'"
#query = """SELECT * FROM usuarios"""
usuario

cursor.execute(query)

records = cursor.fetchall()
for r in records:
    print(f"{r['id']}\t{r['usuario']}\t{r['pass']}")