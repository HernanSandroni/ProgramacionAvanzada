class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x  

    def eje_y(self):
        return self.y  
    
    def impresion(self): #metodoDeImpresion
        return f"({self.x}, {self.y})"
    
    def opuesto(self): #metodoOpuesto
        return Punto(-self.x, -self.y)
    
    def distancia_origen(self):
        return (self.x**2 + self.y**2) ** 0.5
    
p1 = Punto(3, 4)

print(p1.impresion())        
print(p1.eje_x())            
print(p1.eje_y())            

p2 = p1.opuesto()
print(p2.impresion())        

print(p1.distancia_origen()) 
     

