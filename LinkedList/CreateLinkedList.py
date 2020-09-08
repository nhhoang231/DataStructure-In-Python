class Node:
  def _init_(self, dataval = None):
    self.dataval = dataval #Đây là dữ liệu mà ta sẽ lưu trữ trong mỗi node
    self.nextval = None    #Đây là con trỏ trỏ đến node tiếp theo trong linked list

class SlinkedList:
  def _init_(self):
    self.headval = None

list1 = SLinkedList()
list1.headval.nextval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first node to second node
list1.headval.nextval = e2
# Link second node to third node
e2.n 
