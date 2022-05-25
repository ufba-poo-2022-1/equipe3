from backend.model.user import User

class Landlord(User):
  def __init___init__(self, id, name, email, password, celphone, address,imovel_id, imovel):
    super().__init__(self, id, name, email, password, celphone, address)
    self.imovel_id = imovel_id
    self.imovel = imovel
