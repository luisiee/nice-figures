import matplotlib.pyplot as plt

plt.style.use('nicefigures.mplstyle')

_COLORS = [tuple(int(hex[i:i+2], 16)/256 for i in (0, 2, 4)) for hex in ['1F1F1F', '0C5DA5', 'FF2C00', '00B945', 'FF9500']]
BLACK, BLUE, RED, GREEN, YELLOW = _COLORS
