"""
Подвиг 6. С помощью класса deque создайте объект очереди с именем fifo. Затем реализуйте в
программе очередь типа FIFO, используя объект fifo, следующим образом:

поместите в очередь данные, прочитанные из входного потока с помощью команды:
data = list(map(int, input().split()))

извлеките из очереди три объекта (три целых числа) и сохраните их в списке out_lst в порядке извлечения.
Извлечение из очереди подразумевает удаление элемента очереди.

P.S. На экран ничего выводить не нужно.
"""
from collections import deque

data = list(map(int, input().split()))  # этот список в программе не менять

# здесь продолжайте программу
fifo: deque = deque()
fifo.extend(data)
out_lst: list = [fifo.popleft() for _ in range(3) if fifo]

print(out_lst)
print(fifo)





# from collections import deque
#
# lst_in = list(map(str.strip, input().split()))  # этот список в программе не менять
#
# # здесь продолжайте программу
# q = deque()
# q.extend(lst_in)
# q.insert(2, "run")
# if "edit" in q:
# 	q.remove("edit")
#
