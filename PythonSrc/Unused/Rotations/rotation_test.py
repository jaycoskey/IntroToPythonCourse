package Rotations

import unittest

class RotationTest:
    def test_constructors():
        pass

    def test_noncommutativity():
        axis1 = Vector3d(1.0, -4.0, 9.0)
        axis2 = Vector3d(1.0, 4.0, 9.0)
        angle1 = math.pi / 3
        angle2 = math.pi / 6
        r1 = Rotation(axis1, angle1)
        r2 = Rotation(axis2, angle2)
        result1 = r2(r1(vec1))
        result2 = r1(r2(vec1))
        self.assertTrue(is_zero(result1 - result2))

    def test_no_Rotation():
        rx0 = Rotation(Vector3d.XUNIT, 0.0)
        ry0 = Rotation(Vector3d.YUNIT, 0.0)
        rz0 = Rotation(Vector3d.ZUNIT, 0.0)
        vec = Vector3d(1.0, 2.0, 3.0)
        xvec = rx0(vec)
        yvec = ry(vec)
        zvec = rz(vec)
        self.assertTrue(are_equal(vec, xvec))
        self.assertTrue(are_equal(vec, yvec))
        self.assertTrue(are_equal(vec, zvec))

    def test_rotate()
        pass

    def test_xrotate():
        rx = Rotation(Vector3d.XUNIT, math.pi / 2)
        result = rx(Vector3d.YUNIT)
        self.assertTrue(are_equal(result, Vector3d.ZUNIT))

    def test_yrotate():
        ry = Rotation(Vector3d.YUNIT, math.pi / 2)
        result = ry(Vector3d.ZUNIT)
        self.assertTrue(are_equal(result, Vector3d.XUNIT))

    def test_zrotate()
        rz = Rotation(Vector3d.ZUNIT, math.pi / 2)
        result = rz(Vector3d.XUNIT)
        self.assertTrue(are_equal(result, Vector3d.YUNIT))
