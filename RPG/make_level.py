from my_gui.PyGame.RPG.scene_item import BottomPlatform


def create_bottom(all_group, block_group):
    x = 0
    y = 850
    for i in range(0, 28):
        platform = BottomPlatform(x, y)
        all_group.add(platform)
        block_group.add(platform)
        x += 50
