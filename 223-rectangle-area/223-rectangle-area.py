def check_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if ax2 > bx1 and bx2 > ax1 and ay2 > by1 and by2 > ay1:
        return True
    return False

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        basic_area = (ax2-ax1) * (ay2-ay1) + (bx2-bx1) * (by2-by1)
        if check_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
            return basic_area - (min(ay2, by2) - max(ay1, by1)) * (min(ax2, bx2) - max(ax1, bx1))
        else:
            return basic_area