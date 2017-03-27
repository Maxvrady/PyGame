from my_gui.PyGame.RPG.scene_item import HellCenter, HellLeft, HellRight, TreeOne, Bottom, TreeTwo, Table


level = [
    "                            ",
    "                            ",
    "               <------------",
    "                            ",
    "     !                      ",
    "    <----->                 ",
    "                            ",
    "                            ",
    "  <>        <>              ",
    "                            ",
    "                    !       ",
    "     <----------------->    ",
    "                            ",
    "  #                         ",
    " <------>                   ",
    "                            ",
    "             *              ",
    "_________________",
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
            if num == "!":
                tree = TreeOne(x, y - 50)
                all_group.add(tree)
            if num == "*":
                treeTwo = TreeTwo(x, y)
                all_group.add(treeTwo)
            if num == "_":
                bottom = Bottom(x, y)
                block_group.add(bottom)
                all_group.add(bottom)
                x += 36
            if num == "#":
                table = Table(x, y)
                all_group.add(table)
            x += 50
        y += 50
        x = 0
