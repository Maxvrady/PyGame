from my_gui.PyGame.RPG.scene_item import BottomPlatform, UpPlatform


def create_bottom(all_group, block_group):
    x = 0
    y = 850
    for i in range(0, 28):
        platform = BottomPlatform(x, y)
        all_group.add(platform)
        block_group.add(platform)
        x += 50


def create_up_platform(all_group, block_group):
    x = 100
    y = 700
    for n in range(14):
        platform = UpPlatform(x, y)
        all_group.add(platform)
        block_group.add(platform)
        x += 86
