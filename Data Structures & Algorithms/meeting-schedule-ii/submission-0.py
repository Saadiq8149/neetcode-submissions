"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for i in intervals:
            events.append((i.start, 1))
            events.append((i.end, -1))

        # events.sort(key=lambda x:(x[]))
        events.sort()
        print(events)

        running = 0
        res = 0

        for e in events:
            running += e[1]
            res = max(res, running)

        return res
