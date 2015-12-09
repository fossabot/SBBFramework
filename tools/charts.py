#!/usr/bin/env python
# encoding: utf-8
## vim:ts=4:et:nowrap

# http://www.danielsoper.com/statcalc3/calc.aspx?id=96
# https://www.mccallum-layton.co.uk/tools/statistic-calculators/confidence-interval-for-mean-calculator/#confidence-interval-for-mean-calculator

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import matplotlib.mlab as mlab
import math

patches = []

use_chart1 = True

if use_chart1:

#     d = [
# [0.49066, 0.49634, 0.50065, 0.4946, 0.50372, 0.5051, 0.49617, 0.5038, 0.50608, 0.49516, 0.50827],
# [0.48511, 0.50004, 0.49611, 0.50809, 0.51153, 0.50683, 0.50871, 0.51697, 0.5187, 0.5095, 0.51535],
# [0.50721, 0.52754, 0.53179, 0.52584, 0.53023, 0.53009, 0.53245, 0.52906, 0.53686, 0.53361, 0.53457],
# [0.48511, 0.49618, 0.49961, 0.50671, 0.51264, 0.51746, 0.52004, 0.51504, 0.51776, 0.51548, 0.51721],
# [0.48169, 0.49941, 0.50398, 0.50323, 0.50574, 0.50356, 0.51519, 0.5212, 0.51901, 0.52179, 0.51271],
# [0.47023, 0.52018, 0.5395, 0.56514, 0.56678, 0.57567, 0.57472, 0.57627, 0.57842, 0.57693, 0.58157],
# [0.52581, 0.58052, 0.58598, 0.5877, 0.58603, 0.58737, 0.58597, 0.58473, 0.58683, 0.58788, 0.58858],
#     ]

#     data = d[0]
#     color = 'r'
#     plt.plot(data,color)
#     patches.append(mpatches.Patch(color=color, label='run1'))

#     data = d[1]
#     color = 'b'
#     # color = '#B00000'
#     plt.plot(data,color)
#     patches.append(mpatches.Patch(color=color, label='run2'))

#     data = d[2]
#     color = 'g'
#     # color = 'b'
#     plt.plot(data,color)
#     patches.append(mpatches.Patch(color=color, label='run3'))

#     data = d[3]
#     color = 'm'
#     # color = '#000066'
#     plt.plot(data,color)
#     patches.append(mpatches.Patch(color=color, label='run4'))

#     data = d[4]
#     color = 'c'
#     # color = 'g'
#     plt.plot(data,color)
#     patches.append(mpatches.Patch(color=color, label='run5'))

#     data = d[5]
#     color = 'y'
#     # color = '#003300'
#     plt.plot(data,color)
#     patches.append(mpatches.Patch(color=color, label='run6'))

#     data = d[6]
#     color = 'k'
#     plt.plot(data,color)
#     patches.append(mpatches.Patch(color=color, label='run7'))

