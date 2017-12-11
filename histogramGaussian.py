#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import sys
import seaborn as sns

sns.set(style="white", color_codes=True, font_scale=1.8)

def main():
  fig, ax = plt.subplots()
  ClickToDrawPoints(ax).show()

class ClickToDrawPoints(object):
    def __init__(self, ax):
      self.x = np.linspace(115, 135, 21)
      self.h = np.zeros(len(self.x))

      self.ax = ax
      self.fig = self.ax.figure
      self.lines = self.ax.step(self.x, self.h, linewidth=2, label='Histogram')
      self.fig.canvas.mpl_connect('button_press_event', self.on_click)
      self.ax.set_ylim([0, 20])
      self.ax.set_xlabel('Mass of four particles [GeV]', fontsize = 24)
      self.ax.set_ylabel('Count', fontsize = 24)
      plt.legend(loc='best', frameon=False)
      plt.tight_layout()
      plt.title('')

    def on_click(self, event):
      bkgOrGauss = np.random.uniform(0.0, 1.0)
      toy = 0
      if bkgOrGauss < 0.5: # do exponential
        toy = np.random.uniform(115, 135)
      else:
        toy = np.random.normal(125.0, 2.0)
      idx = np.digitize(toy, self.x)
      if idx >= len(self.h): idx = -1
      if idx < 0: idx = 0
      print "Mass: ", toy, " GeV"
      self.h[idx] += 1
      if event.inaxes is None:
          return
      plt.cla()
      self.lines = self.ax.step(self.x, self.h, linewidth=3, label='Histogram')
      #self.ax.set_ylim([0, 20])
      self.ax.set_xlabel('Mass of four particles [GeV]', fontsize = 24)
      self.ax.set_ylabel('Count', fontsize = 24)
      plt.legend(loc='best', frameon=False)
      #self.fig.canvas.blit(self.ax.bbox)
      plt.tight_layout()
      plt.title('')
      plt.draw()

    def show(self):
      plt.show()

main()
