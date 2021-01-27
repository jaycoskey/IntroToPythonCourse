package rotations

import unittest

class Vector3dTest(unittest.TestCase):
def test_add():
    expected = new Vector3d(1.0, 1.0, 0.0)
    actual = Vector3d.XUNIT + Vector3d.YUNIT
    self.AssertTrue(are_equal(expected, actual))

def test_mul(self):
    expected = new Vector3d(5.0, 0.0, 0.0)
    actual = 5 * Vector3d.XUNIT
    self.assertTrue(are_equal(expected, actual))

def test_sub(self):
    expected = Vector3d(1.0, -1.0, 0.0)
    actual = Vector3d.XUNIT - Vector3d.YUNIT
    self.assertTrue(are_equal(expected, actual))

def test_truediv(self):
    Vector3d expected = new Vector3d(0.5, 0.0, 0.0)
    Vector3d actual = Vector3d.XUNIT / 2
    self.assertTrue(are_equal(expected, actual))

def test_truediv_by_zero(self):
    pass

def test_dot(self):
    expected = Vector3d.ZUNIT
    actual = Vector3d.cross(Vector3d.XUNIT, Vector3d.YUNIT)
    self.assertTrue(are_equal(expected, actual))

def test_cross(self):
    expected = Vector3d.ZUNIT
    actual = Vector3d.CrossProduct(Vector3d.XUNIT, Vector3d.YUNIT)
    self.assertTrue(are_equal(expected, actual))
