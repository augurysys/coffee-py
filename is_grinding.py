import numpy as np

GRIDING_FREQ1 = 100
GRIDING_WIN1 = 2
GRIDING_FREQ2 = 50
GRIDING_WIN2 = 2
THRESH_1 = 0.05
THRESH_12 = 5

GRIDING_FREQ3 = 290
GRIDING_WIN3 = 30
GRIDING_WIN3a = 2
THRESH_3 = 0.10
THRESH_3b = 0.18


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

    tt = enrgey_prec1/enrgey_prec2

    start_ix3 = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ3 - GRIDING_WIN3)
    end_ix3 = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ3 + GRIDING_WIN3)
    enrgey_freq_3 = np.sum(x_fft[start_ix3:end_ix3])
    enrgey_prec3 = enrgey_freq_3/all_energy

    start_ix3a = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ3 - GRIDING_WIN3a)
    end_ix3a = next(x[0] for x in enumerate(fft_scale) if x[1] > GRIDING_FREQ3 + GRIDING_WIN3a)
    enrgey_freq_3a = np.sum(x_fft[start_ix3a:end_ix3a])
    enrgey_prec3a = enrgey_freq_3a/all_energy

    enrgey_prec3 = enrgey_prec3 - enrgey_prec3a


    if enrgey_prec1 >= THRESH_1 and tt >= THRESH_12:
        return True

    if enrgey_prec3 >= THRESH_3 and enrgey_prec1 > THRESH_1:
        return True

    if enrgey_prec3 >= THRESH_3b:
        return True



    return False
