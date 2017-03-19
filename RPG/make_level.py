from my_gui.PyGame.RPG.scene_item import BottomPlatform


def create_bottom(group):
    x = 0
    y = 850
    for i in range(0, 28):
        platform = BottomPlatform(x, y)
        group.add(platform)
        x += 50
