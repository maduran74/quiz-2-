class Punto:
    def __init__(self, x=0, y=0):
        self.x = x;
        self.y = y;

    def __str__(self):
        return "({},{})".format(self.x,self.y)

    def cuadrante(self):
        # si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
        if self.x > 0 and self.y > 0:
            return 'Pertenece al primer cuadrante'
        elif self.x < 0 and self.y > 0:
            return 'Pertenece al segundo cuadrante'
        elif self.x < 0 and self.y < 0:
            return 'Pertenece al tercer cuadrante'
        elif self.x > 0 and self.y < 0:
            return 'Pertenece al cuarto cuadrante'
        elif self.x == 0 and self.y != 0:
            return 'Se situa sobre el eje X'
        elif self.x!=0 and self.y== 0:
            return 'Se situa sobre el eje Y'
        elif self.x==0 and self.y==0:
            return 'se situa sobre el origen'

    def vector(self, x0, y0):
        return [x0-self.x,y0-self.x]