#     plt.title("Champion")
#     plt.legend(handles=patches, loc=1)
#     # plt.axis([0, 6, 0, 1.0]) # per validation
#     plt.axis([0, 10, 0.4, 0.8]) # per validation
#     # plt.axis([0, 200, 0.4, 0.8]) # per training
#     # plt.axis([0, 149, 0.0, 1.0]) # per training
#     # plt.axis([0, 124, 0.4, 0.8]) # per training, diversity
#     # plt.axis([0, 99, 0.4, 0.8]) # per training, opponent
#     plt.show()

    #######################################

    d = [
[222.61, 221.65, 221.48, 221.12, 220.57, 219.92, 219.75, 219.249, 218.08, 216.0, 214.24, 213.3, 212.519, 211.82, 211.51, 210.779, 209.77, 209.299, 208.889, 208.359, 207.39, 206.679, 206.27, 205.2, 204.549, 203.379, 202.759, 202.349, 201.849, 201.579, 201.029, 200.63, 199.679, 198.799, 198.009, 197.079, 196.279, 195.359, 194.269, 193.549, 192.189, 191.659, 190.389, 187.889, 186.879, 185.799, 184.679, 178.989, 170.109, 161.919],
[222.61, 230.78, 238.8, 240.27, 240.91, 242.31, 242.869, 243.01, 246.37, 247.279, 248.4, 248.8, 249.48, 249.91, 250.689, 252.88, 253.28, 254.869, 255.45, 256.35, 256.57, 256.94, 257.149, 257.81, 257.82, 257.86, 258.06, 258.789, 260.12, 260.14, 261.12, 261.12, 261.149, 261.169, 261.18, 261.329, 261.55, 261.61, 261.89, 262.079, 262.1, 262.12, 262.12, 262.12, 262.18, 262.2, 262.219, 262.219, 262.26, 262.289]
    ]

    data = d[0]
    color = '#B00000'
    plt.plot(data, color)
    patches.append(mpatches.Patch(color=color, label='5: indiv.'))
    data = d[1]
    color = 'r'
    plt.plot(data, color)
    patches.append(mpatches.Patch(color=color, label='5: accum.'))

    d = [
[262.639, 262.269, 261.759, 261.099, 260.659, 259.679, 258.999, 257.869, 256.139, 254.639, 253.949, 253.449, 252.489, 251.49, 249.249, 247.299, 246.51, 244.529, 242.379, 238.65, 237.179, 236.689, 235.679, 233.919, 231.289, 230.269, 228.959, 226.829, 226.269, 223.689, 221.489, 217.679, 214.699, 212.189, 210.969, 207.409, 205.239, 200.319, 197.329, 191.399, 187.899, 184.489, 181.149, 178.259, 169.939, 167.179, 162.159, 159.529, 150.439, 136.489],
[262.639, 267.749, 270.199, 270.649, 271.859, 273.689, 275.439, 276.119, 276.599, 278.119, 278.669, 282.029, 283.029, 283.449, 283.589, 283.819, 284.059, 284.519, 285.679, 285.959, 286.379, 286.859, 286.909, 287.049, 287.179, 288.309, 288.679, 288.919, 289.169, 289.269, 290.309, 290.689, 291.609, 291.779, 292.339, 292.419, 293.299, 294.619, 295.249, 295.419, 296.359, 296.599, 296.729, 296.819, 296.839, 296.989, 297.159, 297.199, 297.199, 297.199]
    ]

    data = d[0]
    color = '#000066'
    plt.plot(data, color)
    patches.append(mpatches.Patch(color=color, label='6: indiv.'))
    data = d[1]
    color = 'b'
    plt.plot(data, color)
    patches.append(mpatches.Patch(color=color, label='6: accum.'))

    d = [
[268.909, 267.599, 266.809, 266.409, 265.639, 264.939, 264.249, 263.359, 262.929, 261.659, 260.319, 258.669, 257.729, 256.949, 255.559, 254.599, 253.919, 252.849, 251.509, 249.519, 247.829, 243.659, 241.6, 239.909, 237.689, 234.819, 233.729, 231.639, 227.049, 223.789, 219.78, 216.029, 211.649, 205.419, 198.799, 195.769, 189.729, 185.369, 180.989, 176.14, 173.379, 169.229, 162.019, 159.019, 154.579, 152.789, 141.749, 126.339, 113.569, 81.499],
[268.909, 275.059, 275.279, 278.349, 282.489, 283.639, 283.639, 285.029, 286.279, 288.469, 289.829, 291.949, 293.189, 293.749, 294.529, 295.269, 297.339, 298.869, 298.979, 303.159, 303.829, 304.629, 304.739, 305.719, 307.039, 307.309, 308.049, 308.659, 310.829, 312.149, 313.079, 313.329, 315.149, 315.559, 315.959, 315.989, 316.979, 317.939, 318.069, 318.569, 319.289, 319.309, 319.859, 319.879, 319.879, 319.919, 319.979, 319.979, 319.979, 319.979]
    ]
    data = d[0]
    color = '#006600'
    plt.plot(data, color)
    patches.append(mpatches.Patch(color=color, label='7: indiv.'))
    data = d[1]
    color = 'g'
    plt.plot(data, color)
    patches.append(mpatches.Patch(color=color, label='7: accum.'))

