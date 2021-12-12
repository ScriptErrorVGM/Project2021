from functools import wraps

def main():
    def makeBold(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return "<b>" + fn(*args, **kwargs) + "</b>"
        return wrapper

    def makeItalic(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return "<i>" + fn(*args, **kwargs) + "</i>"
        return wrapper

    def makeUnderline(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return "<u>" + fn(*args, **kwargs) + "</u>"
        return wrapper

    @makeBold
    @makeItalic
    @makeUnderline
    def hello():
        return "hello world"

    @makeBold
    @makeItalic
    @makeUnderline
    def log(s):
        return s

    print(hello())        # returns "<b><i>hello world</i></b>"
    print(hello.__name__) # with functools.wraps() this returns "hello"
    print(log('hello'))   # returns "<b><i>hello</i></b>"

if __name__ == "__main__":
    main()