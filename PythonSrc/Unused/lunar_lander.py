#!/usr/bin/env python3

# Lunar lander.

import argparse
import math
import sys

verbose = False


class Game:
    DEFAULT_INITIAL_FUEL = 100
    DEFAULT_INITIAL_HEIGHT = 300
    DEFAULT_INITIAL_VELOCITY = 0
    EPSILON = 0.01
    GRAVITY = -5.0
    MAX_BURN_RATE = 50
    MIN_BURN_RATE = 0
    SOFT_LANDING = -5

    def __init__(self, player, fuel, height, velocity):
        self.player = player
        self.fuel = fuel
        self.height = height
        self.velocity = velocity

    def get_contact_and_time(self, height, vel, acc, dt):
        """Determine if contact with the surface is made.
        This function calls get_contact_and_time_exact.
        Returns a pair (is_contact, contact_time)."""
        is_contact = False
        new_vel = vel + acc * dt
        new_height = height + vel*dt + (0.5 * acc * dt**2)
        if vel <= 0 or new_vel <= 0:
            (is_contact, contact_time) = self.get_contact_and_time_exact(
                                                  height, vel, acc, dt)
            return (is_contact, contact_time)
        else:
            self.player.vprint('get_contact_and_time: The lander is rising')
            return (False, 0)


    def get_contact_and_time_exact(self, height, vel, acc, dt):
        """If there is any contact, then we use the quadratic formula
        to determine the exact moment of contact.
        If contact is not made, this function returns (False, 0).
        If contact is made, this function changes the value of the
        timestep variable, dt, to the time into the current timestep
        that contact took place, then returns (True, contact_time)."""
        if Util.is_zero(acc):
            # Solve for t in the equation x_0 + v_0 t = 0
            contact_time = -height / vel
            if contact_time > 0 and contact_time <= dt:
                return (True, contact_time)
            else:
                return (False, 0)
        else:
            # Solve for t in the equation x_0 + v_0 t + (1/2) acc t^2 = 0
            # Solution: t = (-v_0 +/- sqrt(v_0^2 - 2 acc x_0)) / acc
            radicand = vel**2 - 2*acc*height
            if radicand < 0:
                return (False, 0)
            sroot = math.sqrt(radicand)
            contact_times = [ (-vel + which_root * sroot) / acc
                              for which_root in [-1, 1] ]
            contact_time_min = min(contact_times)
            contact_time_max = max(contact_times)
            if contact_time_min > 0 and contact_time_min <= dt:
                self.player.vprint('INFO: exact: contact_time={0:.2f}'
                               .format(contact_time_min))
                return (True, contact_time_min)
            elif contact_time_max > 0 and contact_time_max <= dt:
                self.player.vprint('INFO: exact: contact_time={0:.2f}'
                               .format(contact_time_max))
                return (True, contact_time_max)
            else:
                return (False, 0)

    def play_game(self, fuel, height, vel):
        has_fuel = True
        has_landed = False
        std_dt = 1
        time = 0

        while not has_landed:
            self.player.show_state(time, fuel, height, vel)
            dt = std_dt
            if has_fuel:
                burn_rate = self.player.get_burn_rate()
                if burn_rate * std_dt > fuel:
                    # If all the fuel is being used,
                    # then set dt to time taken to burn the remaining fuel.
                    dt = fuel / burn_rate
                    self.player.vprint('INFO: play_game: Fuel-abridged dt={0}'
                              .format(dt))
            else:
                burn_rate = 0
            acc = Game.GRAVITY + burn_rate

            (has_landed, new_dt) = self.get_contact_and_time(
                                            height, vel, acc, dt)
            if has_landed:
                dt = new_dt
            time   += dt
            fuel   -= burn_rate * dt
            height += vel * dt + (0.5) * acc * dt**2
            vel    += acc * dt

            # Landing
            if has_landed or height < 0:
                self.player.report_landing(time, vel, fuel)
                return

            # No landing
            if has_fuel and Util.is_zero(fuel):
                print('Out of fuel at t={0}.'.format(time))
                has_fuel = False
                fuel = 0
            if dt < std_dt:
                # Determine what happens after the fuel runs out
                dt = std_dt - dt
                self.player.vprint('INFO: Executing remaining dt={0:.2f}'
                          .format(dt))
                acc = Game.GRAVITY
                (has_landed2, new_dt) = self.get_contact_and_time(
                                                 height, vel, acc, dt)
                if has_landed2:
                    dt = new_dt
                time   += dt
                height += vel * dt + (0.5) * acc * dt**2
                vel    += acc * dt
                if has_landed2:
                    report_landing(time, vel, fuel)
                    return
            continue

    def game_loop(self):
        play_again = True
        do_show_instructions = self.player.offer_boolean(
                                        '\nShow instructions (y/n)? ')
        if do_show_instructions:
            self.player.show_instructions()
        self.player.print_newline()
        while play_again:
            self.play_game(
                     fuel=args.fuel, height=args.height, vel=args.velocity)
            play_again = self.player.offer_boolean('\nPlay again (y/n)? ')
            self.player.print_newline()


