# -*- coding: utf-8 -*-
"""
Игра «Жизнь» (Conway's Game of Life) в консольном режиме.
Чтение начальной конфигурации, моделирование, сохранение состояний и PNG-изображений.
"""

from PIL import Image, ImageDraw
import sys
import os

# Параметры по умолчанию (можно переопределить через аргументы командной строки)
FILE_NAME = 'GoL_02.txt'
IMAGE_FILE_NAME = 'GoL'
STEPS = 10
CELL_SIZE = 20
BORDER_WIDTH = 2
BASE_COLOR = (0, 255, 0)  # Зелёный — базовый цвет «живой» клетки


def live_neighbors(grid, r, c):
    """Подсчитывает число живых соседей клетки (r, c)."""
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] > 0:  # клетка жива (возраст >= 1)
                    count += 1
    return count


def init_file(file_name):
    """Читает начальную конфигурацию из файла."""
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()

    rows, cols = map(int, lines[0].strip().split())
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for line in lines[1:]:
        r, c = map(int, line.strip().split())
        grid[r][c] = 1  # начальная возрастная метка = 1

    return grid


def simulation_step(grid):
    """Выполняет один шаг моделирования по правилам игры «Жизнь»."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            live_count = live_neighbors(grid, r, c)
            cell = grid[r][c]

            if cell > 0:  # клетка жива
                if live_count == 2 or live_count == 3:
                    new_grid[r][c] = cell + 1  # стареет
                else:
                    new_grid[r][c] = 0  # умирает
            else:  # клетка мертва
                if live_count == 3:
                    new_grid[r][c] = 1  # рождается
                else:
                    new_grid[r][c] = 0

    return new_grid


def save_grid_to_file(grid, step, output_dir="output"):
    """Сохраняет текущее состояние поля в текстовый файл."""
    filename = os.path.join(output_dir, f"grid_{step:03d}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{len(grid)} {len(grid[0])}\n")
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val > 0:
                    f.write(f"{r} {c}\n")


def visualize(grid, step, base_color=BASE_COLOR, output_dir="output"):
    """Создаёт PNG-изображение текущего состояния поля."""
    rows, cols = len(grid), len(grid[0])
    cell_size = CELL_SIZE
    border = BORDER_WIDTH

    width = cols * (cell_size + border) + border
    height = rows * (cell_size + border) + border

    im = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(im)

    # Рисуем сетку (границы ячеек)
    for x in range(0, width, cell_size + border):
        draw.line((x, 0, x, height - 1), fill="gray", width=border)
    for y in range(0, height, cell_size + border):
        draw.line((0, y, width - 1, y), fill="gray", width=border)

    # Заполняем клетки
    for r in range(rows):
        for c in range(cols):
            age = grid[r][c]
            if age > 0:
                # Рассчитываем оттенок: чем старше, тем темнее
                factor = max(0.2, 1.0 - 0.1 * (age - 1))  # не темнее 20%
                color = tuple(int(channel * factor) for channel in base_color)

                x1 = c * (cell_size + border) + border
                y1 = r * (cell_size + border) + border
                x2 = x1 + cell_size - 1
                y2 = y1 + cell_size - 1
                draw.rectangle((x1, y1, x2, y2), fill=color)

    filename = os.path.join(output_dir, f"{IMAGE_FILE_NAME}_{step:03d}.png")
    im.save(filename)


def main():
    """Основная функция: запуск моделирования."""
    # Обработка аргументов командной строки (если есть)
    if len(sys.argv) >= 2:
        global FILE_NAME
        FILE_NAME = sys.argv[1]
    if len(sys.argv) >= 3:
        global STEPS
        STEPS = int(sys.argv[2])
    if len(sys.argv) >= 4:
        global BASE_COLOR
        # Пример: "255,0,0" → красный
        r, g, b = map(int, sys.argv[3].split(','))
        BASE_COLOR = (r, g, b)

    # Создаём директорию для вывода
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Инициализация поля
    grid = init_file(FILE_NAME)
    print(f"Начальное состояние загружено: {len(grid)}x{len(grid[0])}")

    # Моделирование
    for step in range(STEPS + 1):  # включая шаг 0 (начальное состояние)
        print(f"Шаг {step}...")
        save_grid_to_file(grid, step, output_dir)
        visualize(grid, step, BASE_COLOR, output_dir)
        if step < STEPS:
            grid = simulation_step(grid)

    print("Моделирование завершено. Результаты в папке 'output/'.")


if __name__ == "__main__":
    main()
