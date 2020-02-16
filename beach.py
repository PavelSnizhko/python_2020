from graph import *

WIDTH_PICTURE = 500
HEIGHT_PICTIRE = 500


def draw_sky(x, y, width_sky, hight_sky):
    """ hight_sky + hight_sea + hight_beach = size of window"""
    brushColor(0, 204, 204)
    rectangle(x, y, x + width_sky, y + hight_sky)
    draw_sun(x + 400, y + 70, 30)
    draw_cloud(80, 50, 10)
    return x + width_sky, y + hight_sky


def draw_cloud(x, y, radius):
    brushColor(255, 255, 255)
    for i in range(8):
        if i < 3:
            circle(x, y, radius)
            x += 8
        elif i >= 4:
            circle(x, y, radius)
            x += 10
        else:
            y += 10
            x -= 30


def draw_sun(x, y, radius):
    brushColor(255, 255, 0)
    circle(x, y, radius)


def draw_sea(x, y, hight_sea):
    brushColor(0, 51, 102)
    rectangle(0, y, x, y + hight_sea // 3)
    width_sea = x

    return x, y + hight_sea // 4


def draw_boat(x, y, width, height, size):
    """ x, y - position rostrum
        x + size ends of ship"""
    points_rostrum = [(width - 20, height - height // 1.5), (width - 60, height - height // 1.5),
                      (width - 60, height - height // 2)]
    brushColor(153, 76, 0)
    polygon(points_rostrum)

def draw_beach(x, y, hight_beach):
    pass


def draw_umbrella(x, y, length):
    pass


def picture():
    x, y = draw_sky(0, 0, WIDTH_PICTURE, HEIGHT_PICTIRE / 2)
    x, y = draw_sea(x, y, HEIGHT_PICTIRE)
    draw_boat(x, y, WIDTH_PICTURE, HEIGHT_PICTIRE, 100)
    run()


if __name__ == '__main__':
    picture()
