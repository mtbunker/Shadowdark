import random


class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


class Dice(object):
    def __init__(self, sides=6, number=1):
        self.sides = sides
        self.number = number

    def roll(self):
        return random.randint(self.number, self.sides)


class Map:
    def __init__(self, cells=None):
        if cells is None:
            cells = {000: {}}
        self.cells = cells
        self.columns = 0
        self.rows = 0

    def cell_details(self):
        previous_hex = ''
        starting_cell = select_random_cell(all_cells)
        print("Start point of map generation: ", starting_cell)
        counter = total_cells
        while counter > 0:
            if counter == total_cells:
                new_hex = starting_cell
            else:
                new_hex = random_hex(previous_hex)
            new_terrain, cataclysm_check = hex_terrain()
            if new_terrain == '':
                new_terrain = prev_terrain
                new_cataclysm = cataclysm_type()
            else:
                new_cataclysm = ''
            danger = danger_level(cataclysm_check)
            d = Dice(6, 1)
            poi_check = d.roll()
            if poi_check == 1:
                poi = poi_type()
            else:
                poi = ''
            self.cells[new_hex] = {'Terrain': new_terrain, 'Cataclysm': new_cataclysm, 'Danger Level': danger, 'POI': poi}
            previous_hex = new_hex
            counter -= 1


    def find_all_cells(self):
        for x in range(self.columns):
            for y in range(self.rows):
                x_coord = x * 100
                y_coord = y+1
                cell = x_coord + y_coord
                self.cells[cell] = {}
        # print(self.cells)

    def x_axis(self):
        self.columns = column_input

    def y_axis(self):
        self.rows = row_input


def border_check(previous_hex):
    # Create a list of directions the hex walker cannot traverse to due to reaching border of map.
    limits = []
    if previous_hex - 100 < 0:
        limits.append(5)
        limits.append(6)
    elif previous_hex + 100 > max(my_map.cells.keys()):


    return limits

def cataclysm_type():
    cataclysm = ''
    d = Dice(8, 1)
    cataclysm_roll = d.roll()
    if cataclysm_roll == 1:
        cataclysm = 'Volcano'
    elif cataclysm_roll == 2:
        cataclysm = 'Fire'
    elif cataclysm_roll == 3:
        cataclysm = 'Earthquake'
    elif cataclysm_roll == 4:
        cataclysm = 'Storm'
    elif cataclysm_roll == 5:
        cataclysm = 'Flood'
    elif cataclysm_roll == 6:
        cataclysm = 'War'
    elif cataclysm_roll == 7:
        cataclysm = 'Pestilence'
    elif cataclysm_roll == 8:
        cataclysm = 'Magical Disaster'
    return cataclysm


def danger_level(cataclysm):
    danger = ''
    d = Dice(6, 1)
    danger_roll = d.roll()
    while danger_roll == 1 and cataclysm == 'Yes':
        danger_roll = d.roll()
    if danger_roll == 1:
        danger = 'Safe'
    elif danger_roll in (2, 3):
        danger = 'Unsafe'
    elif danger_roll in (4, 5):
        danger = 'Risky'
    elif danger_roll == 6:
        danger = 'Deadly'
    return danger


def hex_terrain():
    terrain = ''
    cataclysm = ''
    d = Dice(6, 2)
    terrain_roll = d.roll()
    if terrain_roll == 2:
        terrain = 'Desert/arctic'
    elif terrain_roll in (3, 4):
        terrain = 'Swamp'
    elif terrain_roll in (5, 6):
        terrain = 'Grassland'
    elif terrain_roll in (7, 8):
        terrain = 'Forest/jungle'
    elif terrain_roll in (9, 10):
        terrain = 'River/coast'
    elif terrain_roll == 11:
        terrain = 'Mountain'
    elif terrain_roll == 12:
        terrain = ''
        cataclysm = 'Yes'
    else:
        cataclysm = 'No'
    return terrain, cataclysm


def poi_type():
    poi = ''
    d = Dice(20, 1)
    poi_roll = d.roll()
    if poi_roll == 1:
        poi = 'Small tower'
    elif poi_roll == 2:
        poi = 'Fortified keep'
    elif poi_roll == 3:
        poi = 'Natural landmark'
    elif poi_roll == 4:
        poi = 'Temple'
    elif poi_roll == 5:
        poi = 'Barrow mounds'
    elif poi_roll in (6, 7, 8):
        poi = 'Village'
    elif poi_roll in (9, 10, 11):
        poi = 'Town'
    elif poi_roll in (12, 13):
        poi = 'City'
    elif poi_roll == 14:
        poi = 'Metropolis'
    elif poi_roll == 15:
        poi = 'Monster nest'
    elif poi_roll == 16:
        poi = 'Hermit\'s abode'
    elif poi_roll == 17:
        poi = 'Cave formation'
    elif poi_roll == 18:
        poi = 'Ancient dolmens'
    elif poi_roll == 19:
        poi = 'Barbarian camp'
    elif poi_roll == 20:
        poi = 'Holy shrine'
    return poi


def random_hex(previous_hex):
    d = Dice(6, 1)
    hex_roll = d.roll()
    if hex_roll == 1:
        next_hex = previous_hex - 1

    return


def select_random_cell(c):
    random_cell = random.choice(c)
    return random_cell


if __name__ == '__main__':

    my_map = Map()
    try:
        column_input = int(input("How wide is your map? (Max.=20)"))
        row_input = int(input("How tall is your map? (Max.=20)"))
    except:
        print("Invalid dimension entered!")
    else:
        if column_input <= 20:
            my_map.x_axis()
        if row_input <= 20:
            my_map.y_axis()
    finally:
        my_map.find_all_cells()

    all_cells = list(my_map.cells.keys())
    total_cells = len(list(my_map.cells.keys()))
#    starting_cell = select_random_cell(all_cells)
#    print("Start point of map generation: ", starting_cell)

    my_map.cell_details()

    print(my_map.cells)
