def comb(input_list, n, tmp=[]):
    if len(tmp) == n:
        yield tmp
    else:
        for i in range(len(input_list)):
            yield from comb(input_list[i+1:], n, tmp+[input_list[i]])

def get_ab(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:
        a = 'inf'
    elif y1 == y2:
        a = 0
    else:
        a = (y2 - y1) / (x2 - x1)
    if a == 'inf':
        b = x1
    else:
        b = y1 - a * x1
        
    return a, b

class Solution:
    def maxPoints(self, points) -> int:
        if len(points) == 1:
            return 1
        dct = {}
        maximum = 0
        
        for point1, point2 in comb(points, 2):
            a, b = get_ab(point1, point2)
            key = '{},{}'.format(a, b)
            
            if key in dct:
                dct[key].update(['{},{}'.format(point1[0], point1[1]),
                    '{},{}'.format(point2[0], point2[1])])
            else:
                dct[key] = set(['{},{}'.format(point1[0], point1[1]),
                    '{},{}'.format(point2[0], point2[1])])

            if len(dct[key]) > maximum:
                maximum = len(dct[key])
            
        return maximum