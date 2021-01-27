#!/usr/bin/python3

import math
import re
import sys


# Language features
#  re
#  string.split
#  open().readlines()

# Preparation:
#   read in file, then print numbered lines less comments
#   log_error
#   is_identifier_valid
#   get_val
#   eval_binary_op


def eval_binary_op(linenum, left_arg, op, right_arg):
    if op == '+':
        return left_arg + right_arg
    elif op == '-':
        return left_arg - right_arg
    elif op == '*':
        return left_arg * right_arg
    elif op == '/':
        return left_arg / right_arg
    else:
        log_error(linenum, 'Unknown binary operator: {0:s}'.format(op))
        sys.exit(-1)


def eval_unary_op(linenum, op, unary_arg):
    if op == 'sqrt':
        return math.sqrt(unary_arg)
    else:
        log_error(linenum, 'Unknown unary operator: {0:s}'.format(op))


def get_val(linenum, env, token):
    if token in env:
        return env[token]
    else:
        return float(token) 


def is_identifier_valid(identifier):
    pattern = '^[_a-z][_a-z0-9]*$'
    found = re.match(pattern, identifier)
    return found != None


def log_error(linenum, msg):
        print('Error at line #{0:d}: {1:s}'.format(linenum, msg))
        sys.exit(-1)

    
def unbar_sides(linenum, env, line):
    tokens = line.split(sep=' ')
    token_count = len(tokens)
    assert(token_count == 1 or (token_count >= 3 or token_count <= 5))
    if token_count == 1:
        return ('', 0.0)
    if tokens[1] != '=':
        print('tokens={0:s}'.format(tokens.__str__()))
        print('Not an equality token: "{0:s}"'.format(tokens[1]))
        log_error(linenum, 'Non-empty line lacks assignment operator')
    lhs = tokens[0]
    is_lhs_valid = is_identifier_valid(lhs)
    if not is_lhs_valid:
        log_error(linenum, 'Invalid identifier: {0:s}'.format(lhs)) 
    rhs = None
    if token_count == 3:
        rhs = get_val(linenum, env, tokens[2])
    elif token_count == 4:
        # RHS should be: <unary_op> <value>
        unary_op = tokens[2]
        unary_arg = get_val(linenum, env, tokens[3])
        rhs = eval_unary_op(linenum, unary_op, unary_arg)
    elif token_count == 5:
        # RHS should be: <left_val> <binary_op> <right_val>
        left_val = get_val(linenum, env, tokens[2])
        binary_op = tokens[3]
        right_val = get_val(linenum, env, tokens[4])
        rhs = eval_binary_op(linenum, left_val, binary_op, right_val)
    return (lhs, rhs)

 
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: unbin <filename>')
        sys.exit(-1)
    filename = sys.argv[1]
    script_lines = open(filename).readlines()
    env = dict()
    linenum = 0
    latest_val = None
    for line in script_lines:
        linenum += 1
        line = line.strip()
        line = ' '.join(line.split())
        if '#' in line:
            position = line.index('#')
            if position == 0:
                line = ''
            else:
                line = line[0:position - 1]
        line = line.strip()
        lhs, rhs = unbar_sides(linenum, env, line)
        if lhs == '':
            print('{0:d}: <empty>'.format(linenum))
        else: 
            # Note: lhs already confirmed to be a Validate identifier
            print('{0:d}: {1:s} = {2:f}'.format(linenum, lhs, rhs))
        if lhs != '':
            env[lhs] = rhs
            latest_val = rhs
    if latest_val == None:
        log_error(linenum, 'No assignments in script')
    else:
        print('Final result = {0:f}'.format(latest_val))
