import random
import time
from multiprocessing import Pool, cpu_count, Manager
from tqdm import tqdm
from threading import Thread

# === Настройки колоды ===
ranks = list(range(2, 15))
suits = ['♠', '♥', '♦', '♣']
deck = [(rank, suit) for rank in ranks for suit in suits]

def is_pair(hand):
    return hand[0][0] == hand[1][0]

# === Воркеры ===
def worker(n_trials, queue, seed):
    random.seed(seed + time.time())
    success = 0
    for _ in range(n_trials):
        cards = random.sample(deck, 6)
        hands = [cards[i*2:(i+1)*2] for i in range(3)]
        if all(is_pair(hand) for hand in hands):
            success += 1
        queue.put(1)
    return success

def tqdm_updater(queue, pbar):
    while True:
        try:
            msg = queue.get(timeout=1)
            pbar.update(msg)
        except:
            break

# === Основной запуск ===
if __name__ == "__main__":
    total_trials = 100_000_000
    batch_size = 1_000_000
    n_batches = total_trials // batch_size
    n_jobs = cpu_count()

    manager = Manager()
    queue = manager.Queue()
    progress_bar = tqdm(total=total_trials, desc="Simulating")

    t = Thread(target=tqdm_updater, args=(queue, progress_bar))
    t.start()

    with Pool(processes=n_jobs) as pool:
        seeds = list(range(n_batches))
        results = pool.starmap(worker, [(batch_size, queue, seed) for seed in seeds])

    t.join()
    progress_bar.close()

    success_total = sum(results)
    probability = success_total / total_trials
    print(f"\nВероятность: {probability:.6%}")