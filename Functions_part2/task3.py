from random import randint


def main(prime_list):
    prime = []
    for i in prime_list:
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1

        if counter == 1:
            prime.append(i)
            
    return len(prime)


my_list = [randint(0,100) for i in range(20)]
if __name__ == '__main__':
    print(f'The number of prime numbers in the list is: {main(my_list)}')
