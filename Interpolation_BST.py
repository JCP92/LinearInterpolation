
# coding: utf-8

# In[15]:


import time
import math
import sys
import numpy as np


timer = []
timerBST = []
class BSTNode: #https://codereview.stackexchange.com/questions/175856/python-binary-search-tree
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = self.right = None

class BSTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def pre_order_traversal(self):
        def pre_order(node):
            if node is None: return
            yield node.value
            yield from pre_order(node.left)
            yield from pre_order(node.right)
        yield from pre_order(self._root)

    def in_order_traversal(self):
        def in_order(node):
            if node is None: return
            yield from in_order(node.left)
            yield node.value
            yield from in_order(node.right)
        yield from in_order(self._root)

    def post_order_traversal(self):
        def post_order(node):
            if node is None: return
            yield from post_order(node.left)
            yield from post_order(node.right)
            yield node.value
        yield from post_order(self._root)

    @property
    def size(self):
        return self._size

    def containsV(self, value):
        def _contains(node, value):
            return (
                False if node is None else
                _contains(node.left, value) if value < node.value else
                _contains(node.right, value) if value > node.value else
                True
            )
        return _contains(self._root, value)
    def containsK(self, key):
        def _contains(node, key):
            return (
                False if node is None else
                _contains(node.left, key) if key > node.key else
                _contains(node.right, key) if key < node.key else
                True
            )
        return _contains(self._root, key)

    def insert(self, key, value):
        def _insert(node, key, value):
            if node is None:
                return BSTNode(key, value)
            elif value == node.value:
                return None
            elif value < node.value:
                node.left = _insert(node.left, key, value)
            elif value > node.value:
                node.right = _insert(node.right, key, value)
            return node
        self._root = _insert(self._root, key, value)
        if self._root:
            self._size += 1
        return self._root is not None

    def remove(self, value):
        def _remove(node, value):
            if node.value == value:
                if not (node.left and node.right):
                    return node.left or node.right, True
                else:
                    # Replace the node with its next larger successor
                    successor, parent = node.right, node
                    while successor.left:
                        successor, parent = successor.left, successor

                    successor.left = node.left
                    if parent != node:
                        parent.left = successor.right
                        successor.right = node.right
                    return successor, True
            elif value < node.value and node.left:
                node.left, removed = _remove(node.left, value)
                return node, removed
            elif value > node.value and node.right:
                node.right, removed = _remove(node.right, value)
                return node, removed
            return node, False
        if self._root is None:
            return False
        self._root, removed = _remove(self._root, value)
        self._size -= int(removed)
        return removed

def IPSearch(tarray, v1, size, value):
    if value <= 2:
        v = v1
    else:
        v = tarray
        tarray = v1
    low = 0
    high = size - 1
    count = 0
    t = time.time()
    while (v[high] >= value) & (v[low] < value):
        count += 1
        slope = (high - low)/(v[high] - v[low])
        x = value - v[low]
        index = math.floor(slope * x + low)
        if value < v[index]:
            high = index - 1
        elif value > v[index]:
            low = index + 1
        elif value == v[index]:
            low = index
            break

    if v[low] == value:
        timer.append(time.time() - t)
        print(str(value) +" True: " + "Other Value: " + str(tarray[low]) + " found")
    else:
        print(str(value) + " False")
        timer.append(time.time()-t)
    


def main():
    breakup=[]
    key = []
    vals = []
    check = [30, 1.992015979, 31, 1.98406383, 35, 1.976143426, 
        59, 1.96825464, 792, 1.824210299, 798, 1.816928032, 818, 1.809674836, 822, 1.802450595, 99273, 0.000718135, 99303,0.000715268, 99307, 0.000712413, 99311, 0.000709569, 99391, 0.000706736, 99392, 0.000703915, 99411, 0.000701105, 99491, 0.000698306, 99525, 0.000695519, 99908, 0.000676314, 99955,0.000673614, 3, 4, 5, 6, 7, 8]
    m = BSTree()
    with open('values.txt','r') as f:
        for line in f:
            for word in line.split():
                breakup.append(word)
            n = breakup.pop(0)
            #print(breakup[0] + " " + breakup[1])
            m.insert(int(breakup[0]), float(breakup[1]))
            key.append(breakup.pop(0))
            vals.append(breakup.pop(0))
    for i in range(len(key)):
        key[i] = int(key[i])
        vals[i] = float(vals[i])
    #key.reverse()
    vals.reverse()
    for i in range(len(check)):
        IPSearch(key, vals, len(key), check[i])
        if i%2 == 0:
            t2 = time.time()
            print(m.containsK(check[i]))
            timerBST.append(time.time()-t2)
        else:
            t2 = time.time()
            print(m.containsV(check[i]))
            timerBST.append(time.time()-t2)
    l = np.sum(timer)
    o = np.sum(timerBST)
    print("Interpolation:\n\tTotal Time: ")
    print(l)
    print("\tAverage Time: ") 
    print(l/len(timer))    
    print("BST:\n\tTotal Time: ")
    print(o)
    print("\tAverage Time: ") 
    print(o/len(timer))

    
   # print(key)
   # print(vals)

main()

