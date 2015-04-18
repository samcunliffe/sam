"""Particle data"""

from uncertainties import ufloat as measurednumber


class ParticleData:
    def __init__(self, name, (mass, masserror)):
        self.name = name
        self.mass = measurednumber(mass, masserror)

    def __str__(self):
        return 'Data for the '+self.name

    def msq(self):
        return self.mass*self.mass


B0 = ParticleData("B0", (5279.58, 0.17))
