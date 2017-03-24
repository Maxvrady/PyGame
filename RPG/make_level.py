from my_gui.PyGame.RPG.scene_item import HellCenter, HellLeft, HellRight, Tree


level = [
    "                            ",
    "                            ",
    "               <------------",
    "                            ",
    "                            ",
    "    <----->                 ",
    "                            ",
    "                            ",
    "  <>        <>              ",
    "                            ",
    "             !              ",
    "     <----------------->    ",
    "                            ",
    "                            ",
    " <------>                   ",
    "                            ",
    "                            ",
    "----------------------------"
]


def create_level(all_group, block_group):
    x = 0
    y = 0
    for row in level:
        for num in row:
            if num == '-':
                hell_center = HellCenter(x, y)
                all_group.add(hell_center)
                block_group.add(hell_center)
            if num == '<':
                hell_left = HellLeft(x, y)
                all_group.add(hell_left)
                block_group.add(hell_left)
            if num == '>':
                hell_right = HellRight(x, y)
                all_group.add(hell_right)
                block_group.add(hell_right)
            # if num == "!":
            #     tree = Tree(x, y)
            #     all_group.add(tree)
            x += 50
        y += 50
        x = 0
        print(len(level))
        print(len(level[0]))