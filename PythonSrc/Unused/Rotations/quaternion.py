#!/usr/bin/env python3

import util

EPSILON = 0.0001;


class Quaternion:
    def __init__(self, *args):
        if len(args) == 0:
            self.qr = self.qi = self.qj = self.qk = 0.0
        elif len(args) == 1:
            arg0 = args[0]
            if type(arg0) == type(self):  # arg0 = a Quaternion
                self.qr = other.qr
                self.qi = other.qi
                self.qj = other.qj
                self.qk = other.qk
            else:
                self.qr = arg0
                self.qi = self.qj = self.qk = 0.0
        elif len(args) == 2:  # Axis & angle
            TODO
        elif len(args) == 4:
            self.qr = args[0]
            self.qi = args[1]
            self.qj = args[2]
            self.qk = args[3]
        else:
            raise ValueError('Constructor takes 0, 1, 2, or 4 arguments.')

    def __add__(self, other):
        if type(other) == type(self):
            return Quaternion(self.qr + other.qr, self.qi + other.qi, self.qj + other.qj, self.qk + other.qk)
        else:
            return Quaternion(self.qr + other, self.qi, self.qj, self.qk)

    def __mul__(self, other):
        if type(other) == type(self):
            return Quaternion(
                self.qr * other.qr - self.qi * other.qi - self.qj * other.qj - self.qk * other.qk,
                self.qr * other.qi + self.qi * other.qr + self.qj * other.qk - self.qk * other.qj,
                self.qr * other.qj + self.qj * other.qr + self.qk * other.qi - self.qi * other.qk,
                self.qr * other.qk + self.qk * other.qr + self.qi * other.qj - self.qj * other.qi)
        else:
            return Quaternion(other * self.qr, other * self.qi, other * self.qj, other * self.qk)

    def __pos__(self):
            return Quaternion(self.qr, self.qi, self.qj, self.qk)

    def __neg__(self):
        return Quaternion(-self.qr, -self.qi, -self.qj, -self.qk)

    def __str__():
        return '{0:.2f} + {1:.2f}i + {2:.2f}j + {3:.2f}k'.format(self.qr, self.qi, self.qj, self.qk)

    def __sub__(self, other):
        if type(other) == type(self):
            return Quaternion(self.qr - other.qr, self.qi - other.qi, self.qj - other.qj, self.qk - other.qk)
        else:
            return Quaternion(self.qr - other, self.qi, self.qj, self.qk)

    def __truediv__(self, other):
        if type(other) == type(self):
            return Quaternion(self * other.inverse())
        else:
            return Quaternion(self.qr / other, self.qi / other, self.qj / other, self.qk / other)

    def as_vector(self):
        '''Return a 3D vector representing the non-real components of the argument.
        Note: This should only be called on vector Quaternions.'''
        return vector(self.qi, self.qj, self.qk)

    def conjugate(self):
        return Quaternion(self.qr, -self.qi, -self.qj, -self.qk)

    def diffnorm(self, other):
        return (self - other).length()

    def inverse(self):
        return self.conjugate() / this.length()

    def norm(self):
        norm2 = self.norm2()
        return math.sqrt(norm2)

    def norm2(self):
        norm2 = (self * self.conjugate()).qr
        return norm2

# ---------------------------------------- 

Quaternion.Q0 = Quaternion(0.0, 0.0, 0.0, 0.0)
Quaternion.QR = Quaternion(1.0, 0.0, 0.0, 0.0)
Quaternion.QI = Quaternion(0.0, 1.0, 0.0, 0.0)
Quaternion.QJ = Quaternion(0.0, 0.0, 1.0, 0.0)
Quaternion.QK = Quaternion(0.0, 0.0, 0.0, 1.0)

# ---------------------------------------- 

def exp(q):
    '''Just as e ** (i * pi) == -1, it's also true that e ** (v * PI) == -1 for any unit vector Quaternion, v.'''
    norm = q.norm()
    try:
        unit_quat = q / norm
    except:
        unit_quat = q
    result = math.cos(norm) * q.qr + math.sin(norm) * unit_quat
    result *= math.exp(q.qr)
    return result

def log(q):
    '''TODO: Document the cut point for the complex log function.
    If q = r (cos A + v * sin A), then Log(q) = r + v * A,
    where r is the norm of q, and v is a vector Quaternion.
    (i.e., a vector Quaternion is one with zero real component.)'''
    norm = q.norm()
    normalizedArg = Quaternion(q / norm);
    vectorComponent = Quaternion(normalizedArg);

    # If the argument is close to being purely real, then return the real Log.
    # This safeguards against NaNs, and saves cycles.
    realComponent = normalizedArg.qr;
    angle = math.arccos(realComponent)  # Angle between q and unity.
    vectorComponent.qr = 0.0;
    vectorComponentLength = vectorComponent.norm()
    if is_zero(vectorComponentLength):
        return Quaternion(math.log(realComponent))
    else:
        vectorComponent = vectorComponent / vectorComponent.norm()
        result = Quaternion(math.log(norm)) + angle * vectorComponent
        return result;


def pow(q1, q2):
    '''Note: Since Quaternions are non-commutative,
    it is NOT always the case that log(x**y) = y * log(x) = log(x) * y.
    To make the definition of pow(q1, q2) well-defined, the second argument should be real.
    This is a sufficient, but not necessary condition.'''
    return(exp(q2 * q1.log(x)))


def slerp(a, b, t):
    '''Spherical Linear Interpolation ("Slerp") of Quaternions yeilds natural transitions from one rotation to another.
    x = Starting Quaternion
    y = Ending Quaternion
    z = Time, which goes from 0 to 1'''
    return pow(x, 1-t) * pow(y, t)
