import re


def prod_grp(text):
    pg_list = [ch for ch in text if 48 <= ord(ch) <= 57]
    pg_string = ''.join(pg_list)
    if len(pg_list) == 0:
        return '00'
    else:
        return pg_string


n = int(input())

pattern = r'@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+'
for _ in range(n):
    line = input()
    if re.findall(pattern, line):
        valid_barcode = re.findall(pattern, line)[0]
        product_group = prod_grp(valid_barcode)
        print(f'Product group: {product_group}')
    else:
        print(f'Invalid barcode')
