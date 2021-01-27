#!/usr/bin/env python3

import argparse
import logging
import math
import sys

class Config:
    epsilon = 0.01
    gravity = -5.0
    initial_fuel = 87
    initial_height = 1007
    initial_time = 0
    initial_vel = 0
    max_burn_rate = 50
    min_burn_rate = 0
    soft_landing_threshold = -5
    std_dt = 1


class Lander:
    def __init__(self, init_height=Config.initial_height, init_vel=Config.initial_vel, init_fuel=Config.initial_fuel):
        self.height = init_height
        self.vel = init_vel
        self.fuel = init_fuel

        self.has_fuel = True
        self.has_landed = False
        self.std_dt = 1
        self.time = 0

    def advance_by_timestep(self, burn_rate, dt):
        acc = Config.gravity + burn_rate
        self.fuel   -= burn_rate * dt
        self.height += self.vel * dt + (0.5) * acc * dt**2
        self.vel    += acc * dt

    def get_contact_and_time(self, burn_rate, dt):
        '''Determine if contact with the surface is made.
        get_contact_and_time_exact is called to find the exact time of contact.'''
        acc = Config.gravity + burn_rate
        new_vel = self.vel + acc * dt
        if self.vel <= 0 or new_vel <= 0:
            (is_contact, contact_time) = self.get_contact_and_time_exact(acc, dt)
            if is_contact:
                self.has_landed = True
            return (is_contact, contact_time)
        else:
            LanderLog.log('get_contact_and_time: LANDER RISING: No need to get contact time')
            return (False, 0)

    def get_contact_and_time_exact(self, acc, dt):
        '''The quadratic formula determines the moment of contact, if any.
        If contact is not made, this function returns false.
        If contact is made, this function changes the value of the
        timestep variable, dt, to the time into the current timestep
        that contact took place, then returns true.'''
        if Util.is_zero(acc):
            # Solve for t in the equation x_0 + v_0 t = 0
            contact_time = -self.height / self.vel
            if contact_time > 0 and contact_time <= dt:
                return (True, contact_time)
            else:
                return (False, 0)
        else:
            # Solve for t in the equation x_0 + v_0 t + (1/2) acc t^2 = 0
            # Solution: t = (-v_0 +/- sqrt(v_0^2 - 2 acc x_0)) / acc
            # which_root = -1 * Util.sign(acc)
            radicand = self.vel**2 - 2*acc*self.height
            if radicand < 0:
                return (False, 0)
            sroot = math.sqrt(radicand)
            contact_times = [(-self.vel + which_root * sroot) / acc for which_root in [-1, 1]]
            contact_time_min = min(contact_times)
            contact_time_max = max(contact_times)
            # print('DEBUG: Contact times: {0}'.format(contact_times))
            # print('DEBUG: contact_time = (-self.vel + which_root * sroot) / acc = (-({0:.2f}) + {1} * {2:.2f}) / {3:.2f} = {4:.2f}'
            #        .format(self.vel, which_root, sroot, acc, contact_time))
            if contact_time_min > 0 and contact_time_min <= dt:
                return (True, contact_time_min)
            elif contact_time_max > 0 and contact_time_max <= dt:
                return (True, contact_time_max)
            else:
                # LanderLog.log('No contact in the relative time range [{0:.2f}, {1:.2f}].'.format(0, dt))
                return (False, 0)

class LanderLog:
    def log(str):
        # logging.log(logging.INFO, str)
        print(str)


class Player:
    def farewell(self):
        pass

    def get_burn_rate(lander, dt):
        pass

    def get_do_show_instructions(self):
        pass

    def write_state(event, time, lander):
        pass


