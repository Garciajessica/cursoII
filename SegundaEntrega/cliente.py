import metodoPago


class cliente():
    def __init__(self,name,lasname, Adress, postalCode,CodigoCliente ):
      self.name= name
      self.lasname= lasname
      self.Adress= Adress
      self.postalCode= postalCode
      self.codigoCliente= CodigoCliente

    def compra(self, compra):
      self.compra = compra


    def __str__(self):
      return f"El metodo de pago del cliente {self.name} fue {self.metodosDePago} el cual fue {self.EstadoDePagos}.__name__"


        
clienteUno = cliente("Juana","Garcia","Cordoba 123","CP1408" "JG12")
clienteDos = cliente("Joana","Garcia","Cordoba 123","CP1408" "JG13")


