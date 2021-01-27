# package rotations

import unittest


import quaternion


class QuaternionTest(unittest.TestCase):
    def test_add(self):
        expected = Quaternion(0.0, 1.0, 1.0, 0.0)
        actual = Quaternion.QI + Quaternion.QJ
        unittest.assertTrue(are_equal(expected, actual))

    def test_conjugation(self):
        pass

    def test_constructors(self):
        pass

    def test_exp_and_log(self):
        qIEL = quat.exp(quat.log(quat.QI))
        qILE = quat.log(quat.exp(quat.QI))

        qJEL = quat.exp(quat.log(quat.QJ))
        qJLE = quat.log(quat.exp(quat.QJ))

        qKEL = quat.exp(quat.log(quat.QK))
        qKLE = quat.log(quat.exp(quat.QK))

        qII = pow(quat.QI, 2.0)
        qJJ = pow(quat.QJ, 2.0)
        qKK = pow(quat.QK, 2.0)

        self.assertTrue(are_equal(qIEL, qILE))
        self.assertTrue(are_equal(qIEL, qILE))

        self.assertTrue(are_equal(qJEL, qJLE))
        self.assertTrue(are_equal(qJEL, qJLE))

        self.assertTrue(are_equal(qKEL, qKLE))
        self.assertTrue(are_equal(qKEL, qKLE))

        self.assertTrue(are_equal(qII, -Quaternion.QR))
        self.assertTrue(are_equal(qJJ, -Quaternion.QR))
        self.assertTrue(are_equal(qKK, -Quaternion.QR))

    def test_inverse(self):
        pass

    def test_mul(self):
        II = quat.QI * quat.QI
        IJ = quat.QI * quat.QJ
        IK = quat.QI * quat.QK
        JI = quat.QJ * quat.QI
        JJ = quat.QJ * quat.QJ
        JK = quat.QJ * quat.QK
        KI = quat.QK * quat.QI
        KJ = quat.QK * quat.QJ
        KK = quat.QK * quat.QK

        self.assertTrue(are_same(II, -quat.QR))
        self.assertTrue(are_same(IJ, quat.QK))
        self.assertTrue(are_same(IK, -quat.QJ))
        self.assertTrue(are_same(JI, -quat.QK))
        self.assertTrue(are_same(JJ, -quat.QR))
        self.assertTrue(are_same(JK, quat.QI))
        self.assertTrue(are_same(KI, quat.QJ))
        self.assertTrue(are_same(KJ, -quat.QI))
        self.assertTrue(are_same(KK, -quat.QR))

    def test_sub(self):
        pass

    def test_slerp(self):
        pass

    def test_str(self):
        pass

    def test_sub(self):
        expected = Quaternion(0.0, 1.0, -1.0, 0.0)
        actual = quat.QI - quat.QJ
        self.assertTrue(are_equal(expected, actual))

    def test_truediv(self):
        expected = 0.5 * Quaternion.QI
        actual = quat.QI / 2
        self.assertTrue(are_equal(expected, actual))

    def test_as_vector3d(self):
        pass

if __name__ == '__main__':
    unittest.main()
