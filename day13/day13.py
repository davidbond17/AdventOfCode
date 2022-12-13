from json import loads

def compare(left: list, right: list):
    try:
        for i in range(len(left)):
            left_val = left[i]
            right_val = right[i]

            if isinstance(left_val, int) and isinstance(right_val, int):
                if left_val < right_val:
                    return True
                elif left_val > right_val:
                    return False
                else:
                    continue
            if isinstance(left_val, int) and isinstance(right_val, list):
                if compare([left_val], right_val) is None:
                    continue
                else:
                    return compare([left_val], right_val)    
            if isinstance(left_val, list) and isinstance(right_val, int):
                if compare(left_val, [right_val]) is None:
                    continue
                else:
                    return compare(left_val, [right_val])
            else:
                if compare(left_val, right_val) is None:
                    continue
                else:
                    return compare(left_val, right_val)
        
        if len(left) < len(right):
            return True
        return None
    except IndexError:
        return False

def sort(packets: list):
    for i in range(1, len(packets)):
        value = packets[i]
        i2 = i
        while i > 0 and compare(value, packets[i2 - 1]):
            packets[i2] = packets[i2-1]
            i2 -= 1
            packets[i2] = value
    return packets

def main():
    with open('/Users/david/development/AdventOfCode/day13/input') as reader:
        comparison_packets = reader.read().split('\n\n')
        valid_packets = []
        for x, pair in enumerate(comparison_packets):
            left, right = pair.split('\n')
            left = loads(left)
            right = loads(right)
            if compare(left, right):
                valid_packets.append(x)
        print ('Sum of indicies of valid packets: ' + str(sum(valid_packets) + len(valid_packets)))

        packets = [loads(packet) for pair in comparison_packets for packet in pair.split('\n')]
        packets.append([[2]])
        packets.append([[6]])
        
        print('Index of [2]: ' + str(sort(packets).index([[2]]) + 1) + '\nIndex of [6]: ' + str(sort(packets).index([[6]]) + 1))
        print ('Answer: ' + str((sort(packets).index([[2]]) + 1) * (sort(packets).index([[6]]) + 1)))
main()