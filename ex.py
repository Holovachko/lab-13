import math


class TVector2D:
    def __init__(self, x=0, y =0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,a):
        self.__x = a
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,a):
        self.__y = a



    def vectors_len(self):
        return int(math.sqrt(self.x**2 + self.y**2)+1)
    def rationing_vector(self):
        return self.x/self.vectors_len(),self.y/self.vectors_len()

    def __gt__(self, other):
        return self.vectors_len() > other.vectors_len()
    def __lt__(self, other):
        return self.vectors_len() < other.vectors_len()
    def __add__(self, other):
        return (other.x + self.x , other.y + self.y)
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return (self.x *other.x + self.y * other.y)


v = TVector2D(7,1, 1,5,7)
v2 = TVector2D(10,4,5,9,1)
print(v + v2)
print(v.vector)
print(v.rationing_vector())


class TVector3D(TVector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def vector3D_len(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def __gt__(self, other):
        return self.vector3D_len() > other.vector3D_len()
    def __add__(self, other):
        return (self.x + other.x , self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return (self.x - other.x , self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)

q = TVector3D(10,11,6)
q1 = TVector3D(16,34,5)

if q > q1:
    print('True')
else:
    print('False')
