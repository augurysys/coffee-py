import numpy as np

GRIDING_FREQ1 = 100
GRIDING_WIN1 = 2
GRIDING_FREQ2 = 300
GRIDING_WIN2 = 30
THRESH_1 = 0.05
THRESH_2 = 0.1
THRESH_2b = 0.2


def is_grinding(x_fft, fft_scale):

    all_energy = np.sum(x_fft)
    start_ix1 = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ1 - GRIDING_WIN1)
    end_ix1 =  next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ1 + GRIDING_WIN1)
    enrgey_freq_1 = np.sum(x_fft[start_ix1:end_ix1])
    enrgey_prec1 = enrgey_freq_1/all_energy


    start_ix2 = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ2 - GRIDING_WIN2)
    end_ix2 = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ2 + GRIDING_WIN2)
    enrgey_freq_2 = np.sum(x_fft[start_ix2:end_ix2])
    enrgey_prec2 = enrgey_freq_2/all_energy


    if enrgey_prec1 >= THRESH_1 and enrgey_prec2 >= THRESH_2:
        return True

    if enrgey_prec2 >= THRESH_2b:
        return True

    return False
