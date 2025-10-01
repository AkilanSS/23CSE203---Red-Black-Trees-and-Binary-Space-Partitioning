class Node:
    def __init__(self,line):
        self.div=line
        self.front=None
        self.back=None
        self.lines=[line]

class BSP:
    def __init__(self):
        self.root=None

    def build(self,lines):
        
        if node is None:
            return
        
        div=lines[0]
        node=Node[div]
        front_list,back_list=[],[]

        for i in lines[1:]:
            position=classify_line(div,i)

            if position=="front":
                front_list.append(i)
            elif position=="back":
                back_list.append(i)
            elif position=="spanning":
                l1,l2=split_line(i,div)

                if l1 is not None:
                    front_list.append(l1)
                if l2 is not None:
                    back_list.append(l2)
            else: #lies exactly on the divider
                node.lines.append(i)

        node.front=self.build(front_list)
        node.back=self.builf(back_list)

        return node


    def traverse(self,node,pos,result):

        view=classify_point(pos,node.div)

        if view=="front":
            self.traverse(node.back,pos,result)
            result.extend(node.lines)
            self.traverse(node.front,pos,result)

        elif view=="back":
            self.traverse(node.front,pos,result)
            result.extend(node.lines)
            self.traverse(node.back,pos,result)

        else:
            self.traverse(node.front,pos,result)
            self.traverse(node.back,pos,result)
            


