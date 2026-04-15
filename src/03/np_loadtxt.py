import datetime as dt
import numpy as np

with open("bonn.csv", "r") as f:

    percentage, time = np.loadtxt(f,
                                  delimiter=";",
                                  skiprows=1,
                                  comments="#",
                                  dtype={
                                      'names': ('percentage', 'time'),
                                      'formats': ('i4', 'M8[m]')},
                                  converters={
                                      0: lambda i: i if i != b'None' else -10,
                                      1: lambda t: dt.datetime.fromtimestamp(float(t))},
                                  usecols=(0, 1),
                                  unpack=True
                                  )

np.set_printoptions(threshold=np.inf)

print(percentage)
print(percentage.shape)

print(time)
print(time.shape)
