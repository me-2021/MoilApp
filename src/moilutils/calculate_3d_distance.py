import math

from sympy import Symbol, Eq, solve


class Calculate3dDistance:

    @classmethod
    def get_beta_cartesian(cls, beta):
        if beta < 0:
            beta += 360

        if beta > 360:
            beta %= 360

        if beta <= 90:
            return 90 - beta

        else:
            return 360 - (beta - 90)

    @classmethod
    def get_vector_x(cls, alpha, beta):
        beta = cls.get_beta_cartesian(beta)
        return math.sin(math.radians(alpha)) * math.cos(math.radians(beta))

    @classmethod
    def get_vector_y(cls, alpha, beta):
        beta = cls.get_beta_cartesian(beta)
        return math.sin(math.radians(alpha)) * math.sin(math.radians(beta))

    @classmethod
    def get_vector_z(cls, alpha):
        return math.cos(math.radians(alpha))

    @classmethod
    def get_vector(cls, alpha, beta):
        vector_x = cls.get_vector_x(alpha, beta)
        vector_y = cls.get_vector_y(alpha, beta)
        vector_z = cls.get_vector_z(alpha)

        return vector_x, vector_y, vector_z

    @classmethod
    def get_vector_coord2coord(cls, coord1, coord2):
        pass

    @classmethod
    def get_unknown_point_and_symbol(cls, list_vector, list_camera_coord, symbol_name):

        vector_x = list_vector[0]
        vector_y = list_vector[1]
        vector_z = list_vector[2]

        coord_x = list_camera_coord[0]
        coord_y = list_camera_coord[1]
        coord_z = list_camera_coord[2]

        symbol = Symbol(symbol_name)
        left_image_target_point = [vector_x * symbol + coord_x,
                                   vector_y * symbol + coord_y,
                                   vector_z * symbol + coord_z]

        return left_image_target_point, symbol

    @classmethod
    def get_right_image_target_point_and_n(cls, list_right_vector, list_right_camera_right):

        right_vector_x = list_right_vector[0]
        right_vector_y = list_right_vector[1]
        right_vector_z = list_right_vector[2]

        right_coord_x = list_right_camera_right[0]
        right_coord_y = list_right_camera_right[1]
        right_coord_z = list_right_camera_right[2]

        n = Symbol('n')
        right_image_target_point = [right_vector_x * n + right_coord_x,
                                    right_vector_y * n + right_coord_y,
                                    right_vector_z * n + right_coord_z]

        return right_image_target_point, n

    @classmethod
    def solve_m_n(cls, left_vector, right_vector, point_p, point_q, m, n):

        vector_pq_x = point_q[0] - point_p[0]
        vector_pq_y = point_q[1] - point_p[1]
        vector_pq_z = point_q[2] - point_p[2]

        left_vector_x = left_vector[0]
        left_vector_y = left_vector[1]
        left_vector_z = left_vector[2]

        right_vector_x = right_vector[0]
        right_vector_y = right_vector[1]
        right_vector_z = right_vector[2]

        eq1 = Eq((vector_pq_x * left_vector_x + vector_pq_y * left_vector_y + vector_pq_z * left_vector_z), 0)
        eq2 = Eq((vector_pq_x * right_vector_x + vector_pq_y * right_vector_y + vector_pq_z * right_vector_z), 0)
        ans_s_t = solve((eq1, eq2), (m, n))

        m = ans_s_t[m]
        n = ans_s_t[n]

        return n, m

    @classmethod
    def calculate_point(cls, left_vector, right_vector, left_camera_coord, right_camera_coord, n, m):
        point_p = [left_vector[0] * n + left_camera_coord[0],
                   left_vector[1] * n + left_camera_coord[1],
                   left_vector[2] * n + left_camera_coord[2]]

        point_q = [right_vector[0] * m + right_camera_coord[0],
                   right_vector[1] * m + right_camera_coord[1],
                   right_vector[2] * m + right_camera_coord[2]]

        return point_p, point_q

    @classmethod
    def get_mid_point_of_p_q(cls, point_p, point_q):
        mid_point = [(point_p[0] + point_q[0]) / 2,
                     (point_p[1] + point_q[1]) / 2,
                     (point_p[2] + point_q[2]) / 2]

        return mid_point

    @classmethod
    def get_3d_coord_mid_point_of_two_line(cls, left_alpha, left_beta, right_alpha, right_beta,
                                           left_camera_coord, right_camera_coord):

        left_vector_x, left_vector_y, left_vector_z = cls.get_vector(left_alpha, left_beta)
        print('left_x_y_z', left_vector_x, left_vector_y, left_vector_z)

        right_vector_x, right_vector_y, right_vector_z = cls.get_vector(right_alpha, right_beta)
        print('right_x_y_z', right_vector_x, right_vector_y, right_vector_z)

        left_vector = [left_vector_x, left_vector_y, left_vector_z]
        right_vector = [right_vector_x, right_vector_y, right_vector_z]

        point_p, m = cls.get_unknown_point_and_symbol(left_vector, left_camera_coord, 'm')
        point_q, n = cls.get_unknown_point_and_symbol(right_vector, right_camera_coord, 'n')

        m, n = cls.solve_m_n(left_vector, right_vector, point_p, point_q, m, n)

        point_p, point_q = cls.calculate_point(left_vector, right_vector,
                                               left_camera_coord, right_camera_coord,
                                               m, n)

        mid_point = cls.get_mid_point_of_p_q(point_p, point_q)

        print('mid_point', mid_point)

        return mid_point
