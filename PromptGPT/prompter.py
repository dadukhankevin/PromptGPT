import string
class Node:
    def __init__(self, word, children):
        self.word = word
        self.children = children
    def add_node(self):
        pass
class Prompt:
    def __init__(self):
        self.a = "a"


    def keyword(self, words):
        def my_decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return result

            return wrapper

        return my_decorator

        return wrapper