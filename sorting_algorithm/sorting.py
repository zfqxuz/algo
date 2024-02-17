import inspect
import random
import abc


class Sorter(abc.ABC):
    def __init__(self):
        self.data = [random.randrange(0, 100) for i in range(20)]

    examples = {}

    @abc.abstractmethod
    def sort(self):
        pass

    @abc.abstractmethod
    def suggested(self):
        pass

    def run(self):
        print(inspect.getsource(self.suggested))
        print(self.data)
        self.sort()
        print(self.data)


    def example(self, name=''):
        method_name = self.examples.get(name)
        if method_name == None:
            print(f"no example found for name {name}")
            print(f"candidates:{self.examples.keys()}")
        else:
            sample = getattr(self, method_name, None)
            sample()


    @classmethod
    def sample_usage(cls, chinese_name):
        # 装饰器工厂，接收一个中文名作为参数
        def decorator(func):
            # 将函数名和中文名映射关系存储在类属性中
            cls.examples[chinese_name] = func.__name__
            def wrapper(*args, **kwargs):
                print(inspect.getsource(func))
                return func(*args, **kwargs)
            return wrapper
        return decorator