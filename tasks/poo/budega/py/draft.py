class cliente:
    def _init_(self, nome:str):
        self._nome = nome
    
    def getnome(self) -> str:
        return self.__nome
    
    def _str_(self) -> str:
        return f"{self._nome}"
    
class Mercantil:
    def _init_(self, qtdcaixa:int):
        self.caixa = qtdcaixa
        self.qtdcaixa = [None] * qtdcaixaself.fila = [None]
        
        