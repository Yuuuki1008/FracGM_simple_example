from fracgm import FracGM
model = FracGM(verbose=True)

# test variaous initial values
initial_list = [-10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000]

for initial_guess in initial_list:
    print("="*50)
    model.solve(initial=initial_guess)