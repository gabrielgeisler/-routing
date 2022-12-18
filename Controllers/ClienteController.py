import services.database as db;
import models.Cliente as cliente;
import models.Deposito as deposito;
import models.Motorista as motorista;

def Incluir(cliente):
    db.cursor.execute("""
    INSERT INTO dbo.Cliente (cliNome, cliLatitude, cliLongitude) 
    VALUES (?,?,?)""",
    cliente.nome, cliente.latitude, cliente.longitude).rowcount
    db.cnxn.commit()
    
def IncluirMotorista(motorista):
    db.cursor.execute("""
    INSERT INTO dbo.MOTORISTA (motNome, motPlaca, motHoraInicio, motHoraFim, idDeposito) 
    VALUES (?,?,?,?,?)""",
    motorista.nome, motorista.placa, motorista.inicio, motorista.fim, motorista.deposito).rowcount
    db.cnxn.commit()

def IncluirDeposito(deposito):
    db.cursor.execute("""
    INSERT INTO dbo.DEPOSITO (depNome, depLatitude, depLongitude, depHoraInicio, depHoraFim) 
    VALUES (?,?,?,?,?)""",
    deposito.nome, deposito.latitude, deposito.latitude, deposito.inicio, deposito.fim).rowcount
    db.cnxn.commit()

def SelecionarById(id):
    db.cursor.execute("SELECT * FROM dbo.CLIENTE WHERE ID = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1],row[2], row[3]))

    return costumerList[0]

def SelecionarMotoristaById(id):
    db.cursor.execute("SELECT * FROM dbo.MOTORISTA WHERE ID = ?", id)
    motoristaList = []

    for row in db.cursor.fetchall():
        motoristaList.append(motorista.Motorista(row[0], row[1],row[2], row[3]))

    return motoristaList[0]

def SelecionarByIdDeposito(id):
    db.cursor.execute("SELECT * FROM dbo.DEPOSITO WHERE ID = ?", id)
    depositoList = []

    for row in db.cursor.fetchall():
        depositoList.append(deposito.Deposito(row[0], row[1],row[2], row[3], row[4], row[5]))

    return depositoList[0]

def EncontrarIdDeposito(nome):
    db.cursor.execute("SELECT ID FROM dbo.DEPOSITO WHERE depNome = ?", nome)
    idDeposito = []

    for row in db.cursor.fetchall():
        idDeposito.append(row)

    return idDeposito[0][0]

def Alterar(cliente):
    db.cursor.execute("""
    UPDATE dbo.Cliente
    SET cliNome = ?, cliLatitude = ?, cliLongitude = ?
    WHERE id = ?
    """,
    cliente.nome, cliente.latitude, cliente.longitude, cliente.id).rowcount
    db.cnxn.commit()
    
def AlterarMotorista(motorista):
    db.cursor.execute("""
    UPDATE dbo.MOTORISTA
    SET motNome = ?, motPlaca = ?, motHoraInicio = ?, motHoraFim = ?
    WHERE id = ?
    """,
    motorista.nome, motorista.placa, motorista.inicio, motorista.fim, motorista.id).rowcount
    db.cnxn.commit()

def AlterarDeposito(deposito):
    print("alterando...")
    db.cursor.execute("""
    UPDATE dbo.Deposito
    SET depNome = ?, depLatitude = ?, depLongitude = ?
    WHERE id = ?
    """,
    deposito.nome, deposito.latitude, deposito.longitude, deposito.id).rowcount
    db.cnxn.commit()

def Excluir(id):
    db.cursor.execute("""
    DELETE FROM dbo.CLIENTE WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()
    
def ExcluirMotorista(id):
    db.cursor.execute("""
    DELETE FROM dbo.MOTORISTA WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()

def ExcluirDeposito(id):
    db.cursor.execute("""
    DELETE FROM dbo.DEPOSITO WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM dbo.CLIENTE")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1],row[2], row[3]))

    return costumerList

def SelecionarTodosCliente():
    teste = db.cursor.execute("SELECT cliNome FROM dbo.CLIENTE")
    todosClientes = []
    
    for i in teste:
        for j in i:
            todosClientes.append(j)
    
    return todosClientes

def SelecionarLatLongOrigem(latorigem):
    latLong = db.cursor.execute("SELECT cliLatitude, cliLongitude FROM dbo.CLIENTE WHERE cliNome = ?", latorigem)
    todosLatlong = []
    
    for i in latLong:
        for j in i:
            todosLatlong.append(j)
    
    return todosLatlong

def SelecionarLatLongDestino(latdestino):
    teste = db.cursor.execute("SELECT depLatitude, depLongitude FROM dbo.DEPOSITO WHERE depNome = ?", latdestino)
    todosLatlong = []
    
    for i in teste:
        for j in i:
            todosLatlong.append(j)
    
    return todosLatlong

def SelecionarTodosDepositos():
    teste = db.cursor.execute("SELECT depNome FROM dbo.DEPOSITO")
    todosDepositos = []
    
    for i in teste:
        for j in i:
            todosDepositos.append(j)
    
    return todosDepositos

def SelecionarTodosClientes():
    teste = db.cursor.execute("SELECT cliNome FROM dbo.CLIENTE")
    todosClientes = []
    
    for i in teste:
        for j in i:
            todosClientes.append(j)
    
    return todosClientes
    
def SelecionarTodosDeposito():
    db.cursor.execute("SELECT * FROM dbo.DEPOSITO")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(deposito.Deposito(row[0], row[1],row[2], row[3], row[4], row[5]))

    return costumerList

def SelecionarTodosMotoristas():
    db.cursor.execute("SELECT * FROM dbo.MOTORISTA")
    motoristaList = []

    for row in db.cursor.fetchall():
        motoristaList.append(motorista.Motorista(row[0], row[1],row[2], row[3], row[4], row[5]))

    return motoristaList