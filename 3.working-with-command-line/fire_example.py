import fire

def greet(greeting='Hey', name='Jacob'):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    fire.Fire(greet)