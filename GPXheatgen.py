#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 22:29:24 2018

@author: daanwielens
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Read a GPX file and return the lat (y) and lon (x) coordinates as np arrays
def parseGPX(filename):
    x = np.array([])
    y = np.array([])
    with open(filename, 'r') as file:
        for line in file:
            if '<trkpt lat' in line:
                line = line.split('"')
                x = np.append(x, float(line[3]))
                y = np.append(y, float(line[1]))

    return x, y
                
# Plot GPX data
def plotGPX(x,y):
    plt.plot(x,y)

#------------------------------------------------------------------------------
# MAIN CODE
#------------------------------------------------------------------------------

#%% Get all GPX data
x_all = []
y_all = []
cwd = os.getcwd()
for filename in os.listdir(cwd):
    if filename.endswith('.gpx'):
        x,y = parseGPX(filename)
        x_all.append(x)
        y_all.append(y)

#%% Plot data - normal plot (black on white), alpha < 1
nData = len(x_all)
fig, ax = plt.subplots(figsize=(10, 10))
for i in range(len(x_all)):
    plt.plot(x_all[i], y_all[i], color='black', alpha=0.2)
ax.set_xticks([])
ax.set_yticks([])

# Remove 'figure border' without destroying ALL axis' parameters:
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

#%% Plot data - normal plot (black on white), alpha < 1
nData = len(x_all)
fig, ax = plt.subplots(figsize=(10, 10))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
for i in range(len(x_all)):
    plt.plot(x_all[i], y_all[i], color='white', alpha=0.2)
ax.set_xticks([])
ax.set_yticks([])

# Remove 'figure border' without destroying ALL axis' parameters:
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)