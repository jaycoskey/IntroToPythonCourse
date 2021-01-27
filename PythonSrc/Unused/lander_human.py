#!/usr/bin/env python3

import argparse
import math
import sys

EPSILON = 0.01
GRAVITY = -5.0
INITIAL_FUEL = 100
INITIAL_HEIGHT = 300
MAX_BURN_RATE = 50
MIN_BURN_RATE = 0
SOFT_LANDING = -5

verbose = False


def farewell():
    print('Bye!')
    sys.exit(0)


def get_burn_rate():
    burn_rate = -1.0
    while burn_rate < 0 or burn_rate > 50:
        try:
            response = input('\tBurn rate? ')
            if response.lower().startswith("q"):
                sys.exit(0)
            burn_rate = float(response)
        except KeyboardInterrupt:
            farewell()
        except:
            pass
    return burn_rate


def get_contact_and_time(height, vel, acc, dt):
    '''Determine if contact with the surface is made.
    get_contact_and_time_exact is called to find the exact time of contact.'''
    is_contact = False
    new_vel = vel + acc * dt
    new_height = height + vel*dt + (0.5 * acc * dt**2)
    if vel <= 0 or new_vel <= 0:
        (is_contact, contact_time) = get_contact_and_time_exact(height, vel, acc, dt)
        return (is_contact, contact_time)
    else:
        vprint('INFO: get_contact_and_time: LANDER RISING: No need to get contact time')
        return (False, 0)


def get_contact_and_time_exact(height, vel, acc, dt):
    '''The quadratic formula determines the moment of contact, if any.
    If contact is not made, this function returns false.
    If contact is made, this function changes the value of the
    timestep variable, dt, to the time into the current timestep
    that contact took place, then returns true.'''
    if is_zero(acc):
        # Solve for t in the equation x_0 + v_0 t = 0
        contact_time = -height / vel
        if contact_time > 0 and contact_time <= dt:
            return (True, contact_time)
        else:
            return (False, 0)
    else:
        # Solve for t in the equation x_0 + v_0 t + (1/2) acc t^2 = 0
        # Solution: t = (-v_0 +/- sqrt(v_0^2 - 2 acc x_0)) / acc
        which_root = sign(acc)
        radicand = vel**2 - 2*acc*height
        if radicand < 0:
            return (False, 0)
        sroot = math.sqrt(radicand)
        contact_time = (-vel + which_root * sroot) / acc
        if contact_time > 0 and contact_time <= dt:
            vprint('INFO: contact_time={0:.2f}'.format(contact_time))
            return (True, contact_time)
        else:
            vprint('INFO: contact_time ({0:.2f}) out of range'.format(contact_time))
            return (False, 0)


def is_zero(x):
    '''Tests to see if a number has magnitude less than EPSILON.'''
    return math.fabs(x) < EPSILON


def offer(prompt):
    response = input(prompt)
    letter = response[0].lower()
    if letter == 'q':
        farewell()
    elif letter == 'n':
        return False
    else:
        return True


def play_game(fuel, height):
    has_fuel = True
    has_landed = False
    std_dt = 1
    time = 0
    vel = 0

    while not has_landed:
        show_state(time, height, vel, fuel)
        dt = std_dt
        if has_fuel:
            burn_rate = ask_for_burn_rate()
            if burn_rate * std_dt > fuel:
                # If all the fuel is being used,
                # then set dt to time taken to burn the remaining fuel.
                dt = fuel / burn_rate
                vprint('INFO: play_game: Fuel-abridged dt={0}'.format(dt))
        else:
            burn_rate = 0
        acc = GRAVITY + burn_rate

        (has_landed, new_dt) = get_contact_and_time(height, vel, acc, dt)
        if has_landed:
            dt = new_dt
        time   += dt
        fuel   -= burn_rate * dt
        height += vel * dt + (0.5) * acc * dt**2
        vel    += acc * dt

        # Landing
        if has_landed or height < 0:
            report_landing(time, vel, fuel)
            return

        # No landing
        if has_fuel and is_zero(fuel):
            print('Out of fuel at t={0}.'.format(time))
            has_fuel = False
            fuel = 0
        if dt < std_dt:
            # Determine what happens after the fuel runs out
            dt = std_dt - dt
            vprint('INFO: Executing remaining dt={0:.2f}'.format(dt))
            acc = GRAVITY
            (has_landed2, new_dt) = get_contact_and_time(height, vel, acc, dt)
            if has_landed2:
                dt = new_dt
            time   += dt
            height += vel * dt + (0.5) * acc * dt**2
            vel    += acc * dt
            if has_landed2:
                report_landing(time, vel, fuel)
                return
        continue


def report_landing(time, vel, fuel):
    event = "landed safely" if vel >= -5 else "crashed"
    print('At t={0:.2f}, you {1:s}.'.format(time, event))
    print('\tLanding speed = {0:.2f}'.format(math.fabs(vel)))
    if fuel > EPSILON:
        print('\tFuel remaining = {0:.2f}'.format(fuel))
    else:
        print('\tNo fuel remaining')


def show_instructions():
    print('Attempt to land softly on the moon.')
    print('The gravity on the moon is 5 ft/sec^2.')
    print('Each second, set the burn rate between 0 and 50 fuel units.')
    print('It takes 5 units of fuel per second to maintain your speed.')
    print('Using more will cause you to accelerate upward.')
    print('Using less will cause you to accelearate downward.')
    print('Try to land with a downward velocity of less than 5 ft/sec')


def show_state(time, height, vel, fuel):
    print('t={0:3.0f}: height:{1:7.2f}, velocity:{2:7.2f}, fuel:{3:7.2f}'.format(time, height, vel, fuel))


def sign(x):
    return math.copysign(1, x)


def vprint(str):
    if verbose:
        print(str)


def welcome():
    print("\n\t\t*** Welcome to Lunar Lander ***")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play lunar lander!!!')
    parser.add_argument('--fuel', type=int, default=INITIAL_FUEL,
            help='Initial fuel')
    parser.add_argument('--height', type=int, default=INITIAL_HEIGHT,
            help='Initial height')
    parser.add_argument('--verbose', type=bool, default=False,
            help='Whether or not to print out debugging information')
    args = parser.parse_args()

    verbose = args.verbose
    play_again = True
    do_show_instructions = offer('\nShow instructions (y/n)? ')
    if do_show_instructions:
        show_instructions()
    print('')
    while play_again:
        play_game(fuel=args.fuel, height=args.height)
        play_again = offer('\nPlay again (y/n)? ')
        print('')
    farewell()
