from database.conexao import conectar

class Usuario:
    def __init__ (self, usuario:str, senha:str, nome:str):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
    
    def cadastrar(self):
        conexao, cursor = conectar()
        cursor.execute("""
                        INSERT INTO cadastro (usuario, senha, nome)
                       VALUES(%s, %s, %s);
                            """, [self.usuario, self.senha, self.nome])
        conexao.commit()
        conexao.close()

    def logar(usuario:str, senha:str):
        conexao, cursor = conectar()
        cursor.execute("""
                        SELECT * FROM cadastro WHERE usuario = %s AND senha = %s;
                            """, [usuario, senha])
        resultado = cursor.fetchone()
        conexao.close()
        return resultado