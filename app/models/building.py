
class Building:
    #Todo - Use hash for password
  def __init__(self, id, tipo, descricao, endereco, valor, area, esta_disponivel):
    self.id = id
    self.tipo = tipo
    self.descricao = descricao
    self.endereco = endereco
    self.valor = valor
    self.area = area
    self.esta_disponivel = esta_disponivel


  def get_dados(self):
      l = [self.id,self.tipo,self.descricao,self.endereco,self.valor,self.area,self.esta_disponivel]
      return l

