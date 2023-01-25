my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s
print(max_min([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))