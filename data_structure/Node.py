import inspect


class BaseNodeMeta(type):
    def __new__(cls, name, bases, attrs):
        def create_init(enabled_attrs):
            def __init__(self, weight=0):
                for attr in enabled_attrs:
                    if attr in ['left', 'right', 'parent', 'left_sibling', 'right_sibling']:  # 特殊处理left和right属性
                        setattr(self, attr, None)  # 初始化为子类实例
                    elif attr in ['color']:
                        setattr(self, attr, 'w')
                    elif attr in ['children', 'adjacent']:
                        setattr(self, attr, [])
                    else:
                        setattr(self, attr, weight)

            return __init__

        def uninherited_exception(*args, **kwargs):
            raise NotImplementedError("Method not registered")

        inherit_attrs = attrs.get('node_attr', attrs.get('__slots__', []))
        inherit_methods = attrs.get("node_methods", [k for k in attrs if not k.startswith("__")])
        if attrs.get('node_attr')==None:
            attrs['node_attr']=attrs.get('__slots__')
        new_class = super().__new__(cls, name, bases, attrs)
        for base_class in bases:
            for name,func in inspect.getmembers(base_class,predicate=inspect.isfunction):
                if name in inherit_methods:
                    setattr(new_class, name,func)
                else:
                    setattr(new_class,name,uninherited_exception)
        setattr(new_class, '__init__', create_init(inherit_attrs))
        return new_class


class CommonNode(metaclass=BaseNodeMeta):
    __slots__ = ['weight', 'left', 'right', 'parent', 'left_sibling', 'right_sibling', 'color', 'children', 'adjacent']
    def add_left(self, weight):
        left_node=type(self)(weight)
        self.left = left_node
        if 'parent' in left_node.node_attr:
            left_node.parent=self

    def add_right(self, weight):
        right_node = type(self)(weight)
        self.right = right_node
        if 'parent' in right_node.node_attr:
            right_node.parent = self

    def change_color(self,color):
        if 'color' in self.node_attr:
            self.color=color

    def get_parent(self):
        return self.parent.weight


class BinaryTreeNode(CommonNode):
    node_attr = ['weight', 'left', 'right','parent']
    node_methods = ['add_left', 'add_right','get_parent']



if __name__ == '__main__':
    a = BinaryTreeNode(1)
    a.add_right(2)
    a.add_left(0)
    a.right.change_color('r')
    print(a.right.color)
