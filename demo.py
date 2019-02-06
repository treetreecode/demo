def say_hello():
    print('hello')


def print_README():
    with open('README.md','r',encoding='utf8') as f:
        data = f.read()
        print(data)

if __name__ == "__main__":
    print_README()