import scipy.signal as signal

numerator = [3, -4]
denominator = [-1.6, 0.6]

zeros, poles, gain = signal.tf2zpk(numerator, denominator)
print("Poles:", poles)
0.6x^2 +1.6x -0.6