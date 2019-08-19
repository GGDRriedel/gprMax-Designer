from math import floor

from point import TPoint

class TGeometry(object):
    """
    Class contains static methods used for coordinates calculations (window and model system)
    and other geometry related procedures.
    """

    @staticmethod
    def window_to_model(window_pt, min_model, max_model, min_window, max_window, dx, dy):
        """
        Calculate model coordinates from a given windows coordinates.

        :param window_pt: point in window coordinates system (pixels).
        :param type: TPoint.
        :param min_model: visible model area lower left point in m.
        :param type: TPoint.
        :param max_model: vivible model area upper right point in m.
        :param type: TPoint
        :param min_window: model box lower left point in pixels.
        :param type: TPoint.
        :param max_window: model box upper right point in pixels.
        :param type: TPoint.
        :param dx: grid discretisation step in x direction.
        :param type: float.
        :param dx: grid discretisation step in y direction.
        :param type: float.
        
        :rtype: TPoint.
        """
        mod_pt = TPoint()
        mod_pt.x = TGeometry.round_to_multiple((max_model.x - min_model.x)*(window_pt.x - min_window.x)/(max_window.x - min_window.x) + min_model.x, dx)
        mod_pt.y = TGeometry.round_to_multiple((max_model.y - min_model.y)*(window_pt.y - min_window.y)/(max_window.y - min_window.y) + min_model.y, dy)
        return mod_pt

    @staticmethod
    def model_to_window(mod_pt, min_model, max_model, min_window, max_window):
        """
        Calculate window coordinates from s given model coordinates.

        :param mod_pt: point in model coordinate system (m).
        :param type: TPoint.
        :param min_model: visible model area lower left point in m.
        :param type: TPoint.
        :param max_model: vivible model area upper right point in m.
        :param type: TPoint.
        :param min_window: model box lower left point in pixels.
        :param type: TPoint.
        :param max_window: model box upper right point in pixels.
        :param type: TPoint.
        
        :rtype: TPoint.
        """
        window_pt = TPoint()
        window_pt.x = round(((mod_pt.x - min_model.x)*(max_window.x - min_window.x))/(max_model.x - min_model.x) + min_window.x)
        window_pt.y = round(((mod_pt.y - min_model.y)*(max_window.y - min_window.y))/(max_model.y - min_model.y) + min_window.y)
        # window_pt.x = TGeometry.round_to_multiple(((mod_pt.x - min_model.x)*(max_window.x - min_window.x))/(max_model.x - min_model.x) + min_window.x, 1)
        # window_pt.y = TGeometry.round_to_multiple(((mod_pt.y - min_model.y)*(max_window.y - min_window.y))/(max_model.y - min_model.y) + min_window.y, 1)
        return window_pt

    @staticmethod
    def dist_window_to_model(mod_dist, min_model, max_model, min_window, max_window, dx, dy):
        """
        Calculate distance in model coordinate system from a given distance in window coordinate system.

        :param mod_dist: distance in model coordinate system (m).
        :param type: TPoint.
        :param min_model: visible model area lower left point in m.
        :param type: TPoint.
        :param max_model: vivible model area upper right point in m.
        :param type: TPoint.
        :param min_window: model box lower left point in pixels.
        :param type: TPoint.
        :param max_window: model box upper right point in pixels.
        :param type: TPoint.
        :param dx: model discretization in x direction.
        :param type: float.
        :param dy: model discretization in y direction.
        :param type: float.

        :rtype: float.
        """
        return TGeometry.round_to_multiple(mod_dist*(max_model.x - min_model.x)/(max_window.x - min_window.x), min(dx, dy))

    @staticmethod
    def dist_model_to_window(win_dist, min_model, max_model, min_window, max_window):
        """
        Calculate distance in windows coordinate system from a given distance in model coordinate system.

        :param win_dist: distance in window coordinate system (pixels).
        :param type: TPoint.
        :param min_model: visible model area lower left point in m.
        :param type: TPoint.
        :param max_model: vivible model area upper right point in m.
        :param type: TPoint.
        :param min_window: model box lower left point in pixels.
        :param type: TPoint.
        :param max_window: model box upper right point in pixels.
        :param type: TPoint.

        :rtype: float.
        """
        return win_dist*(max_window.x - min_window.x)/(max_model.x - min_model.x)

    @staticmethod
    def round_to_multiple(x, m):
        """
        Round given float to nearest multiple of another real.
        
        :param x: number to be rounded.
        :param type: float.
        :param m: number to multiple of which x is to be rounded to.
        :param type: float.

        :rtype: float.
        """
        m_reverse = m**(-1)
        return floor (x*m_reverse + 0.5)/m_reverse # Python has issues with float multiplying

    @staticmethod
    def position_in_boundries(pos, box_min, box_max):
        """
        Detect if a given mouse position lies within model.

        :param pos: point coordinates in pixels.
        :param type: TPoint.
        :param box_min: lower left model box point.
        :param type: TPoint.
        :param box_max: upper right model box point.
        :param type: TPoint.

        :rtype: boolean.
        """
        if(pos.x >= min(box_min.x, box_max.x) and pos.x <= max(box_min.x, box_max.x) and \
           pos.y >= min(box_min.y, box_max.y) and pos.y <= max(box_min.y, box_max.y)):
            return True
        return False

    @staticmethod
    def point_visible(point, min_model, max_model):
        """
        Detect if a given point is within visible area of model.

        :param point: point coordinates in m.
        :param type: TPoint.
        :param min_model: lower left visible model area point.
        :param type: TPoint.
        :param max_model: upper right visible model area point.
        :param type: TPoint.

        :rtype: boolean.
        """
        if((point.x >= min_model.x and point.y >= min_model.y) and \
           (point.x <= max_model.x and point.y <= max_model.y)):
            return True
        else:
            return False

    @staticmethod
    def intersect(point1, point2, point3, point4):
        """
        Detect if two line segments intersect.

        :param point1: first line segment start.
        :param type: TPoint.
        :param point2: first line segment end.
        :param type: TPoint.
        :param point3: second line segment start.
        :param type: TPoint.
        :param point4: second line segment end.
        :param type: TPoint.

        :rtype: boolean.
        """
        def sign(a):
            if(a >= 0):
                return 1
            else:
                return -1
        det1 = point1.x*point2.y + point1.y*point3.x + point2.x*point3.y - \
               point3.x*point2.y - point1.x*point3.y - point2.x*point1.y
        det2 = point1.x*point2.y + point1.y*point4.x + point2.x*point4.y - \
               point4.x*point2.y - point1.x*point4.y - point2.x*point1.y
        if(sign(det1) != sign(det2)):
            return True
        else:
            return False
    
    @staticmethod
    def polygon_area(points):
        """
        Calculate the area of polygon enclosed by points in given list.

        :param points: list of consecutive polygons points.
        :param type: list of TPoint.

        :rtype: float.
        """
        sum = 0.0
        for i, pt in enumerate(points):
            if(i == 0):
                sum += pt.x*(points[1].y - points[-1].y)
            elif(i + 1 == len(points)):
                sum += pt.x*(points[0].y - points[-2].y)
            else:
                sum += pt.x*(points[i+1].y - points[i-1].y)
        return abs(sum/2)