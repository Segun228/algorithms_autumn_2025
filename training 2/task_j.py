import sys

class Shop:
    def __init__(self, single_cost, bulk_min, bulk_cost, max_items):
        self.single_cost = single_cost
        self.bulk_min = bulk_min
        self.bulk_cost = bulk_cost
        self.max_items = max_items

class Cell:
    def __init__(self, total=0, take_here=0, take_before=0):
        self.total = total
        self.take_here = take_here
        self.take_before = take_before

def calc_cost(shop, cnt):
    if cnt > shop.max_items:
        return 10**9
    if cnt < shop.bulk_min:
        return cnt * shop.single_cost
    return cnt * shop.bulk_cost

def main():
    input_data = sys.stdin.read().strip().split()
    pos = 0
    shops_count = int(input_data[pos])
    pos += 1
    needed = int(input_data[pos])
    pos += 1
    shops = []
    for g in range(shops_count):
        a = int(input_data[pos])
        pos += 1
        b = int(input_data[pos])
        pos += 1  
        c = int(input_data[pos])
        pos += 1
        d = int(input_data[pos])
        pos += 1
        shops.append(Shop(a, b, c, d))
    table = [[Cell() for _ in range(101)] for _ in range(shops_count)]

    for cnt in range(101):
        table[0][cnt].total = calc_cost(shops[0], cnt)
        table[0][cnt].take_here = cnt

    for shop_idx in range(1, shops_count):
        for total_cnt in range(101):
            best_cost = calc_cost(shops[shop_idx], total_cnt)
            best_here = total_cnt
            best_before = 0

            for prev_cnt in range(total_cnt + 1):
                current_cnt = total_cnt - prev_cnt
                cost_here = calc_cost(shops[shop_idx], current_cnt)
                cost_before = table[shop_idx-1][prev_cnt].total
                total_cost = cost_here + cost_before
                
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_here = current_cnt
                    best_before = prev_cnt

            table[shop_idx][total_cnt].total = best_cost
            table[shop_idx][total_cnt].take_here = best_here
            table[shop_idx][total_cnt].take_before = best_before

    min_cost = table[shops_count-1][needed].total
    best_total = needed

    for cnt in range(needed, 101):
        if table[shops_count-1][cnt].total < min_cost:
            min_cost = table[shops_count-1][cnt].total
            best_total = cnt
    
    if min_cost == 10**9:
        print(-1)
        return

    purchases = []
    current_cnt = best_total

    for shop_idx in range(shops_count-1, -1, -1):
        purchases.append(str(table[shop_idx][current_cnt].take_here))
        current_cnt = table[shop_idx][current_cnt].take_before

    purchases.reverse()

    print(min_cost)
    print(' '.join(purchases))

if __name__ == "__main__":
    main()