# Global variable
message = "my name is priya"
def inner_function():
# Local variable
    message = "what is your name"
    print(message)
inner_function()
print(message)