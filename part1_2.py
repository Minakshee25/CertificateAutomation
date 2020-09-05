from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

df = pd.read_csv('sample.csv')

font = ImageFont.truetype('arial.ttf',50)

for index,j in df.iterrows():
    img = Image.open('raw_certificate.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(280,280),text='{}'.format(j['name']),fill=(255,69,0),font=font)
    img.save('pictures/{}.jpg'.format(j['name']))