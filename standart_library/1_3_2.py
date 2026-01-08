"""
Подвиг 7. С помощью класса Enum объявите перечисление PlatformOS со следующими константами:

WINDOWS = 'wnd'
LINUX = 'linux'
Объявите функцию с сигнатурой:

def path_join(*args, p:PlatformOS=PlatformOS.LINUX)
которая формирует и возвращает маршрут к файлу на основе фрагментов пути, указанных в первых
позиционных аргументах args. Если используется платформа LINUX, то разделителем каталогов должен
быть символ '/'. Если же используется платформа WINDOWS, то разделителем является символ '\'
(этот символ должен экранироваться в тексте программы).

Вызовите функцию path_join с позиционными аргументами:

"usr", "bin", "java", "course.java"

для построения маршрута на платформе WINDOWS. Результат сохраните в переменной filename.

P.S. На экран ничего выводить не нужно.
"""

from enum import Enum

class PlatformOS(Enum):
	WINDOWS = 'wnd'
	LINUX = 'linux'


def path_join(*args, p:PlatformOS=PlatformOS.LINUX) -> str:
	if p == PlatformOS.WINDOWS:
		return '\\'.join(args)

	elif p == PlatformOS.LINUX:
		return '/'.join(args)



filename = path_join("usr", "bin", "java", "course.java", p=PlatformOS.WINDOWS)
# filename = path_join("usr", "bin", "java", "course.java", p=PlatformOS.LINUX)
print(filename)