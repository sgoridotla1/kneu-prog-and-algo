"""Варіант 64. Завдання 1. Облік подарункових наборів: залишки та черга операцій"""
from utils import RequestQueue, binary_search, linear_search, sort_records

R = 6
C = 43


class Record:
    kind = ""

    def __init__(self, id, a, b):
        self.id = id
        self.a = a
        self.b = b

    def value(self):
        return self.a * self.b

    def apply(self, op, x):
        if x <= 0:
            return "AMOUNT"
        if op == "TAKE":
            if self.b < x:
                return "STOCK"
            self.b = self.b - x
            return "OK"
        if op == "PUT":
            if self.b + x > C:
                return "SPACE"
            self.b = self.b + x
            return "OK"

class RecordA(Record):
    kind = "A"

class RecordB(Record):
    kind = "B"

    def value(self):
        v = self.a * self.b - R
        if v < 0:
            v = 0
        return v


class System:
    def __init__(self, records, requests):
        self.records = list(records)
        self.queue = RequestQueue(requests)
        self.processed = []

    def snapshot(self):
        snap = []
        for r in self.records:
            snap.append((r.id, r.kind, r.a, r.b, r.value()))
        return snap

    def execute_next(self):
        req = self.queue.pop()
        if req == None:
            return None
        j, op, id, x = req
        rec = linear_search(self.records, id)
        if rec == None:
            res = (j, "MISSING", None)
        else:
            status = rec.apply(op, x)
            if status == "OK":
                res = (j, status, (rec.b,))
            else:
                res = (j, status, None)
        self.processed.append(res)
        return res

    def result(self, s, g, T):
        lines = []
        ok = 0
        bad = 0
        for j, status, state in self.processed:
            if status == "OK":
                ok += 1
                lines.append("OP " + str(j) + " OK " + str(state[0]))
            else:
                bad += 1
                lines.append("OP " + str(j) + " " + status)
        lines.append(f"PROCESSED {ok} {bad}")

        wait = self.queue.snapshot()
        lines.append(f"PENDING {len(wait)}")
        for j, op, id, x in wait:
            lines.append(f"WAIT {j} {op} {id} {x}")

        sorted_by_id = sort_records(self.records, lambda r: r.id)
        found = binary_search(sorted_by_id, s)
        if found == None:
            lines.append("FOUND NONE")
        else:
            lines.append(f"FOUND {found.id} {found.kind} {found.a} {found.b} {found.value()}")

        sel = []
        for r in self.records:
            if r.b > 0 and r.value() >= T and (g == "ALL" or g == r.kind):
                sel.append(r)
        sel = sort_records(sel, lambda r: (-r.value(), r.id))
        lines.append(f"SELECT {len(sel)}")
        for r in sel:
            lines.append(f"ITEM {r.id} {r.kind} {r.a} {r.b} {r.value()}")

        Q = 0
        V = 0
        for r in self.records:
            Q += r.b
            V += r.value()
        lines.append(f"TOTAL {Q} {V}")
        return lines


def validate_record(id, kind, a, b):
    if kind != "A" and kind != "B":
        return False
    return 1 <= id <= 999 and 1 <= a <= 10000 and 0 <= b <= C

def validate_request(op, id, x):
    if op != "TAKE" and op != "PUT":
        return False
    return 1 <= id <= 999 and -100 <= x <= 100

def read_input():
    n = int(input())
    records = []
    for i in range(n):
        parts = input().split()
        id = int(parts[0])
        kind = parts[1]
        p = int(parts[2])
        q = int(parts[3])
        if validate_record(id, kind, p, q):
            if kind == "A":
                records.append(RecordA(id, p, q))
            else:
                records.append(RecordB(id, p, q))

    m = int(input())
    requests = []
    for j in range(1, m + 1):
        op, id, x = input().split()
        if validate_request(op, int(id), int(x)):
            requests.append((j, op, int(id), int(x)))

    k = int(input())
    s, g, T = input().split()
    return records, requests, k, int(s), g, int(T)

def main():
    records, requests, k, s, g, T = read_input()
    system = System(records, requests)
    for i in range(k):
        system.execute_next()
    # print(system.snapshot())
    for line in system.result(s, g, T):
        print(line)


if __name__ == "__main__":
    main()