class PlayerComputer(Player):
    def farewell(self):
        sys.exit(0)

    def get_burn_rate(self, lander, dt):
        '''TODO: Don't wait until we're below critical height to start burning fuel!'''
        # Formula from physics: (v_1)**2 = (v_0)**2 + 2 * acc * (h_1 - h_0)
        # To get safe landing, conditions, set h_1=0 and v_1=0.
        # Then acc = (v_0)**2 / (2*h_0)
        # So burn_rate = (v_0)**2 / (2*h_0) - gravity
        is_landing_inevitable = Config.max_burn_rate < (lander.vel**2 / lander.height) - Config.gravity
        # Note: There might not be enough fuel to last the entire timestep at this burn_rate.
        #       If this is the case, then the timestep is adjusted accordingly.
        burn_rate = Config.max_burn_rate if is_landing_inevitable else 0
        print('Burn rate={0:.2f}.'.format(burn_rate))
        return burn_rate

    def get_do_show_instructions(self):
        return False

    def write_state(self, event, time, lander):
        LanderLog.log('{0:s}: t={1:.4f}: height:{2:.4f}, velocity:{3:.4f}, fuel:{4:.4f}'.format(
            event, time, lander.height, lander.vel, lander.fuel))


class Util:
    def is_zero(x):
        '''Tests to see if a number has magnitude less than epsilon.'''
        return math.fabs(x) < Config.epsilon

    def offer(prompt):
        response = input(prompt)
        letter = response[0].lower()
        if letter == 'q':
            farewell()
        elif letter == 'n':
            return False
        else:
            return True

    def sign(x):
        return math.copysign(1, x)


def play_game(lander, player):
    time = Config.initial_time
    while not lander.has_landed:
        player.write_state('STATE', time, lander)
        dt = Config.std_dt
        if lander.has_fuel:
            burn_rate = player.get_burn_rate(lander, dt)
            if burn_rate * dt > lander.fuel:
                # If all the fuel is being used,
                # then set dt to time taken to burn the remaining fuel.
                dt = lander.fuel / burn_rate
        else:
            burn_rate = 0
        acc = Config.gravity + burn_rate

        (has_landed, new_dt) = lander.get_contact_and_time(burn_rate, dt)
        if has_landed:
            dt = new_dt
        lander.advance_by_timestep(burn_rate, dt)
        time += dt

        # Landing
        if lander.has_landed or lander.height < 0:
            print('DEBUG: height upon landing={0:f}'.format(lander.height))
            player.write_state('LANDING', time, lander)
            return

        # No landing
        print('No landing fuel check: fuel={0:f}'.format(lander.fuel))
        if lander.has_fuel and Util.is_zero(lander.fuel):
            print('Setting has_fuel to False')
            lander.has_fuel = False
            lander.fuel = 0
            burn_rate = 0
        if dt < Config.std_dt:
            # Determine what happens after the fuel runs out
            remaining_dt = Config.std_dt - dt
            (has_landed2, new_dt) = lander.get_contact_and_time(burn_rate, remaining_dt)
            if has_landed2:
                dt = new_dt
            lander.advance_by_timestep(burn_rate, dt)
            time += dt
            if has_landed2:
                write_state('LANDING', time, lander)
                return
        continue


if __name__ == '__main__':
    '''In this game you attempt to land softly on the moon.
    The gravity on the moon is 5 ft/sec^2.
    Each second, set the burn rate between 0 and 50 fuel units.
    It takes 5 units of fuel per second to maintain your speed.
    Using more will cause you to accelerate upward.
    Using less will cause you to accelearate downward.
    Try to land with a downward velocity of less than 5 ft/sec.'''
    parser = argparse.ArgumentParser(description='Play lunar lander!!!')
    parser.add_argument('--fuel', type=int, default=Config.initial_fuel,
            help='Initial fuel')
    parser.add_argument('--height', type=int, default=Config.initial_height,
            help='Initial height')
    args = parser.parse_args()

    lander = Lander()  # Use default values
    player = PlayerComputer()
    do_show_instructions = player.get_do_show_instructions()
    if do_show_instructions:
        player.show_instructions()
    play_game(lander, player)
