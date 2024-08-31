def calculate_unit_value(items):
  for item in items:
    item.append(item[1] / item[0])
  return items
def sort_by_unit_value(items):
  items.sort(key=lambda x: x[2], reverse=True)
  return items
def sack(items, lim):
  total_value = 0  
  remaining = lim
  for item in items:
    if item[0] <= remaining:
      total_value += item[1]
      remaining -= item[0]
    else:
      fraction = remaining / item[0]
      total_value += item[1] * fraction
      break 
  return total_value
def solution(items,lim):
  items = calculate_unit_value(items)
  items = sort_by_unit_value(items)
  return sack(items, lim)  
