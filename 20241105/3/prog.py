from copy import deepcopy
from collections import deque

BLOCK = "█"
class Maze:
    def __init__(self, N=4):
        self.n = N
        self.s = [[BLOCK] * (2*N + 1) for _ in range(2*N + 1)]
        for i in range(2*N + 1):
            for j in range(2*N + 1):
                if i % 2 and j % 2:
                    self.s[i][j] = "."
    
    def __str__(self):
        print()
        return "\n".join("".join(r) for r in self.s)
    
    def __setitem__(self, key, value):
        x0, y1 = key[0], key[2]
        y0, x1 = key[1].start, key[1].stop 

        if x0 == x1:  
            for j in range(min(y0, y1)*2 + 1, max(y0, y1)*2 + 2):
                self.s[j][2 * x0 + 1] = value
        elif y0 == y1:  
            for i in range(min(x0, x1)*2 + 1, max(x0, x1)*2 + 2):
                self.s[2 * y0 + 1][i] = value

    def __getitem__(self, key):
        start = (key[1].start * 2 + 1, key[0] * 2 + 1)  
        stop = (key[2] * 2 + 1, key[1].stop * 2 + 1)  
        return self.find(start, stop)

    def find(self, p1, p2):
        # Используем очередь для BFS
        queue = deque([p1])
        visited = set()  # Множество посещенных точек

        visited.add(p1)
        steps = {}  # Словарь для хранения шагов
        steps[p1] = 0  # Начальная точка имеет шаг 0

        # Список направлений (вверх, вправо, вниз, влево)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            cur = queue.popleft()

            if cur == p2:
                return True  # Путь найден

            # Проверка всех направлений
            for dx, dy in directions:
                nx, ny = cur[0] + dx, cur[1] + dy

                # Проверяем, если сосед не посещен и проходим
                if 0 <= nx < len(self.s) and 0 <= ny < len(self.s[0]):
                    if self.s[nx][ny] == '·' and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        steps[(nx, ny)] = steps[cur] + 1  # Устанавливаем шаг для соседа

        return False  # Путь не найден
    
   
import sys
exec(sys.stdin.read())