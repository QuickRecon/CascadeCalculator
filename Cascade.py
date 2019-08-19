import Cylinder

# Bank Parameters
fills = 1
empty_pressure = 50
bank = [Cylinder.Cylinder(12, 232, "Bank 1", 232),
        Cylinder.Cylinder(12, 232, "Bank 2", 232),
        Cylinder.Cylinder(11.6, 240, "AL 95 1", 240),
        Cylinder.Cylinder(11.6, 240, "AL95 2", 240)]

target = [Cylinder.Cylinder(5.7, empty_pressure, "Target 1", 200),
          Cylinder.Cylinder(5.7, empty_pressure, "Target 2", 200)]


def print_state(label):
    print("------------------------------------------------------------")
    print(label + " bank state:")
    print()
    for ii in bank:
        ii.print_cylinder()
        print()  # newline

    print("------------------------------------------------------------")
    print(label + " target state:")
    print()  # newline
    for ii in target:
        ii.print_cylinder()
        print()  # newline


def main():
    print_state("Starting")
    for i in range(1, fills+1):
        # Combine target tanks into 1 big tank for the sake of analysis
        combined_target = target[0].copy()
        combined_size = 0

        for ii in target:
            combined_target.transfill(ii)
            combined_size += ii.volume

        combined_target.volume = combined_size

        for ii in bank:
            if combined_target.pressure != combined_target.max_pressure:
                combined_target.transfill(ii)

        for ii in target:
            ii.pressure = combined_target.pressure

        print("------------------------------------------------------------")
        print_state("Fill " + str(i))

        for ii in target:
            ii.pressure = empty_pressure


main()
