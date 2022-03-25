import life
x = life.dead_state(8,8)
d = {0:[3,4],1:[2,5],2:[1,6],3:[0,7],4:[0,7],5:[1,6],6:[2,5],7:[3,4]}

for key in d.keys():
    for value in d[key]:
        x[key][value] = 1

life.render(life.next_board_state(x))