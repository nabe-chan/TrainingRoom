#
# 数値を保存するためのLinkedList
#
class LinkedList:

    first_node = None

    # デフォルトは空リストで作成
    def __init__(self):
        pass

    # 最後尾にノードを追加
    def add(self, next_value):
        if first_node is None:
            first_node
        next_node = self.first_node
        count = 0
        while next_node is not None:
            print("1:", next_node.getValue)

    # 昇順ソート
    def sort(self):
        pass

    # 配列のサイズを返却
    def size(self):
        next_node = self.first_node
        count = 0
        while next_node is not None:
            count += 1
            next_node = next_node.getNextNode()

    def display(self):
        next_node = self.first_node
        count = 0
        while next_node is not None:
            print("1:", next_node.getValue)


#
# LinkedListを構成する各値を保存するためのノード
#
class LinkedListNode:
    value = None
    next_node = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getNextNode(self):
        return self.next_node

    def setNextNode(self, next_node):
        self.next_node = next_node


linkedlist = LinkedList()

linkedlist.add(50)
linkedlist.add(30)
linkedlist.add(20)
linkedlist.add(10)

