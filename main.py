import turtle, pandas

data = pandas.read_csv("50_states.csv")

print("1", type(data))
state_list = data["state"].to_list()
print("2",type(state_list))
print(state_list)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tmap = turtle.Turtle()
tmap.hideturtle()
tmap.penup()

### Main Game Loop
done = False
count = 0
answer_state = screen.textinput(title="Guess the States", prompt="What's another State's name?")

while(not done):
    if answer_state.title() == "Exit":
        new_data = pandas.DataFrame(state_list)
        new_data.to_csv("the_leftover_states.csv")
        break

    if answer_state.title() in state_list:
        count += 1
        print(count)
        row = data[data.state == str(answer_state).title()]
        print(data.state == str(answer_state).title())
        print(row)
        print(int(row.x), int(row.y))
        tmap.setpos(int(row.x), int(row.y))
        tmap.write(str(answer_state).title())
        state_list.pop(state_list.index(str(answer_state).title()))
        print(state_list)
        if len(state_list) == 0:
            done = True
            continue
    else:
        print("%s is wrong!" %(str(answer_state)))

    answer_state = screen.textinput(title="Score: "+str(count)+"/50", prompt="What's another State's name?")

# def get_mouse_click_coor(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


print("Done.  Congrats!!!")
# screen.exitonclick()
turtle.mainloop()
