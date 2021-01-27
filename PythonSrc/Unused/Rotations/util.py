# package rotations

EPSILON = 0.00001

def are_equal(x, y):
    return is_zero(x - y)

def is_zero(x):
    t = type(x)
    if t == Quaternion or t == Vector3d:
        return is_zero(x.length())
    else:
        return math.fabs(x) < EPSILON
