from threading import Thread

finish_results = []


def get_primes(start: int, end: int) -> list[int]:
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            results.append(number)
    [finish_results.append(i) for i in results]
    return results


start = 100
end = 10_000
num_threads = 5


threads: list[Thread] = []
# value_range: list[tuple] = [] -check range for treading
for i in range(1, num_threads + 1):
    new_end = int(end * (i / num_threads))
    threads.append(
        Thread(
            target=get_primes,
            args=[start, new_end],
        )
    )
    # value_range.append((start, new_end))
    start = new_end


def run_threads():
    for thread in threads:
        thread.start()
        thread.join()


def main():
    run_threads()
    print(finish_results)


if __name__ == "__main__":
    main()
