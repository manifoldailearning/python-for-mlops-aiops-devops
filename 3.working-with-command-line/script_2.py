
import sys 

def greeting(greet,target):
    message = f"{greet} {target}"
    print(message)


if __name__ == "__main__":
    greet = "Hello"
    target = "Jack"
    
    if "--name" in sys.argv:
        name_index = sys.argv.index("--name") + 1
        print(f"name index is {name_index} ")

        if name_index < len(sys.argv):
            target = sys.argv[name_index]
    
    if "--greet" in sys.argv:
        greet_index = sys.argv.index("--greet") + 1
        print(f"greet index is {greet_index} ")

        if greet_index < len(sys.argv):
            greet = sys.argv[greet_index]
    
    greeting(greet,target)