import re

def process_product_codes(n, codes):
    results = []
    for code in codes:
        uppercase_letters = ''.join(re.findall(r'[A-Z]', code))
        numbers = sum(map(int, re.findall(r'-?\d+', code)))
        results.append(f"{uppercase_letters}{numbers}")
    return results

n = int(input())
codes = [input().strip() for _ in range(n)]

for result in process_product_codes(n, codes):
    print(result)
