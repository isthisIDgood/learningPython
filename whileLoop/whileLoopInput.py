##forever prompt until quit

prompt = "To exit this program, enter 'quit'\n"
prompt += 'Please enter your name: '

message = ""
while message != 'quit':
    message = input(prompt)
    print (message.title())