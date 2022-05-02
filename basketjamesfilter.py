import instream
import outstream
import stddraw
import color

COLORS = [color.RED, color.BLUE, color.CYAN, color.GREEN,
          color.MAGENTA, color.ORANGE, color.PINK,
          color.VIOLET, color.YELLOW, color.GRAY,
          color.DARK_RED, color.DARK_BLUE, color.DARK_GREEN
          ]


def plot_bars(data_dict):
    # Modified from stdstats.plotBars() to include color coding
    n = len(data_dict)
    stddraw.setXscale(-1, n)
    for i in range(n):
        stddraw.setPenColor(data_dict[i]['color'])
        stddraw.filledRectangle(i - 0.25, 0.0, 0.5, data_dict[i]['data'])
    return True


y = instream.InStream('basketballRAW.csv')
y_read = y.readAllLines()
for index, line in enumerate(y_read):
    y_read[index] = line.split(',')

out_filter1 = []
out_filter2 = []

out1 = outstream.OutStream('output1.csv')
out2 = outstream.OutStream('output2.csv')

out1.write(','.join(out_filter1))