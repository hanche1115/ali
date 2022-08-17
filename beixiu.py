import numpy as np
import pygame

X_DOT=50
Y_DOT=50
DOT_PX=20
np.random.seed(100)
source_a=np.random.randint(0,2,(X_DOT,Y_DOT))
copy_a=np.copy(source_a)

def has_counts(a, x, y):
    counts = 0

    # 考虑更多因素
    if x > X_DOT:
        x = X_DOT - 1  # 直接抛异常
    if y > Y_DOT:
        y = Y_DOT - 1
	
    if (x > 0) and (y > 0) and a[x - 1, y - 1]:
        counts += 1  # counts = counts+1
    if (x > 0) and a[x - 1, y]:
        counts += 1
    if (x > 0) and (y + 1 < Y_DOT) and a[x - 1, y + 1]:
        counts += 1
    if (y > 0) and a[x, y - 1]:
        counts += 1
    if (y + 1 < Y_DOT) and a[x, y + 1]:
        counts += 1
    if (y > 0) and (x + 1 < X_DOT) and a[x + 1, y - 1]: 
        counts += 1
    if (x + 1 < X_DOT) and a[x + 1, y]:
        counts += 1
    if (y + 1 < Y_DOT) and (x + 1 < X_DOT) and a[x + 1, y + 1]:
        counts += 1

    return counts

def live_or_die(life_counts,x,y,a):
	#函数判断生命的状态
    if life_counts ==3:
        return 1
    elif life_counts ==2:
        return a[x,y]
    else:
        return 0
def next_a(source_a):
    for x in range(X_DOT):
        for y in range(Y_DOT):
            copy_a[x,y] = live_or_die(has_counts(source_a,x,y),x,y,source_a)
    return copy_a


def main():
	#用pygame生成界面
    pygame.init()
    pygame.display.set_caption('生命游戏')
    screen = pygame.display.set_mode((DOT_PX * X_DOT, DOT_PX * Y_DOT))
    running = True
    global source_a
    while running:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for x in range(X_DOT):
            for y in range(Y_DOT):
                if source_a[x,y]:
                    screen.fill((0,0,225),(y*DOT_PX,x*DOT_PX,DOT_PX,DOT_PX))
                    pygame.draw.rect(screen,(0,255,0),(y*DOT_PX,x*DOT_PX,DOT_PX,DOT_PX),2)

        pygame.display.update()
        next_a(source_a)
        source_a=copy_a
        pygame.time.wait(500)

if __name__ == '__main__':
    main()
