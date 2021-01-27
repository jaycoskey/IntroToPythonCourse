#!/usr/bin/env python3

package Rotations


import math


# TODO: JMC: Allow conversion to and from matrices
# TODO: JMC: Allow representation via Euler angles
# TODO: JMC: Add support for angular velocity (vector Quaternion class)
# TODO: JMC: Add support for distinguishing between body & space coordinates

##### See Vec impl at https://gist.github.com/rldotai/0b0e56c4dfb17cde00f2
##### abs, add, floordiv, matmul, mul, neg, pow, sub, radd, rfloordiv,
##### rmatmul, rmul, rpow, rsub, rtruediv, truediv


class Rotation:
    def __init__(self, *args):
        if len(args) == 0:
            _quat = Quaternion()
        elif len(args) == 1:
            _quat = args[0]
        elif len(args) == 2:
            axis = args[0].normalized()
            angle = args[1]
            sin = math.sin(angle/2)
            _quat = Quaternion(
                math.cos(angle/2),
                sin * axis.qx,
                sin * axis.qy,
                sin * axis.qz)

    def __call__(self, vec):
        return self.rotate(vec)

    def __str__(self):
        return "Rotation-" + _quat.__str__()

    def rotate(vec: vector3d) -> vector3d:
        '''The result of rotating a vector using a Quaternion is
            q * v * q^(-1),
        where R^3 is identified with the imaginary subspace of H (the Quaternions).'''
        v = vec.as_Quaternion()
        qinv = _quat.inverse()
        result = _quat * v * qinv
        return result.as_vector3d()

    def xrotate(angle):
        return Rotation(vector3d.XUNIT, angle)

    def yrotate(angle):
        return Rotation(vector3d.YUNIT, angle)

    def zrotate(angle):
        return Rotation(vector3d.ZUNIT, angle)
