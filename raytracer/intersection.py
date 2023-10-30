class Intersection:

    def __init__(self, t: int, object):
        self.t = t
        self.object = object

    @staticmethod
    def intersections(*args):
        return list(args)

    @staticmethod
    def hit(intersections):
        nonneg_intersections = [i for i in intersections if i.t >= 0]
        if not nonneg_intersections:
            return None
        return min(nonneg_intersections, key=lambda i: i.t)
