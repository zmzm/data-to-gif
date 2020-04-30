import pandas as pd
import matplotlib.pyplot as plt
import glob
import moviepy.editor as mpy

df = pd.read_csv('regions.csv', parse_dates=['date'])

# df.date= pd.to_datetime(df.date)
# df.set_index('date', inplace=True)
# df = df.drop(columns=['fips', 'deaths'])
df = df.pivot(index = 'date', columns = 'state', values = 'cases')
print(df)

df = df.reset_index()
df = df.reset_index(drop=True)
df = df.drop(columns = 'date')



gif_name = 'COVID'
fps = 3
file_list = glob.glob('pngs/*')
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)