def main():
    weekly_temperatute = []
    while True:
        dail_temp = input('Enter daily temperature (type "Done" to finish): ')
        if dail_temp == 'Done' or dail_temp == 'done':
            break
        weekly_temperatute.append(int(dail_temp))

    print(f'Weekly temperatures: {weekly_temperatute}')
    print(f'Average temperature: {sum(weekly_temperatute) / len(weekly_temperatute)} degrees Celsius.')
    print('Days with temperature exceeding 25 degrees Celsius:')
    for i, t in enumerate(weekly_temperatute):
        if t > 25:
            print(f'- Day {i + 1}: {t} degrees Celsius')


if __name__ == '__main__':
    main()
