# -*- coding: utf-8 -*-

#O(1)时间取得栈内最小元素
#方法：
# 除了原有的数据栈，再创建一个辅助栈，
# 每次入栈时，若入栈元素比辅助栈的栈顶元素小,则新元素在数据栈和辅助栈都入栈，否则只入数据栈，辅助栈复制栈顶元素入栈
# 每次出栈时，两个栈一起出栈
class Stack(object):
    def __init__(self):
        self.data_stack = []
        self.min_stack = []
    def push(self,value):
        self.data_stack.append(value)
        if len(self.min_stack) == 0:
            self.min_stack.append(value)
        else:
            min = self.min_stack[-1]
            if value < min:
                self.min_stack.append(value)
            else:
                self.min_stack.append(min)

    def pop(self):
        top = self.data_stack.pop()
        _ = self.min_stack.pop()
        return top

    def top(self):

        if len(self.data_stack) > 0:
            return self.data_stack[-1]
        else:
            return None

    def min(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None
def test_stack():
    stack = Stack()
    stack.push(5)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(6)
    print stack.min()
    print stack.data_stack
    print stack.min_stack
    stack.pop()
    stack.pop()

    print stack.min()

if __name__ == '__main__':
    pass

