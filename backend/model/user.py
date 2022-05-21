
class User:
    #Todo - Use hash for password
  def __init__(self, id, name, email, password, celphone, address):
    self.id = id
    self.name = name
    self.email = email
    self.password = password
    self.celphone = celphone
    self.address = address

  def get_id(self):
      return self.id

  def get_data(self):
      l = [self.id,self.name,self.email,self.password,self.celphone,self.addresss]
      return l

  def set_cellphone(self,number):
      self.celphone = number
      return 0 

  def set_email(self,email):
      self.email = email
      return 0

  def set_password(self,password):
      self.password = password
      return 0    