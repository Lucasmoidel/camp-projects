from tkinter import Tk, simpledialog, messagebox
def read_from_file():
    file = open('capital_data.txt')
    for line in file:
        line = line.rstrip('\n')
        state, city = line.split('/')
        the_world[state] = city
def write_to_file(state_name, city_name):
    file = open('capital_data.txt', 'a')
    file.write('\n' + state_name + '/' + city_name) # + '\n')
window = Tk()
window.withdraw()
the_world = {}
read_from_file()
print("Ask the state expert")
print("these are the states i know:")
for state in the_world:
    print(state + ", " + the_world[state])
while True:
    state = simpledialog.askstring("state", "Type the name of the state:")
    if state is None:
        exit()
    elif state in the_world:
        capital = the_world[state]
        first = 'the capital of '
        messagebox.showinfo("Answer", first + state + ' is ' + capital + "!")
    else:
        question = "I don\'t know! what is the capital city of "
        new_city = simpledialog.askstring("Teach me", question + state + "?")
        the_world[state] = new_city
        print(state + ", " + new_city)
        write_to_file(state, new_city)
window.mainloop()