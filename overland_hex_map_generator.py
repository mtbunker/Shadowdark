# Unresolved Issues
# 1 - Starting cell == 0, or anytime the current hex == 0
# 2 - Test randomness; tend to get no cataclysms

import json
import random


def dice(sides, number):
    rolls = 0
    for i in range(number):
        die_roll = random.randint(1, sides)
        rolls += die_roll
    return rolls


class Map:
    def __init__(self, cells=None):
        if cells is None:
            cells = {000: {}}
        self.cells = cells
        self.columns = 0
        self.rows = 0

    def cell_details(self):
        former_x = None
        former_y = None
        prev_terrain = None
        starting_cell = 0
        while starting_cell == 0:
            starting_cell, x, y = select_random_cell(all_cells)
        print("Start point of map generation: ", starting_cell)
        counter = total_cells
        while counter > 0:
            if counter == total_cells:
                new_hex = starting_cell
                transition = None
            else:
                transition = terrain_transition()
                new_hex, x, y = random_hex(former_x, former_y)
            new_terrain, cataclysm_check = hex_terrain(transition, prev_terrain)
            if new_terrain == '':
                new_terrain = prev_terrain
                new_cataclysm = cataclysm_type()
            else:
                new_cataclysm = ''
            danger = danger_level(cataclysm_check)
            poi_check = dice(4, 1)  # Altered to 25% probability of finding POI
            # poi_check = d.roll()
            if poi_check == 1:
                poi = poi_type()
            else:
                poi = ''
            # noinspection PyTypeChecker
            self.cells[new_hex]['Terrain'] = new_terrain
            self.cells[new_hex]['Cataclysm'] = new_cataclysm
            self.cells[new_hex]['Danger Level'] = danger
            self.cells[new_hex]['POI'] = poi
            previous_hex = new_hex
            former_x = x
            former_y = y
            prev_terrain = self.cells[previous_hex]['Terrain']
            counter -= 1
            print(my_map.cells[previous_hex])

    def find_all_cells(self):
        for x in range(self.columns):
            for y in range(self.rows):
                x_coord = x * 100
                y_coord = y+1
                cell = x_coord + y_coord
                # noinspection PyTypeChecker
                self.cells[cell] = {"x_coord": x_coord, "y_coord": y_coord}
        # print(self.cells)

    def x_axis(self):
        self.columns = column_input

    def y_axis(self):
        self.rows = row_input


def cataclysm_type():
    cataclysm = ''
    cataclysm_roll = dice(8, 1)
    # cataclysm_roll = d.roll()
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


def compass(hex_roll):
    direction = ''
    if hex_roll == 1:
        direction = 'North'
    elif hex_roll == 2:
        direction = 'Northeast'
    elif hex_roll == 3:
        direction = 'Southeast'
    elif hex_roll == 4:
        direction = 'South'
    elif hex_roll == 5:
        direction = 'Southwest'
    elif hex_roll == 6:
        direction = 'Northwest'
    print(direction)
    return


def danger_level(cataclysm):
    danger = ''
    danger_roll = dice(6, 1)
    # danger_roll = d.roll()
    while danger_roll == 1 and cataclysm == 'Yes':
        danger_roll = dice(6, 1)
    if danger_roll == 1:
        danger = 'Safe'
    elif danger_roll in (2, 3):
        danger = 'Unsafe'
    elif danger_roll in (4, 5):
        danger = 'Risky'
    elif danger_roll == 6:
        danger = 'Deadly'
    return danger


def hex_terrain(transition=None, prev_terrain=None):
    terrain = ''
    cataclysm = ''
    roll = dice(6, 2)
    # roll = d.roll()
    # Value of roll is shifted up or down based on transition roll
    if transition is None:
        terrain_roll = roll
    elif prev_terrain is not None:
        terrain_roll = terrain_roll_shift(roll, transition, prev_terrain)
    else:
        terrain_roll = terrain_roll_shift(roll, transition, None)
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
    terrain_list.append(terrain_roll)
    return terrain, cataclysm


def key_exists(dictionary, keys):
    nested_dict = dictionary
    for key in keys:
        try:
            nested_dict = nested_dict[key]
        except KeyError:
            return False
    return True


def poi_type():
    poi = ''
    poi_roll = dice(20, 1)
    # poi_roll = d.roll()
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
    elif poi_roll == 6:
        poi = 'Worker\'s Camp'
    elif poi_roll in (7, 8, 9):
        poi = 'Village'
    elif poi_roll in (10, 11):  # Larger settlements
        settlement_roll = dice(10, 1)
        if settlement_roll in (1, 2, 3, 4):
            poi = 'Town'
        elif settlement_roll in (5, 6, 7):
            poi = 'City'
        elif settlement_roll in (8, 9):
            poi = 'Metropolis'
        elif settlement_roll == 10:
            poi = 'Capital City'
    elif poi_roll == 12:
        poi = 'Ruin'
    elif poi_roll == 13:
        poi = 'Noble\'s Lodge'
    elif poi_roll == 14:
        poi = 'Arcane Nexus'
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


