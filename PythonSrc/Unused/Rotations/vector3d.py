package rotations

import unittest

class Vector3d:
    ZERO = Vector3d(0.0, 0.0, 0.0)
    XUNIT = Vector3d(1.0, 0.0, 0.0)
    YUNIT = Vector3d(0.0, 1.0, 0.0)
    ZUNIT = Vector3d(0.0, 0.0, 1.0)

    def __init__(self, *args):
        if len(args) == 0:
            self.x = self.y = self.z = 0.0
        elif len(args) == 1:
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z
        elif len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        else:
            raise ValueError('Vector3d() requires 0, 1, or 3 arguments')

    def __add__(other): 
        return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(other):
        return Vector3d(other * v.x, other * v.y, other * v.z)

    def __rmul__(other):
        return Vector3d(other * v.x, other * v.y, other * v.z)
 
    def __str__():
        return '({0:f}, {1:f}, {2:f})'.format(self.x, self.y, self.z)
 
    def __sub__(other): 
        return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(other):
        return Vector3d(self.x / other, self.y / other, self.z / other)

    def as_quaternion():
        '''Identifies the imaginary subspace of quaternionic space with R^3.'''
        return quaternion(0.0, self.x, self.y, self.z)

    @staticmethod
    def cross(a, b):
        result = Vector3d(
            a.Y * b.Z - a.Z * b.Y,  
            a.Z * b.X - a.X * b.Z,  
            a.X * b.Y - a.Y * b.X )
        return result

    def cross(self, b):
        return Vector3d.cross(self, b)

    @staticmethod
    def dot(a, b):
        return(a.x * b.x + a.y * b.y + a.z * b.z) 

    def interpolate(a, b, t):
        return (1 - t) * a + t * b

    def norm(self):
        return math.sqrt(self.norm2())

    def norm2(self):
        return self.x ** 2 + self.y ** 2 +  self.z ** 2
