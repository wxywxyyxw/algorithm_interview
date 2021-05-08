class treenode(object):
    def __init__(self,name="", id=0, evaluation_id=0, origin_score=0.0, score=0.0, proportion=0.0):
        self.name = name
        self.origin_score = origin_score
        self.score = score
        self.id = id
        self.evaluation_id = evaluation_id
        self.children = []
        self.proportion = proportion
        self.parent = None
    def __repr__(self):
        return "{} {}".format(self.name,self.id)



root = treenode(name='root',origin_score=100)
child1 = treenode(name='child1',proportion=0.4)
child2 = treenode(name='child2',proportion=0.6)
root.children = [child1,child2]
child1.parent = root
child2.parent = root


child3 = treenode(name='child3',proportion=0.2)
child4 = treenode(name='child4',proportion=0.8)
child1.children = [child3,child4]
child3.parent = child1
child4.parent = child1

child5 = treenode(name='child5',proportion=0.4,id=100)
child6 = treenode(name='child6',proportion=0.6,id=101)
child2.children = [child5,child6]

child5.parent = child2
child6.parent = child2


child7 = treenode(name='child7',proportion=0.5,id=103)
child8 = treenode(name='child8',proportion=0.5,id=104)
child3.children = [child7,child8]
child7.parent = child3
child8.parent = child3

child9 = treenode(name='child9',proportion=0.5,id=105)
child10 = treenode(name='child10',proportion=0.5,id=106)
child4.children = [child9,child10]
child9.parent = child4
child10.parent = child4

score_dict = {
    100:0.5,
    101:1.0,
    103:1.0,
    104:1.0,
    105:1.0,
    106:1.0
}

queue = [root]
cal_queue = [root]
while queue:
    item = queue.pop(0)
    print (item.name, item.origin_score)
    origin_score = item.origin_score
    for child in item.children:
        child.origin_score = origin_score * child.proportion
        #print (child.name, child.origin_score)

    queue.extend(item.children)
    cal_queue.extend(item.children)

print (cal_queue)

cal_queue = cal_queue[::-1]

temp_sum = 0
for index, item in enumerate(cal_queue):



    if item.id != 0:
        proportion = score_dict.get(item.id,0)
        item.score = item.origin_score * proportion
        #print ("--", item.name, item.id, item.origin_score,proportion, item.score )

    temp_sum += item.score

    has_sum = False
    if index != len(cal_queue) -1:
        if cal_queue[index + 1].parent != item.parent:

            item.parent.score =  temp_sum
            temp_sum = 0
            has_sum = True

    print (item.name,item.score, temp_sum, has_sum,item.parent.score if item.parent else "")



print ('---------------------')

# queue = [root]
# while queue:
#     item = queue.pop(0)
#     print (item.name, item.score)
#     origin_score = item.origin_score
#
#     queue.extend(item.children)






