#!/usr/bin/env python

#TODO: @apick
# [ ] line chart
#   - x=time, y=unemployment percentage
#   - each line different category

import os

from bokeh.plotting import figure, show
from bokeh.models.tools import PanTool, WheelZoomTool
import pandas

def main():

    abs_filepaths = [
        os.path.abspath(os.path.join(dirpath, filepath)) 
        for dirpath, _, filepaths in os.walk('../datasets/bls')
        for filepath in filepaths
        if os.path.splitext(filepath)[-1] == '.xlsx'
            ]
    abs_filepaths.sort()
    print(len(abs_filepaths))
    header_start_lines = [12] + [13] * (len(abs_filepaths) - 1)
    df_list = [
        pandas.read_excel(fp, header=hsl) for fp, hsl in zip(abs_filepaths, header_start_lines)
            ]
    print(df_list)
    exit()

    x = list(range(1,6))
    y1 = [6, 7, 2, 4, 5]
    y2 = list(range(2,7))
    y3 = [4, 5, 5, 7, 2]

    plot = figure(title="Multi-line Ex", x_axis_label="Time", y_axis_label="y",
                  active_drag="pan", active_scroll="wheel_zoom")

    plot.line(x, y1, legend_label="Temp.", color="aqua", line_width=2)
    plot.vbar(x=x, top=y2, legend_label="Rate", width=0.5, bottom=0, color="coral")
    plot.circle(x, y3, legend_label="Objects", color="black", line_width=2)

    show(plot)

if __name__ == "__main__":
    main()
