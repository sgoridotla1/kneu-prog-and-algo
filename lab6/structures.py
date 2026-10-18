from collections import deque


class Record:
    def __init__(self, record_id: int, value: int):
        self.id = record_id
        self.value = value

    def score(self) -> int:
        raise NotImplementedError


class Storage:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._items: deque[Record] = deque()

    def push(self, record: Record) -> bool:
        if self.is_full():
            return False
        self._items.append(record)
        return True

    def pop(self) -> Record | None:
        raise NotImplementedError

    def peek(self) -> Record | None:
        raise NotImplementedError

    def state(self) -> list[Record]:
        raise NotImplementedError

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return self.size() == 0

    def is_full(self) -> bool:
        return self.size() >= self.capacity

    def total_score(self) -> int:
        return sum(record.score() for record in self._items)


class Stack(Storage):
    def pop(self) -> Record | None:
        return None if self.is_empty() else self._items.pop()

    def peek(self) -> Record | None:
        return None if self.is_empty() else self._items[-1]

    def state(self) -> list[Record]:
        return list(reversed(self._items))


class Queue(Storage):
    def pop(self) -> Record | None:
        return None if self.is_empty() else self._items.popleft()

    def peek(self) -> Record | None:
        return None if self.is_empty() else self._items[0]

    def state(self) -> list[Record]:
        return list(self._items)


class Section:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.taken: list[int] = []
        self.accepted = 0
        self.rejected = 0
        self.empty = 0

    def add(self, record: Record):
        if self.storage.push(record):
            self.accepted += 1
        else:
            self.rejected += 1

    def take(self, attempts: int):
        for _ in range(attempts):
            record = self.storage.pop()
            if record is None:
                self.empty += 1
            else:
                self.taken.append(record.id)