#     d = [
# [242.32, 239.399, 238.768, 237.899, 237.241, 236.024, 235.16, 234.464, 233.462, 231.695, 230.879, 230.166, 229.577, 228.797, 227.739, 227.11, 226.506, 225.31, 224.191, 222.974, 222.562, 221.762, 219.924, 219.041, 217.406, 216.993, 215.585, 215.166, 212.997, 211.333, 210.635, 208.218, 202.285, 201.381, 200.439, 199.772, 197.943, 196.439, 192.96, 184.939],
# [242.32, 256.031, 266.545, 270.168, 272.199, 278.424, 280.449, 281.649, 282.245, 283.993, 285.741, 286.731, 288.452, 289.687, 290.216, 290.697, 291.643, 292.314, 293.372, 295.956, 296.683, 298.022, 298.064, 298.149, 299.066, 299.202, 299.327, 300.102, 300.295, 300.424, 300.539, 302.595, 302.687, 302.774, 303.358, 303.595, 303.604, 303.604, 303.629, 303.92]
#     ]
#     data = d[0]
#     color = '#CC0066'
#     plt.plot(data, color)
#     patches.append(mpatches.Patch(color=color, label='4: indiv.'))
#     data = d[1]
#     color = 'm'
#     plt.plot(data, color)
#     patches.append(mpatches.Patch(color=color, label='4: accum.'))

    plt.title("Accumulative Curve")
    plt.legend(handles=patches, loc=3)
    plt.axis([0, 49, 0, 449])
    plt.show()
