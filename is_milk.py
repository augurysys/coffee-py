import numpy as np

GRIDING_FREQ1 = 40
GRIDING_WIN1 = 15
THRESH_1 = 0.42


def is_milk(x_fft, fft_scale):

    all_energy = np.sum(x_fft)

    start_ix1 = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ1 - GRIDING_WIN1)
    end_ix1 =  next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ1 + GRIDING_WIN1)
    enrgey_freq_1 = np.sum(x_fft[start_ix1:end_ix1])
    enrgey_prec1 = enrgey_freq_1/all_energy


    if enrgey_prec1 >= THRESH_1:
        return True

    return False
