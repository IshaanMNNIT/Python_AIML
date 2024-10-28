def main() :
    name = input("Enter the name : ").strip().title()
    hello()
    hello(name)
def hello(to = "World") :
    print("Hello , ",to)

main()
