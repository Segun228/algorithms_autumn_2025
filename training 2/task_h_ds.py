from math import isqrt

def is_prime(n):
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = isqrt(n) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def main():
    N = int(input())
    
    # dp[i] = True если позиция i выигрышная для текущего игрока
    dp = [False] * (N + 1)
    
    # Базовый случай: 0 спичек - проигрыш (нельзя сделать ход)
    dp[0] = False
    
    for i in range(1, N + 1):
        # Проверяем все возможные ходы
        for take in [1, 2, 3]:
            remaining = i - take
            if remaining >= 0 and not is_prime(remaining):
                # Если можем перейти в проигрышную позицию противника
                if not dp[remaining]:
                    dp[i] = True
                    break
    
    print(1 if dp[N] else 2)

if __name__ == "__main__":
    main()