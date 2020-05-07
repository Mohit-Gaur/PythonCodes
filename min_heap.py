lass MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count
  
  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
    
    min = self.heap_list[1]
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    self.heapify_down()
    return min

  def add(self, element):
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()


  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        return self.left_child_idx(idx)
      else:
        return self.right_child_idx(idx)
