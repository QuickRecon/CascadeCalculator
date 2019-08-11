class Cylinder:

    _gasloss = 5 # Fudge factor for gas lost during the transfer due to whips and such

    def __init__(self, volume, pressure, label, max_pressure):
        self.volume = volume
        self.pressure = pressure
        self.label = label
        self.max_pressure = max_pressure

    def transfill(self, cylinder):
        pv1 = self.volume * self.pressure
        pv2 = cylinder.volume * cylinder.pressure

        volume_sum = self.volume + cylinder.volume

        new_pressure = ((pv1+pv2)/volume_sum) - self._gasloss

        if new_pressure > self.max_pressure:
            self.pressure = self.max_pressure
            pv3 = self.volume * self.pressure  # Now we need to go "backwards" to get the pressure in the bank

            cylinder.pressure = ((pv1 + pv2-pv3)/cylinder.volume) - self._gasloss
        else:
            self.pressure = new_pressure
            cylinder.pressure = new_pressure

    def print_cylinder(self):
        print("Cylinder: " + self.label)
        print("Size: " + str(self.volume) + " L")
        print("Pressure: " + str(round(self.pressure)) + " bar")

    def copy(self):
        return Cylinder(self.volume, self.pressure, self.label, self.max_pressure)
