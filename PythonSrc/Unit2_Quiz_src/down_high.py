#!/usr/bin/env python3

class Down:
    def down(s):
        print('Calling down with arg {0:s}'.format(s))
        if len(s) > 1:
            return s[0].lower() + High.high(s[1::])
        else:
            return ''


class High:
    def high(s):
        print('Calling high with arg {0:s}'.format(s))
        if len(s) > 1:
            return s[0].upper() + Down.down(s[1::])
        else:
            return ''


print(Down.down('Hello'))
