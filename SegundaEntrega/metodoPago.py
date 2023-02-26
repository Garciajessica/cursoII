from cliente import compra 

class metodosDePago:
    
    def __init__(self, tarjeta, efectivo):
        self.tarjeta= tarjeta
        self.efectivo= efectivo

    def EstadoDePagos(self):
        if self.tarjeta == True:
            print('pago aprobado')
        elif self.efectivo >= self.compra:
            print('pago aprobado')
        else:
            print('pago rechazado')
