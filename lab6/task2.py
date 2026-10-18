"""Варіант 64. Завдання 2. Незалежні сховища з обмеженою місткістю"""
from structures import Queue, Record, Section, Stack
from utils import format_ids, read_commands

CAPACITY = 3

class RecordA(Record):
    def score(self) -> int:
        return 3 * self.value

class RecordB(Record):
    def score(self) -> int:
        return 2 * self.value + 4

RECORD_TYPES = {"A": RecordA, "B": RecordB}

class EquipmentDesk:
    def __init__(self):
        self.sections = {"S": Section(Stack(CAPACITY)), "Q": Section(Queue(CAPACITY))}
        self.next_id = 1

    def add(self, name: str, kind: str, value: int):
        record = RECORD_TYPES[kind](self.next_id, value)
        self.next_id += 1
        self.sections[name].add(record)

    def take(self, name: str, attempts: int):
        self.sections[name].take(attempts)

    def execute(self, command: list[str]):
        match command:
            case ["ADD", name, kind, value]:
                self.add(name, kind, int(value))
            case ["TAKE", name, attempts]:
                self.take(name, int(attempts))

    def report(self) -> list[str]:
        s, q = self.sections["S"], self.sections["Q"]
        return [
            f"S: {format_ids([record.id for record in s.storage.state()])}",
            f"Q: {format_ids([record.id for record in q.storage.state()])}",
            f"Сума S: {s.storage.total_score()}",
            f"Сума Q: {q.storage.total_score()}",
            f"Вилучено S: {format_ids(s.taken)}",
            f"Вилучено Q: {format_ids(q.taken)}",
            f"Порожньо S: {s.empty}",
            f"Порожньо Q: {q.empty}",
            f"Відхилено S: {s.rejected}",
            f"Відхилено Q: {q.rejected}",
        ]

def main():
    desk = EquipmentDesk()
    for command in read_commands():
        desk.execute(command)
    print("\n".join(desk.report()))


if __name__ == "__main__":
    main()
