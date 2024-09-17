from fracgm import FracGM

# test variaous initial values
initial_list = [-10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000]

for initial_guess in initial_list:
    print("="*20)
    FracGM().solve(initial=initial_guess)