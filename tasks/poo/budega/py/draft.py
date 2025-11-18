class cliente:
    def _init_(self, nome:str):
        self.__nome = nome
    
    def getnome(self) -> str:
        return self.__nome
    
    def _str_(self) -> str:
        return f"{self.__nome}"
    
class Mercantil:
    def __init__(self, qtdcaixa:int):
        self.caixa: list[cliente | None] = [None] * qtdcaixa
        self.qtdcaixa = qtdcaixa
        self.fila: list[cliente | None] = []

    def __str__(self) -> str:
        caixas: list[str] = list(map(lambda cliente: '-----' if cliente is None else cliente.getnome(), self.caixa))
        strCaixasFinal: str = "[" +", ".join(caixas) + "]"
        fila: list[str] = list(map(lambda p: "" if p is None else p.getnome(), self.fila))
        strFilaFinal: str = "[" +", ".join(fila) + "]"
        return f"Caixas: {strCaixasFinal}\nEspera: {strFilaFinal}"
    
    def chegar (self, nome: cliente | None) -> None:
        self.fila.append(nome)
        return
    
    def chamar(self, number: int):
        if not self.fila:
            print("fail: sem cliente")
            return
        
    

        





