"""created by Katrina Huber-Juma for a Hackbright Academy lecture, Jan 2021"""


class Savage:
    """ define the Plantonic Ideal of a Savage
    
    Specifically 'Savage' as described by Megan Thee Stallion """

    # class attributes shared by all instances of class Savage
    classy_bougie_ratchet = True
    sassy_moody_nasty = 100

    def __init__(self, name, esteem, money):
        """ Set instance attributes expected on all instances of class Savage"""
        self.name = name
        self.esteem = esteem
        self.money = money 
    
    def __repr__(self):
        return f'<Savage name: {self.name}, esteem: {self.esteem}, money: {self.money}>'

    def actin_stupid(self):
        print('what\'s happenin?')
        print('what\'s happenin?')
        return f'I\m {self.name}'

    def release_hit(self):
        self.money *= 2
        return self.money


if __name__ == '__main__':
    thee = Savage('Megan Thee Stallion', 100, 100)
    bey = Savage('Beyonce', 100, 100)
    rd = Savage('Raindrop', 100, 0)

    lst_of_instances = [thee, bey, rd]