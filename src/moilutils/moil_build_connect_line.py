from Moildev import Moildev
import numpy as np
import cv2


class GetOrgLineFromAnypoint:

    def __init__(self):
        pass

    @classmethod
    def get_mid_of_2point(cls, coord_a, coord_b):
        mid_x = round((coord_a[0] + coord_b[0]) / 2)
        mid_y = round((coord_a[1] + coord_b[1]) / 2)

        return mid_x, mid_y

    @classmethod
    def get_anypoint_img_coord(cls, org_x, org_y, map_x, map_y):
        coord_list = []

        img_h = len(list(map_x))  # 800 of Intel
        img_w = len(list(map_x)[0])  # 848 of Intel

        for any_y in range(img_h):
            for any_x in range(img_w):

                if org_x + 5 > int(map_x[any_y][any_x]) > org_x - 5 and \
                        org_y + 5 > int(map_y[any_y][any_x]) > org_y - 5:
                    coord_list.append((any_x, any_y))

        any_x, any_y = cls.average_coord(coord_list)

        return any_x, any_y

    @classmethod
    def get_any_connect_line(cls, any_coord_a, any_coord_b):

        if any_coord_a[0] == any_coord_b[0]:
            any_line_list = cls.get_any_connect_line_by_vertical_line(any_coord_a, any_coord_b)

        else:
            coefficient_a, coefficient_b = cls.get_coefficient(any_coord_a, any_coord_b)

            diff_x = abs(any_coord_a[0] - any_coord_b[0])
            diff_y = abs(any_coord_a[1] - any_coord_b[1])

            if diff_x >= diff_y:
                any_line_list = cls.get_any_connect_line_by_x(any_coord_a, any_coord_b, coefficient_a, coefficient_b)

            else:
                any_line_list = cls.get_any_connect_line_by_y(any_coord_a, any_coord_b, coefficient_a, coefficient_b)

        return any_line_list

    @classmethod
    def convert_line_any2org(cls, any_line_list, map_x, map_y):
        org_line_list = []
        for coord in any_line_list:
            any_x = int(map_x[coord[1]][coord[0]])
            any_y = int(map_y[coord[1]][coord[0]])

            org_line_list.append((any_x, any_y))

        print('\norg_line_list', org_line_list)

        return org_line_list

    @classmethod
    def get_org_connect_line(cls, org_coord_a, org_coord_b, map_x, map_y):
        any_coord_a = cls.get_anypoint_img_coord(org_coord_a[0], org_coord_a[1], map_x, map_y)
        any_coord_b = cls.get_anypoint_img_coord(org_coord_b[0], org_coord_b[1], map_x, map_y)

        print('any_coord_a_b', any_coord_a, any_coord_b)

        any_connect_line = cls.get_any_connect_line(any_coord_a, any_coord_b)
        org_connect_line = cls.convert_line_any2org(any_connect_line, map_x, map_y)

        return org_connect_line

    @classmethod
    def average_coord(cls, coord_list):

        sum_x = 0
        sum_y = 0
        for coord in coord_list:
            sum_x += coord[0]
            sum_y += coord[1]

        coord_x = round(sum_x / len(coord_list))
        coord_y = round(sum_y / len(coord_list))

        return coord_x, coord_y

    @classmethod
    def get_coefficient(cls, point_a, point_b):

        k = np.array([[point_a[0], 1], [point_b[0], 1]])
        l = np.array([point_a[1], point_b[1]])

        ans = np.linalg.solve(k, l)

        coefficient_a = ans[0]
        coefficient_b = ans[1]

        '''
        y = ax+b
        Y = coefficient_a * X + coefficient_b
        '''

        return coefficient_a, coefficient_b

    @classmethod
    def get_any_connect_line_by_x(cls, point_a, point_b, coefficient_a, coefficient_b):
        print('\n[get_any_connect_line_by_x]')
        any_line_list = []
        print('point_a[x]', point_a[0])
        print('point_b[x]', point_b[0] + 1)

        order = 1 if point_a[0] < point_b[0] + 1 else -1
        for x in range(point_a[0], (point_b[0] + 1), order):
            # y = Ax+b
            y = coefficient_a * x + coefficient_b
            any_line_list.append((x, round(y)))

        print('any_line_list', any_line_list)
        return any_line_list

    @classmethod
    def get_any_connect_line_by_y(cls, point_a, point_b, coefficient_a, coefficient_b):
        print('\n[get_any_connect_line_by_y]')
        any_line_list = []
        print('point_a[y]', point_a[1])
        print('point_b[y]', point_b[1] + 1)

        order = 1 if point_a[1] < point_b[1] + 1 else -1
        for y in range(point_a[1], (point_b[1] + 1), order):
            # y = Ax+b
            x = (y - coefficient_b) / coefficient_a

            any_line_list.append((round(x), y))

        print('any_line_list', any_line_list)
        return any_line_list

    @classmethod
    def get_any_connect_line_by_vertical_line(cls, point_a, point_b):
        print('\n[get_any_connect_line_by_vertical_line]')
        any_line_list = []
        print('point_a[y]', point_a[1])
        print('point_b[y]', point_b[1] + 1)

        # x = point_a[0] bcz vertical line
        x = point_a[0]
        print('x=', x)
        order = 1 if point_a[1] < point_b[1] + 1 else -1
        for y in range(point_a[1], (point_b[1] + 1), order):
            any_line_list.append((x, y))

        print('any_line_list', any_line_list)
        return any_line_list
