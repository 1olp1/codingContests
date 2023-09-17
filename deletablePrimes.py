def main():
    f = open("n_to_check.txt", "r")
    numbers = f.readlines()
    f.close()
    for i, number in enumerate(numbers):
        number = number.strip()
        n = int(number)
        ways = count_deletable_primes(n)
        print(f"Number: {number} \tWays: {ways}")


def count_deletable_primes(n):
    count = 0
    if is_prime(n):
        if n < 10:
            count += 1
        else:
            for i in range(len(str(n))):
                new_n = int(str(n)[:i] + str(n)[i+1:])
                count += count_deletable_primes(new_n)
    return count


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
