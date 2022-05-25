
from email import feedparser


class Rent:
    
  def __init__(self, id, id_landlord, id_tenant, id_building, initial_date, final_date, projected_date, total, fee, creation_date):
    self.id = id
    self.id_landlord = id_landlord	
    self.id_tenant = id_tenant
    self.id_building = id_building
    self.initial_date = initial_date
    self.final_date = final_date
    self.projected_date = projected_date
    self.total = total
    self.fee = fee
    self.creation_date = creation_date

  def get_dados(self):
      l = [self.id,self.id_landlord,self.id_tenant,self.id_building,self.initial_date,self.final_date,self.projected_date,self.total,self.fee,self.creation_date]
      return l


