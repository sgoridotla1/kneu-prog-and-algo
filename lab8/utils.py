from collections import deque


class RequestQueue:
    def __init__(self, requests):
        self.items = deque(requests)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.popleft()

    def snapshot(self):
        return list(self.items)


def linear_search(records, s):
    for rec in records:
        if rec.id == s:
            return rec
    return None

def binary_search(records, s):
    l = 0
    r = len(records) - 1
    while l <= r:
        mid = (l + r) // 2
        # print("mid", mid, records[mid].id)
        if records[mid].id == s:
            return records[mid]
        elif records[mid].id < s:
            l = mid + 1
        else:
            r = mid - 1
    return None

def sort_records(records, key):
    res = list(records)
    for i in range(1, len(res)):
        cur = res[i]
        j = i - 1
        while j >= 0 and key(res[j]) > key(cur):
            res[j + 1] = res[j]
            j = j - 1
        res[j + 1] = cur
    return res
