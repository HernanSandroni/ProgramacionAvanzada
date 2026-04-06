class Punto:  #ejercicio 2
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
    
p1 = Punto(5, 10)

print(p1.impresion())        
print(p1.eje_x())            
print(p1.eje_y())            

p2 = p1.opuesto()
print(p2.impresion())        

print(p1.distancia_origen()) 
     
#ejercicio3

class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a 
        self._punto_b = punto_b

    def mueve_derecha(self, d):
        self._punto_a.x += d
        self._punto_b.x += d

    def mueve_izquierda(self, d):
        self._punto_a.x -= d
        self._punto_b.x -= d  

    def mueve_arriba(self, d):
        self._punto_a.y += d
        self._punto_b.y += d

    def mueve_abajo(self, d):
        self._punto_a.y -= d
        self._punto_b.y -= d

    def impresion(self):
        return f"A{self._punto_a.impresion()} - B{self._punto_b.impresion()}"    

p1 = Punto(3, 7)
p2 = Punto(8, 11)

linea = Linea(p1, p2)

print(linea.impresion())

linea.mueve_derecha(3)
print(linea.impresion())

linea.mueve_abajo(4)
print(linea.impresion())