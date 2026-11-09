"""Варіант 64. Завдання 2. Рахунки підрозділів: допустимість операцій і зміни стану"""
from utils import RequestQueue, binary_search, linear_search, sort_records

R = 6
C = 43
P = 17


class Record:
    kind = ""

    def __init__(self, id, a, b):
        self.id = id
        self.a = a
        self.b = b

    def value(self):
        return self.b * P

    def pay_sum(self, x):
        return x

    def apply(self, op, x):
        if x <= 0:
            return "AMOUNT"
        if op == "CREDIT":
            if self.a + x > C:
                return "SPACE"
            self.a += x
        elif op == "PAY":
            total = self.pay_sum(x)
            if self.a < total:
                return "RESOURCE"
            self.a -= total
            self.b += total
        elif op == "REFUND":
            if self.b < x:
                return "RESOURCE"
            if self.a + x > C:
                return "SPACE"
            self.b -= x
            self.a += x
        return "OK"

class RecordA(Record):
    kind = "A"

class RecordB(Record):
    kind = "B"

    def pay_sum(self, x):
        return x + R


class System:
    def __init__(self, records, requests):
        self.records = list(records)
        self.queue = RequestQueue(requests)
        self.processed = []

    def snapshot(self):
        return [(r.id, r.kind, r.a, r.b, r.value()) for r in self.records]

    def execute_next(self):
        req = self.queue.pop()
        if req is None:
            return None
        j, op, id, x = req
        rec = linear_search(self.records, id)
        if rec is None:
            res = (j, "MISSING", None)
        else:
            status = rec.apply(op, x)
            if status == "OK":
                res = (j, "OK", (rec.a, rec.b))
            else:
                res = (j, status, None)
        self.processed.append(res)
        return res

    def result(self, s, g, T):
        lines = []
        ok = 0
        for j, status, state in self.processed:
            if state != None:
                ok += 1
                lines.append(f"OP {j} OK {state[0]} {state[1]}")
            else:
                lines.append(f"OP {j} {status}")
        lines.append(f"PROCESSED {ok} {len(self.processed) - ok}")

        wait = self.queue.snapshot()
        lines.append("PENDING " + str(len(wait)))
        for w in wait:
            lines.append(f"WAIT {w[0]} {w[1]} {w[2]} {w[3]}")

        found = binary_search(sort_records(self.records, lambda r: r.id), s)
        if found is None:
            lines.append("FOUND NONE")
        else:
            lines.append(f"FOUND {found.id} {found.kind} {found.a} {found.b} {found.value()}")

        sel = []
        for r in self.records:
            if (g == "ALL" or r.kind == g) and r.value() >= T:
                sel.append(r)
        sel = sort_records(sel, lambda r: (-r.value(), r.id))
        lines.append(f"SELECT {len(sel)}")
        for r in sel:
            lines.append(f"ITEM {r.id} {r.kind} {r.a} {r.b} {r.value()}")

        sum_a = 0
        sum_b = 0
        sum_v = 0
        for r in self.records:
            sum_a += r.a
            sum_b += r.b
            sum_v += r.value()
        lines.append(f"TOTAL {sum_a} {sum_b} {sum_v}")
        return lines


def validate_record(id, kind, a, b):
    if kind not in ["A", "B"]:
        return False
    if id < 1 or id > 999:
        return False
    return 0 <= a <= C and 0 <= b <= 10000

def validate_request(op, id, x):
    return op in ["CREDIT", "PAY", "REFUND"] and 1 <= id <= 999 and -100 <= x <= 100

def read_input():
    records = []
    n = int(input())
    for _ in range(n):
        id, kind, a, b = input().split()
        id, a, b = int(id), int(a), int(b)
        if validate_record(id, kind, a, b):
            if kind == "A":
                records.append(RecordA(id, a, b))
            else:
                records.append(RecordB(id, a, b))

    requests = []
    m = int(input())
    for j in range(m):
        op, id, x = input().split()
        if validate_request(op, int(id), int(x)):
            requests.append((j + 1, op, int(id), int(x)))

    k = int(input())
    line = input().split()
    return records, requests, k, int(line[0]), line[1], int(line[2])

def main():
    records, requests, k, s, g, T = read_input()
    system = System(records, requests)
    for _ in range(k):
        system.execute_next()
    print("\n".join(system.result(s, g, T)))


if __name__ == "__main__":
    main()
