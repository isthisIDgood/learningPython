##Using a flag to stop a program
##One variable can control the whole progran

prompt = "Enter a 'q' to exit this program."
prompt += '\nWhat is your name? ' 

active = True
while active:
    message = input(prompt)
    if message == 'q':
        active = False
    else:
        print ('Hello, ' + message)

