#!/usr/bin/env python3

def update(env,  key, val):
    env[key] = val


if __name__ == '__main__':
    env = dict()
    update(env, 'x', 1)
    update(env, 'y', 2)
    update(env, 'z', 3)
    print(env)
