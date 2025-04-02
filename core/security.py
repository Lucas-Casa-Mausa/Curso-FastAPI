from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=['bcrypt'],deprecated ='auto')

def verificar_senha(senha:str,has_senha:str) -> bool:
    """
    Função para verificar se a senha está correta, comparando a senha em texto puro, informada pelo usuário, e o hash da senha que estará salvo no banco de dados durante a criação da conta
    """ 
    return CRIPTO.verify(senha,has_senha)

def gerar_hash_senha(senha:str) -> str :
    """
    Função que gera e retorna o HASH da senha
    """
    return CRIPTO.hash(senha)