def random_hex(former_x, former_y):
    check = 0
    # d = Dice(6, 1)
    while check < 1:
        hex_roll = dice(6, 1)
        evens_check = (former_x / 100) % 2
        if evens_check == 0:
            if hex_roll == 1:
                new_x = former_x
                new_y = former_y - 1
            elif hex_roll == 2:
                new_x = former_x + 100
                new_y = former_y
            elif hex_roll == 3:
                new_x = former_x + 100
                new_y = former_y + 1
            elif hex_roll == 4:
                new_x = former_x
                new_y = former_y + 1
            elif hex_roll == 5:
                new_x = former_x - 100
                new_y = former_y + 1
            elif hex_roll == 6:
                new_x = former_x - 100
                new_y = former_y
        else:
            if hex_roll == 1:
                new_x = former_x
                new_y = former_y - 1
            elif hex_roll == 2:
                new_x = former_x + 100
                new_y = former_y - 1
            elif hex_roll == 3:
                new_x = former_x + 100
                new_y = former_y
            elif hex_roll == 4:
                new_x = former_x
                new_y = former_y + 1
            elif hex_roll == 5:
                new_x = former_x - 100
                new_y = former_y
            elif hex_roll == 6:
                new_x = former_x - 100
                new_y = former_y - 1
        new_hex = new_x + new_y
        # Confirm hex cell included in defined map, otherwise re-roll
        if new_hex in my_map.cells.keys():
            # Accept the move to the new hex cell if it hasn't been defined
            if not key_exists(my_map.cells, [new_hex, 'Terrain']):
                check = 1
            # Otherwise reset cell position and re-roll
            else:
                former_x = new_x
                former_y = new_y
    # compass(hex_roll)
    return new_hex, new_x, new_y


def select_random_cell(cell_list):
    random_cell = random.choice(cell_list)
    x_coord = my_map.cells.get(random_cell).get("x_coord")
    y_coord = my_map.cells.get(random_cell).get("y_coord")
    return random_cell, x_coord, y_coord


def terrain_roll_shift(roll, shift, prev_terrain=None):
    if shift is None:
        pass
    elif shift == 'Step Down':
        if roll == 2:
            roll = 12
        elif roll == 3:
            roll = 2
        elif roll in (4, 5, 6, 7, 8, 9, 10, 11):
            roll = roll - 2
        elif roll == 12:
            roll = 11
    elif shift == 'Step Up':
        if roll in (2, 3, 4, 5, 6, 7, 8, 9):
            roll = roll + 2
        elif roll in (10, 11):
            roll = roll + 1
        elif roll == 12:
            roll = 2
    elif shift == 'Same':
        if prev_terrain == 'Desert/arctic':
            roll = 2
        elif prev_terrain == 'Swamp':
            roll = 3
        elif prev_terrain == 'Grassland':
            roll = 5
        elif prev_terrain == 'Forest/jungle':
            roll = 7
        elif prev_terrain == 'River/coast':
            roll = 9
        elif prev_terrain == 'Mountain':
            roll = 11
    return roll


def terrain_transition():
    shift = None
    roll = dice(6, 2)
    # roll = d.roll()
    if roll in (2, 3):
        shift = 'Step Down'
    elif roll in (4, 5, 6, 7, 8, 9):
        shift = 'Same'
    elif roll in (10, 11):
        shift = 'Step Up'
    elif roll == 12:
        shift = None
    return shift


if __name__ == '__main__':

    my_map = Map()
    terrain_list = []
    try:
        column_input = int(input("How wide is your map? (Max.=20)"))
        row_input = int(input("How tall is your map? (Max.=20)"))
        file_name = input("Provide a file name: ")
        file_name = file_name+".json"
    except AssertionError as error:
        print("Invalid dimension entered!")
        print(error)
    else:
        if column_input <= 100:
            my_map.x_axis()
        if row_input <= 100:
            my_map.y_axis()
    finally:
        my_map.find_all_cells()
        print(my_map.cells)

    all_cells = list(my_map.cells.keys())
    total_cells = len(list(my_map.cells.keys()))
    print(all_cells)
#    starting_cell = select_random_cell(all_cells)
#    print("Start point of map generation: ", starting_cell)

    my_map.cell_details()

    # print(my_map.cells)
    print(terrain_list)
    json.dump(my_map.cells, open(file_name, "w"))
