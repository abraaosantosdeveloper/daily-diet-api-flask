def sayHi(userName: str):
    print(f"\n Hi there, {userName}!")

print(f"What is your name?")
name = input(f">>> ")
sayHi(name)