class RecordN:
    def __init__(self, value: int):
        self.value = value

    def score(self) -> int:
        return self.value


class RecordD(RecordN):
    def score(self) -> int:
        return 2 * self.value


RECORD_TYPES = { "N": RecordN, "D": RecordD }
