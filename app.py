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
    
    def insert(self):
        query = "INSERT INTO usuarios VALUES ('"+self.user+"','"+self.password+"')"
        return query
    def login(user,password):
        query = "SELECT * FROM usuarios WHERE usuario = '"+user+"' AND pass = '"+password+"'"
#query = """SELECT * FROM usuarios"""
user = input("ingresar usuario")
password = input("ingresar contraseña")

activeuser = usuario(user,password)

print (activeuser.insert())
#cursor.execute(query)

#records = cursor.fetchall()
#for r in records:
#    print(f"{r['id']}\t{r['usuario']}\t{r['pass']}")