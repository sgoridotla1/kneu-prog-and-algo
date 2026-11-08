"""Варіант 64. Завдання 1. Відбір на шляху від кореня"""
from records import RECORD_TYPES, RecordN
from utils import format_ids


class Node:
    def __init__(self, node_id: int, record: RecordN, parent: "Node | None"):
        self.id = node_id
        self.record = record
        self.parent = parent
        self.children: list[Node] = []

class Tree:
    def __init__(self):
        self.nodes: dict[int, Node] = {}
        self.root: Node | None = None

    def add(self, node_id: int, parent_id: int, record: RecordN):
        parent = self.nodes.get(parent_id)
        node = Node(node_id, record, parent)
        self.nodes[node_id] = node
        if parent is None:
            self.root = node
        else:
            parent.children.append(node)

    def traverse(self) -> list[Node]:
        result: list[Node] = []
        if self.root is not None:
            self.visit(self.root, result)
        return result

    def visit(self, node: Node, result: list[Node]):
        result.append(node)
        for child in node.children:
            self.visit(child, result)

    def path_to(self, node_id: int) -> list[Node]:
        path: list[Node] = []
        node = self.nodes.get(node_id)
        while node is not None:
            # print("up", node.id)
            path.append(node)
            node = node.parent
        path.reverse()
        return path

def read_tree() -> Tree:
    tree = Tree()
    n = int(input())
    for _ in range(n):
        node_id, parent_id, kind, value = input().split()
        tree.add(int(node_id), int(parent_id), RECORD_TYPES[kind](int(value)))
    return tree

def main():
    tree = read_tree()
    r, t = map(int, input().split())

    path = tree.path_to(r)
    selected = [node for node in path if node.record.score() <= t]
    # print([(node.id, node.record.score()) for node in path])

    print(f"Обхід: {format_ids([node.id for node in tree.traverse()])}")
    print(f"Шлях: {format_ids([node.id for node in path])}")
    print(f"Відібрано: {format_ids([node.id for node in selected])}")
    print(f"Кількість: {len(selected)}")
    print(f"Сума: {sum(node.record.score() for node in selected)}")


if __name__ == "__main__":
    main()
