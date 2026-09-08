import ast
import math
from pathlib import Path
from types import SimpleNamespace
import unittest

# ROS 런타임 없이 입력 해석·판정 함수만 검사한다.
source = Path(__file__).parents[1] / 'wall_follow_lab' / 'wall_follow.py'
tree = ast.parse(source.read_text())
functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)
             and n.name in ('sector', 'decide')]
scope = {'math': math}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(source), 'exec'), scope)
decide = scope['decide']


def scan(front=2.0, right=0.45, diagonal=0.6364, start=0.0):
    ranges = []
    for i in range(360):
        deg = math.degrees(math.atan2(math.sin(start + i * math.pi / 180),
                                    math.cos(start + i * math.pi / 180)))
        if abs(deg) <= 26:
            value = front
        elif abs(deg + 90) <= 4:
            value = right
        elif abs(deg + 45) <= 4:
            value = diagonal
        else:
            value = 2.0
        ranges.append(value)
    return SimpleNamespace(ranges=ranges, angle_min=start,
                           angle_increment=math.pi / 180,
                           range_min=0.12, range_max=3.5)


class ControllerTests(unittest.TestCase):
    def test_parallel_wall(self):
        v, w, state = decide(scan())
        self.assertEqual(state, 'FOLLOW')
        self.assertGreater(v, 0)
        self.assertLess(abs(w), 0.01)

    def test_front_turn(self):
        self.assertEqual(decide(scan(front=0.4)), (0.0, 0.5, 'TURN_LEFT'))

    def test_near_stop(self):
        self.assertEqual(decide(scan(right=0.18)), (0.0, 0.0, 'TOO_CLOSE'))

    def test_lost_wall(self):
        self.assertEqual(decide(scan(right=math.inf))[2], 'FIND_RIGHT_WALL')

    def test_invalid(self):
        for value in (math.nan, 0.0, -math.inf):
            self.assertEqual(decide(scan(front=value))[2], 'INVALID_SCAN')

    def test_angle_origin(self):
        self.assertEqual(decide(scan())[2], decide(scan(start=-math.pi))[2])

    def test_steering(self):
        self.assertGreater(decide(scan(right=0.3, diagonal=0.3 * math.sqrt(2)))[1], 0)
        self.assertLess(decide(scan(right=0.7, diagonal=0.7 * math.sqrt(2)))[1], 0)


if __name__ == '__main__':
    unittest.main()
