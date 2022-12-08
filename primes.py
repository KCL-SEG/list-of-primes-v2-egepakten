"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes >= 1:
        if number_of_primes == 1:
            list.append(2)
            return list
        prime_range = int(number_of_primes)**2
        for check_prime in range(2, prime_range):
            primeCounter = 0
            if len(list) < number_of_primes:
                for j in range(2,prime_range):
                    if check_prime % j == 0:
                        if check_prime != j:
                            break
                        primeCounter+=1
                if (primeCounter >= 1):
                    list.append(check_prime)
        return list
    else:
        raise ValueError

print(primes(0))