class Player:
    def farewell(self):
        print('Bye!')
        sys.exit(0)

    def get_burn_rate(self):
        burn_rate = -1.0
        while burn_rate < Game.MIN_BURN_RATE or burn_rate > Game.MAX_BURN_RATE:
            try:
                response = input('\tBurn rate? ')
                if response.lower().startswith("q"):
                    sys.exit(0)
                burn_rate = float(response)
            except KeyboardInterrupt:
                self.farewell()
            except:
                pass
        return burn_rate

    def offer_boolean(self, prompt):
        response = input(prompt)
        letter = response[0].lower()
        if letter == 'q':
            farewell()
        elif letter == 'n':
            return False
        else:
            return True

    def print_newline(self):
        print()

    def report_landing(self, time, vel, fuel):
        event = "landed safely" if vel >= Game.SOFT_LANDING else "crashed"
        print('At t={0:.2f}, you {1:s}.'.format(time, event))
        print('\tLanding speed = {0:.2f}'.format(math.fabs(vel)))
        if Util.is_zero(fuel):
            print('\tNo fuel remaining')
        else:
            print('\tFuel remaining = {0:.2f}'.format(fuel))

    def show_instructions(self):
        print('Attempt to land softly on the moon.')
        print('The gravity on the moon is 5 ft/sec^2.')
        print('Each second, set the burn rate between 0 and 50 fuel units.')
        print('It takes 5 units of fuel per second to maintain your speed.')
        print('Using more will cause you to accelerate upward.')
        print('Using less will cause you to accelearate downward.')
        print('A "soft" landing has a downward velocity of less than 5 ft/sec.')

    def show_state(self, time, fuel, height, vel):
        print('t={0:3.0f}: height:{1:7.2f}, velocity:{2:7.2f}, fuel:{3:7.2f}'
            .format(time, height, vel, fuel))

    def vprint(self, str):
        if verbose:
            print(str)

    def welcome(self):
        print("\n\t\t*** Welcome to Lunar Lander ***")


class Util:
    def is_zero(x):
        """Tests to see if a number has magnitude less than EPSILON."""
        return math.fabs(x) < Game.EPSILON

    def sign(x):
        return math.copysign(1, x)

def main(fuel, height, velocity):
    player = Player()
    game = Game(player, fuel, height, velocity)
    game.game_loop()
    player.farewell()


if __name__ == '__main__':
    # Example invocation syntax:
    #     python lunar_lander.py --verbose=True --height=300 --fuel=200
    parser = argparse.ArgumentParser(description='Play lunar lander!!!')
    parser.add_argument(
            '--fuel',
            type=int,
            default=Game.DEFAULT_INITIAL_FUEL,
            help='Initial fuel')
    parser.add_argument(
            '--height',
            type=int,
            default=Game.DEFAULT_INITIAL_HEIGHT,
            help='Initial height')
    parser.add_argument(
            '--velocity',
            type=int,
            default=Game.DEFAULT_INITIAL_VELOCITY,
            help='Initial velocity')
    parser.add_argument(
            '--verbose',
            type=bool,
            default=False,
            help='Whether or not to print out debugging information')
    args = parser.parse_args()

    verbose = args.verbose

    main(args.fuel, args.height, args.velocity)
