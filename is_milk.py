import numpy as np

GRIDING_FREQ1 = 40
GRIDING_WIN1 = 18
THRESH_1 = 0.29

GRIDING_FREQ2 = 150
GRIDING_WIN2 = 2
THRESH_2 = 0.05

def is_milk(x_fft, fft_scale):

    all_energy = np.sum(x_fft)

    start_ix1 = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ1 - GRIDING_WIN1)
    end_ix1 =  next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ1 + GRIDING_WIN1)
    enrgey_freq_1 = np.sum(x_fft[start_ix1:end_ix1])
    enrgey_prec1 = enrgey_freq_1/all_energy

    start_ix2 = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ2 - GRIDING_WIN2)
    end_ix2 =  next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ2 + GRIDING_WIN2)
    enrgey_freq_2 = np.sum(x_fft[start_ix2:end_ix2])
    enrgey_prec2 = enrgey_freq_2/all_energy

    if enrgey_prec1 >= THRESH_1 and  enrgey_prec2 <= THRESH_2 : # milk and not water
        return True

    return False
