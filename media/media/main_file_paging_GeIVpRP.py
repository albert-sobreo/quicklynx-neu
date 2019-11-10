from random import randint
size = 2048

tlb = {'page 0': 'frame 4', 'page 1': 'frame 3', 'page 2': 'frame 1', 'page 3': 'frame 5', 'page 4': 'frame 2'}
for i, j in tlb.items():
    print(i, '-->', j)

cpu_generated_address = randint(0,10239)
print('Generated Logical Address:', hex(cpu_generated_address))
page_no, page_offset = int(cpu_generated_address/size), cpu_generated_address % size
print(page_no, page_offset)

frame = tlb['page {}'.format(page_no)]
print('Physical Address:', hex(int(frame[-1])*size + page_offset))
input()