else:
    # m = [[0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.0, 0.153, 0.0, 0.0, 1.0, 0.0, 1.0], [0.0, 0.153, 0.0, 0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.423, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.423, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.423, 0.0, 1.0, 0.0], [0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.475, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.475, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.475, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.475, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.386, 0.538, 0.435, 0.0, 0.736, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.589, 1.0, 0.333, 0.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.589, 1.0, 0.333, 0.0, 0.0, 0.0, 0.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.508, 1.0, 0.589, 0.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.738, 0.0, 0.461, 0.884, 0.0, 0.0, 0.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.555, 1.0, 0.538, 0.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.466, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.508, 1.0, 0.589, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.538, 1.0, 0.0, 0.0, 0.0], [0.738, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.897, 0.0, 0.641, 0.884, 0.0, 0.0, 0.0]]
    # OLD
    # m = [[0.035, 0.0, 0.0, 0.0, 0.992, 0.0, 1.0], [0.035, 0.0, 0.0, 0.0, 0.992, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.452, 0.615, 0.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], [0.806, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]]

    # m = [[0.856, 0.846, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.846, 0.0, 0.447, 0.271, 0.0, 0.0], [0.625, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.856, 0.846, 0.0, 0.0, 0.0, 0.0, 0.0], [0.856, 0.846, 0.0, 0.0, 0.0, 0.0, 0.0], [0.625, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.198, 0.0, 0.0, 0.821, 0.0, 0.0, 0.0], [0.468, 0.0, 0.0, 0.931, 0.0, 0.0, 0.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.538, 0.0, 0.756, 1.0, 0.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.564, 0.0, 1.0, 0.0, 0.0], [0.795, 0.769, 0.0, 0.0, 0.0, 0.0, 1.0]]
    # m = [[0.64, 0.0, 0.41, 0.714, 0.0, 0.0, 0.0], [0.64, 0.0, 0.41, 0.714, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.64, 0.0, 0.41, 0.714, 0.0, 0.0, 0.0], [0.997, 0.923, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.672, 0.0, 1.0, 0.0, 0.802, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.756, 0.846, 0.0, 0.0, 0.0, 0.0, 1.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0], [0.12, 0.0, 0.384, 0.0, 0.362, 0.75, 0.0], [0.603, 0.0, 1.0, 0.884, 0.0, 0.0, 0.0]]

    # m = [[0.0, 0.0, 0.0, 0.439, 0.0, 0.75, 1.0], [0.756, 0.846, 0.358, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.439, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0], [0.66, 0.0, 0.0, 0.372, 0.0, 0.75, 1.0]]
    # m = [[0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.0, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.635, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.635, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.635, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0], [0.681, 0.846, 0.0, 0.0, 0.0, 0.0, 1.0], [0.493, 0.0, 0.615, 0.0, 0.0, 1.0, 0.0], [0.642, 0.0, 0.846, 0.0, 0.436, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.593, 0.0, 0.0], [0.635, 0.538, 0.0, 0.911, 0.0, 0.0, 1.0]]

    m = [[0.494, 0.692, 0.0, 0.0, 0.0, 1.0, 0.0], [0.494, 0.692, 0.0, 0.0, 0.0, 1.0, 0.0], [0.494, 0.692, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.692, 0.0, 0.0, 0.0, 1.0, 0.5], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.692, 0.076, 0.0, 0.0, 1.0, 0.5], [0.0, 0.692, 0.076, 0.0, 0.0, 1.0, 0.5], [0.117, 0.461, 0.179, 0.466, 0.0, 0.75, 0.0], [0.0, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.152, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.152, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.256, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.256, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.256, 0.508, 0.0, 0.75, 0.5], [0.0, 0.692, 0.256, 0.508, 0.0, 0.75, 0.5], [0.117, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.4, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.46, 0.692, 0.205, 0.448, 0.0, 0.75, 0.5], [0.521, 0.692, 0.205, 0.448, 0.0, 0.75, 0.5], [0.521, 0.692, 0.205, 0.448, 0.0, 0.75, 0.5], [0.521, 0.692, 0.205, 0.448, 0.0, 0.75, 0.5], [0.553, 0.692, 0.0, 0.508, 0.0, 0.75, 0.5], [0.546, 0.692, 0.0, 0.574, 0.0, 0.75, 0.5], [0.713, 0.692, 0.0, 0.334, 0.0, 0.75, 0.5], [0.713, 0.692, 0.0, 0.334, 0.0, 0.75, 0.5], [0.577, 0.692, 0.0, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.404, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.404, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.499, 0.692, 0.0, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.561, 0.692, 0.0, 0.479, 0.951, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.577, 0.692, 0.0, 0.508, 0.954, 0.0, 0.5], [0.3, 0.923, 0.205, 0.447, 0.954, 0.0, 0.5], [0.3, 0.923, 0.205, 0.447, 0.954, 0.0, 0.5], [0.3, 0.923, 0.205, 0.447, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.478, 0.692, 0.205, 0.479, 0.951, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.478, 0.692, 0.205, 0.479, 0.951, 0.0, 0.5], [0.481, 0.692, 0.205, 0.26, 0.951, 0.0, 1.0], [0.481, 0.692, 0.205, 0.26, 0.951, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 0.5], [0.493, 0.692, 0.205, 0.448, 0.954, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.545, 0.769, 0.205, 0.495, 0.954, 0.0, 0.5], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.545, 0.769, 0.205, 0.494, 0.954, 0.0, 0.5], [0.478, 0.769, 0.205, 0.495, 0.954, 0.0, 0.5], [0.38, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.478, 0.692, 0.205, 0.479, 0.951, 0.0, 0.5], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.605, 0.692, 0.205, 0.374, 0.985, 0.0, 1.0], [0.605, 0.692, 0.205, 0.374, 0.985, 0.0, 0.5], [0.605, 0.692, 0.205, 0.374, 0.985, 0.0, 0.5], [0.545, 0.769, 0.205, 0.494, 0.953, 0.0, 0.5], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.605, 0.692, 0.205, 0.374, 0.985, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.951, 0.0, 1.0], [0.479, 0.692, 0.205, 0.531, 0.95, 0.0, 1.0], [0.509, 0.692, 0.205, 0.551, 0.954, 0.0, 0.5], [0.545, 0.769, 0.0, 0.561, 0.953, 0.0, 0.5], [0.525, 0.769, 0.0, 0.428, 0.985, 0.0, 1.0], [0.642, 0.769, 0.0, 0.494, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.494, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.625, 0.769, 0.0, 0.532, 0.95, 0.0, 1.0], [0.625, 0.769, 0.0, 0.532, 0.95, 0.0, 1.0], [0.689, 0.461, 0.205, 0.494, 0.953, 0.0, 0.5], [0.54, 0.615, 0.0, 0.606, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.518, 0.615, 0.0, 0.606, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.6, 0.307, 0.0, 0.792, 0.954, 0.0, 1.0], [0.545, 0.769, 0.205, 0.495, 0.953, 0.0, 0.5], [0.662, 0.769, 0.205, 0.247, 0.983, 0.0, 0.5], [0.538, 0.769, 0.205, 0.578, 0.953, 0.0, 1.0], [0.538, 0.769, 0.205, 0.578, 0.953, 0.0, 1.0], [0.726, 0.769, 0.0, 0.522, 0.981, 0.25, 1.0], [0.726, 0.769, 0.0, 0.522, 0.981, 0.25, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.625, 0.769, 0.0, 0.602, 0.978, 0.25, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.953, 0.0, 1.0], [0.725, 0.769, 0.0, 0.522, 0.981, 0.25, 1.0], [0.625, 0.769, 0.0, 0.602, 0.978, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.642, 0.769, 0.0, 0.561, 0.954, 0.0, 1.0], [0.625, 0.769, 0.0, 0.602, 0.977, 0.25, 1.0], [0.625, 0.769, 0.0, 0.602, 0.977, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.635, 0.769, 0.0, 0.628, 0.954, 0.0, 1.0], [0.818, 0.769, 0.0, 0.521, 0.985, 0.25, 1.0], [0.818, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.642, 0.923, 0.0, 0.433, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.982, 0.75, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.982, 0.75, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.982, 0.75, 1.0], [0.818, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.75, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.818, 0.769, 0.0, 0.521, 0.985, 0.25, 1.0], [0.736, 0.769, 0.0, 0.521, 0.982, 0.75, 1.0], [0.818, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.818, 0.769, 0.0, 0.521, 0.983, 0.25, 1.0], [0.708, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.706, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.708, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.708, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.708, 0.692, 0.0, 0.577, 0.983, 0.75, 1.0], [0.622, 0.692, 0.0, 0.574, 0.982, 0.75, 1.0], [0.688, 0.692, 0.0, 0.596, 0.982, 0.75, 1.0], [0.677, 0.692, 0.0, 0.601, 0.983, 0.75, 1.0], [0.694, 0.538, 0.0, 0.686, 0.982, 0.75, 1.0], [0.694, 0.538, 0.0, 0.686, 0.982, 0.75, 1.0], [0.764, 0.846, 0.0, 0.401, 0.983, 0.75, 1.0], [0.764, 0.846, 0.0, 0.401, 0.983, 0.75, 1.0], [0.646, 0.923, 0.0, 0.433, 0.983, 0.75, 1.0], [0.685, 0.846, 0.0, 0.433, 0.983, 0.75, 1.0], [0.587, 0.923, 0.0, 0.599, 0.983, 0.75, 1.0], [0.573, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.609, 0.692, 0.0, 1.0, 0.987, 0.75, 1.0], [0.609, 0.692, 0.0, 1.0, 0.987, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.609, 0.692, 0.0, 1.0, 0.987, 0.75, 1.0], [0.587, 0.846, 0.0, 0.882, 0.983, 0.75, 1.0], [0.573, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.776, 0.769, 0.0, 0.51, 0.998, 0.75, 1.0], [0.573, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.609, 0.692, 0.0, 1.0, 0.987, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.588, 0.846, 0.0, 0.882, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.736, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.736, 0.769, 0.0, 0.882, 0.982, 0.75, 1.0], [0.736, 0.769, 0.0, 0.882, 0.982, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.573, 0.692, 0.0, 1.0, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.69, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.69, 0.692, 0.0, 1.0, 0.983, 0.75, 0.5], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.736, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.73, 0.615, 0.0, 1.0, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.982, 1.0, 1.0], [0.73, 0.538, 0.0, 1.0, 0.985, 0.75, 1.0], [0.69, 0.692, 0.0, 1.0, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.73, 0.538, 0.0, 1.0, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.882, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.707, 0.846, 0.0, 0.882, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.586, 0.846, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.763, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.763, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.763, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.763, 0.769, 0.0, 0.967, 0.985, 0.75, 0.5], [0.771, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.771, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.706, 0.846, 0.0, 0.967, 0.985, 0.75, 1.0], [0.706, 0.846, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.706, 0.846, 0.0, 0.967, 0.982, 0.75, 1.0], [0.706, 0.846, 0.0, 0.967, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 0.5], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 0.5], [0.707, 0.846, 0.0, 0.967, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.605, 0.846, 0.282, 0.967, 0.983, 0.75, 0.5], [0.666, 0.769, 0.282, 0.967, 0.983, 0.75, 0.5], [0.704, 0.769, 0.153, 0.967, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.769, 0.282, 0.967, 0.983, 0.75, 0.5], [0.677, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.677, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.677, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.588, 0.846, 0.256, 0.796, 0.985, 0.75, 1.0], [0.727, 0.846, 0.256, 0.796, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.737, 0.846, 0.384, 0.812, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.812, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.737, 0.846, 0.41, 0.818, 0.983, 0.75, 1.0], [0.8, 0.846, 0.41, 0.818, 0.985, 0.75, 1.0], [0.8, 0.846, 0.41, 0.818, 0.985, 0.75, 1.0], [0.737, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.807, 0.769, 0.256, 0.821, 0.983, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.682, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.737, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.682, 0.769, 0.256, 0.821, 0.983, 0.75, 1.0], [0.737, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.682, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.682, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.812, 0.769, 0.256, 0.821, 0.985, 0.75, 1.0], [0.812, 0.769, 0.256, 0.821, 0.983, 0.75, 1.0], [0.774, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.774, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.985, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.983, 0.75, 1.0], [0.896, 0.769, 0.051, 0.967, 0.983, 0.75, 1.0], [0.896, 0.769, 0.051, 0.967, 0.983, 0.75, 1.0], [0.896, 0.769, 0.051, 0.967, 0.983, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.737, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.983, 0.75, 1.0], [0.8, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.634, 0.846, 0.358, 0.821, 0.983, 0.75, 1.0], [0.825, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.74, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.742, 0.846, 0.282, 0.821, 0.983, 0.75, 1.0], [0.742, 0.846, 0.282, 0.821, 0.983, 0.75, 1.0], [0.667, 0.923, 0.282, 0.814, 0.985, 0.75, 0.5], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.85, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.71, 0.923, 0.256, 0.821, 0.983, 0.75, 1.0], [0.822, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.831, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.71, 0.923, 0.256, 0.821, 0.983, 0.75, 1.0], [0.85, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.776, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.79, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.723, 0.923, 0.256, 0.821, 0.983, 0.75, 1.0], [0.841, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.836, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.831, 0.615, 0.256, 0.821, 0.983, 0.75, 1.0], [0.79, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.79, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.666, 0.846, 0.256, 0.821, 0.985, 0.75, 1.0], [0.841, 0.846, 0.256, 0.821, 0.982, 0.75, 1.0], [0.836, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.836, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.831, 0.615, 0.256, 0.821, 0.983, 0.75, 1.0], [0.822, 0.846, 0.256, 0.821, 0.983, 0.75, 1.0], [0.836, 0.615, 0.256, 0.821, 0.985, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.853, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.843, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.853, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.538, 0.282, 0.967, 0.985, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.703, 0.538, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.666, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.853, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.713, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.713, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.864, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.843, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.634, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0], [0.634, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0], [0.737, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.737, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.983, 0.75, 0.5], [0.634, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.824, 0.615, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.982, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.834, 0.615, 0.282, 0.967, 0.982, 0.75, 1.0], [0.958, 0.615, 0.0, 0.967, 0.983, 0.75, 1.0], [0.951, 0.769, 0.0, 0.967, 0.985, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.953, 0.538, 0.0, 0.967, 0.983, 0.75, 1.0], [0.958, 0.538, 0.0, 0.967, 0.982, 0.75, 1.0], [0.958, 0.538, 0.0, 0.967, 0.985, 0.75, 1.0], [0.93, 0.769, 0.051, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.93, 0.769, 0.051, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.957, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.951, 0.769, 0.0, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.958, 0.769, 0.0, 0.967, 0.982, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.802, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.634, 0.769, 0.384, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.834, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.824, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.816, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.615, 0.282, 0.967, 0.983, 0.75, 1.0], [0.823, 0.769, 0.282, 0.967, 0.983, 0.75, 1.0], [0.819, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.819, 0.769, 0.282, 0.967, 0.985, 0.75, 1.0], [0.861, 0.769, 0.282, 0.883, 0.985, 0.75, 1.0], [0.653, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0], [0.831, 0.769, 0.282, 0.967, 0.982, 0.75, 1.0], [0.7, 0.769, 0.307, 0.967, 0.983, 0.75, 1.0], [0.7, 0.769, 0.307, 0.967, 0.983, 0.75, 1.0], [0.653, 0.769, 0.384, 0.967, 0.983, 0.75, 1.0], [0.818, 0.769, 0.076, 0.967, 0.983, 0.75, 1.0], [0.634, 0.769, 0.384, 0.967, 0.985, 0.75, 1.0]]

    a = np.array(m)
    np.set_printoptions(precision=3)
    d = [a[:,0], a[:,1], a[:,2], a[:,3], a[:,4], a[:,5], a[:,6]]

    for item in d:
        data = item
        plt.plot(data)

    plt.title("DR per class over generations")
    plt.axis([0, 499, -0.1, 1.1])
    plt.show()
