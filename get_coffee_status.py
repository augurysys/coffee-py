import numpy as np
from is_grinding import is_grinding
from is_milk import is_milk
from is_water import is_water
import event_types

F_S = 1000

def get_coffee_status(x_window):
    x_window = x_window - np.mean(x_window)

    signal_rms = np.mean(np.abs(x_window))

    # do fft
    x_fft = np.fft.fft(x_window)
    x_fft = np.abs(x_fft[:(len(x_fft) + 1) / 2])
    freq = np.fft.fftfreq(len(x_window), 1.0 / F_S)
    freq = freq[:(len(freq) + 1) / 2]

    water_stat = is_water(x_fft, freq)
    if water_stat:
        return event_types.WATER, signal_rms
    grinding_stat = is_grinding(x_fft, freq)
    if grinding_stat:
        return event_types.GRINDING, signal_rms

    milk_stat = is_milk(x_fft, freq)
    if milk_stat:
        return event_types.MILK, signal_rms

    return event_types.IDLE, signal_rms




