"""Варіант 64. Завдання 1. Розподіл записів за оцінкою"""
from structures import Queue, Record, Section, Stack
from utils import format_ids, read_commands

CAPACITY = 5
THRESHOLD = 12

class RecordA(Record):
    def score(self) -> int:
        return 2 * self.value

class RecordB(Record):
    def score(self) -> int:
        return 4 * self.value + 3

RECORD_TYPES = {"A": RecordA, "B": RecordB}

class EquipmentDesk:
    def __init__(self):
        self.sections = {"S": Section(Stack(CAPACITY)), "Q": Section(Queue(CAPACITY))}
        self.next_id = 1

    def add(self, kind: str, value: int):
        record = RECORD_TYPES[kind](self.next_id, value)
        self.next_id += 1
        target = "S" if record.score() <= THRESHOLD else "Q"
        self.sections[target].add(record)

    def take(self, name: str, attempts: int):
        self.sections[name].take(attempts)

    def execute(self, command: list[str]):
        match command:
            case ["ADD", kind, value]:
                self.add(kind, int(value))
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
            f"Прийнято S: {s.accepted}",
            f"Прийнято Q: {q.accepted}",
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
