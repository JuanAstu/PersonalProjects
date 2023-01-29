# Importing packages and libraries

import pandas as pd
import pytesseract
import PIL.Image
import cv2
import os
import pdf2image
import matplotlib.pyplot as plt
from pdf2image import convert_from_path

# Store Pdf with convert_from_path function

images = convert_from_path('Lista_precios_oct.pdf', poppler_path = r"C:\Users\Raul\Desktop\Python Training\Lista a excel\poppler-23.01.0\Library\bin")
for i in range(len(images)):
      # Save as JPG Images the pages in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')


# We now face the first problem: the words and numbers are not zoomed in enough, so the image-to-text 
# algorithm does not do a good job, and most of the products and prices got "translated" incorrectly.

# To solve that, I thought that as the prices lists are always the same, the program could cut each individual
# column, leaving the blank spaces behind, and then resize them so the words and numbers get bigger and therefore more clear.

page1 = cv2.imread('page1.jpg', 1)
page1_resized = cv2.resize(page1, (1200,1400))
page2 = cv2.imread('page2.jpg', 1)
page2_resized = cv2.resize(page2, (1200,1400))
page3 = cv2.imread('page3.jpg', 1)
page3_resized = cv2.resize(page3, (1200,1400))
page4 = cv2.imread('page4.jpg', 1)
page4_resized = cv2.resize(page4, (1200,1400))

#Cutting and saving page 1 products table

productos1_y1 = 184
productos1_y2 = 1000
productos1_x1 = 187
productos1_x2 = 540

productos1_img = page1_resized[productos1_y1:productos1_y2, productos1_x1:productos1_x2]
cv2.imwrite('Recortes\\productos1.jpg', productos1_img)

#Cutting and saving page 1 presentations table

presentaciones1_y1 = 184
presentaciones1_y2 = 1000
presentaciones1_x1 = 670
presentaciones1_x2 = 865

presentaciones1_img = page1_resized[presentaciones1_y1:presentaciones1_y2, presentaciones1_x1:presentaciones1_x2]
cv2.imwrite('Recortes\\presentaciones1.jpg', presentaciones1_img)

#Cutting and saving page 1 prices table

precios1_y1 = 184
precios1_y2 = 1000
precios1_x1 = 1000
precios1_x2 = 1130

precios1_img = page1_resized[precios1_y1:precios1_y2, precios1_x1:precios1_x2]
cv2.imwrite('Recortes\\precios1.jpg', precios1_img)

#Products page 2

productos2_y1 = 184
productos2_y2 = 1000
productos2_x1 = 187
productos2_x2 = 470

productos2_img = page2_resized[productos2_y1:productos2_y2, productos2_x1:productos2_x2]
cv2.imwrite('Recortes\\productos2.jpg', productos2_img)

#Presentations page 2

presentaciones2_y1 = 184
presentaciones2_y2 = 1000
presentaciones2_x1 = 675
presentaciones2_x2 = 875

presentaciones2_img = page2_resized[presentaciones2_y1:presentaciones2_y2, presentaciones2_x1:presentaciones2_x2]
cv2.imwrite('Recortes\\presentaciones2.jpg', presentaciones2_img)

#Prices page 2

precios2_y1 = 184
precios2_y2 = 1000
precios2_x1 = 1000
precios2_x2 = 1130

precios2_img = page2_resized[precios2_y1:precios2_y2, precios2_x1:precios2_x2]
cv2.imwrite('Recortes\\precios2.jpg', precios2_img)

#Products page 3

productos3_y1 = 180
productos3_y2 = 1000
productos3_x1 = 187
productos3_x2 = 540

productos3_img = page3_resized[productos3_y1:productos3_y2, productos3_x1:productos3_x2]
cv2.imwrite('Recortes\\productos3.jpg', productos3_img)

#Presentations page 3

presentaciones3_y1 = 175
presentaciones3_y2 = 1000
presentaciones3_x1 = 650
presentaciones3_x2 = 875

presentaciones3_img = page3_resized[presentaciones3_y1:presentaciones3_y2, presentaciones3_x1:presentaciones3_x2]
cv2.imwrite('Recortes\\presentaciones3.jpg', presentaciones3_img)

#Prices page 3

precios3_y1 = 175
precios3_y2 = 1000
precios3_x1 = 900
precios3_x2 = 1130

precios3_img = page3_resized[precios3_y1:precios3_y2, precios3_x1:precios3_x2]
cv2.imwrite('Recortes\\precios3.jpg', precios3_img)

#Products page 4
productos4_img = page4_resized[productos1_y1:productos1_y2, productos1_x1:productos1_x2]
cv2.imwrite('Recortes\\productos4.jpg', productos4_img)

#Presentations page 4
presentaciones4_img = page4_resized[presentaciones3_y1:presentaciones3_y2, presentaciones3_x1:presentaciones3_x2]
cv2.imwrite('Recortes\\presentaciones4.jpg', presentaciones4_img)

#Prices page 4
precios4_img = page4_resized[precios3_y1:precios3_y2, precios3_x1:precios3_x2]
cv2.imwrite('Recortes\\precios4.jpg', precios4_img)

#Pytesseract algorithm config

myconfig = r"--psm 6 --oem 3"
products = []
presentations = []
all_prices = []

# Image to string function

for file in os.listdir("Recortes"):
    file_name = "Recortes\\" + file
    if "productos" in file_name:
        products.append(pytesseract.image_to_string(PIL.Image.open(file_name), config=myconfig))
    if "presentaciones" in file_name:
        presentations.append(pytesseract.image_to_string(PIL.Image.open(file_name), config=myconfig))
    if "precios" in file_name:
        all_prices.append(pytesseract.image_to_string(PIL.Image.open(file_name), config=myconfig))


# The text in the images didn't get translated 100% accurately, so I wrote the following code to transform the data correctly

raw_products_list = products[0].split("\n") + products[1].split("\n") + products[2].split("\n") + products[3].split("\n")
raw_presentations_list = presentations[0].split("\n") + presentations[1].split("\n") + presentations[2].split("\n") + presentations[3].split("\n")

# Cleaning products names list

# Eliminates capitalized words, since they didn't belong to products names

def product_isupper(word):
    count = 0
    for i in range(len((word))-2):
        if word[i].isupper() and word[(i+1)].isupper() and word[(i+2)].isupper():
            count += 1
    return count > 0

# Clean "false" products from the list

def remove_wrong_products(original_list):
    for product in original_list[:]:
        if ("!" in product) or ("Producto" in product) or (len(product) <= 2) or product_isupper(product):
            original_list.remove(product)
    return original_list

clean_products_list = remove_wrong_products(raw_products_list)


# Cleaning presentations list

def remove_wrong_presentations(original_list):
    clean_presentations_list = []
    for presentation in original_list:
        if ("x" in presentation) or ("de" in presentation) or ("por" in presentation) or ("tratamientos" in presentation):
            clean_presentations_list.append(presentation)
    return clean_presentations_list

clean_presentations_list = remove_wrong_presentations(raw_presentations_list)


# The prices table from page 3 is analyzed separatedly from the others because it contains two prices,
# by dosis and by flasks (AKA "fcos")

# Image to string
raw_prices3_list = pytesseract.image_to_string(PIL.Image.open("Recortes\precios3.jpg"), config=myconfig).split("\n")

# Split prices by "$"
raw_split_prices3_list = []
for prices in raw_prices3_list:
    split_pirces = prices.split("$")
    raw_split_prices3_list.append(split_pirces[1:])

# Transforming the prices so they are presented in a traditional format
clean_prices3_list = []
for raw_pair_list in raw_split_prices3_list:
    float_clean_pair_list = []    
    clean_prices3_list.append(float_clean_pair_list)
    for str_price in raw_pair_list:         
        if "—" in str_price:
            str_price = str_price.replace("—", "")          
        str_price = str_price.replace(" ", "")
        str_price = str_price.replace(",", "")
        str_price = str_price.replace(".", "")
        str_price = str_price[:-2] + "." + str_price[-2:]
        str_price = str_price.strip()
        float_price = float(str_price)
        float_clean_pair_list.append(float_price)

clean_prices3_list = clean_prices3_list[:-1]

# list containing the dosis prices
dosis_price = []
# list containing the flasks prices from page 3
fcos_price3 = []

for dosis_fcos_prices_list in clean_prices3_list:
    dosis_price.append(dosis_fcos_prices_list[0])
    fcos_price3.append(dosis_fcos_prices_list[1])

# The dosis price list only contains 23 elements, where the product were 76 in total. So we have to fill
# the dosis list with NaN values so then it can match the lengths of the rest of the columns.
top_emptys = [None] * 41
bottom_emptys = [None] * 12
dosis_price = top_emptys + dosis_price + bottom_emptys


# Cleaning and transforming the prices from the pages 1, 2 and 4

raw_prices_complete = []

for page in all_prices:
    raw_prices_complete.append(page.split("\n"))

prices124 = raw_prices_complete[0] + raw_prices_complete[1] + raw_prices_complete[3]
prices124_clean = []

# Transforming the prices so they are presented in a traditional format
for price in prices124:
    if "§" in price:
        price = price.replace("§", "$")
    price = price.replace(",", "")
    price = price.replace(".", "")
    price = price[:-2] + "." + price[-2:]
    if "$" in price:
        price = price.replace("$", "")
        price = price.replace(" ", "")
        prices124_clean.append(price)

# Creating the list with the prices formatted correctly
prices124_clean_float = []
for str_price in prices124_clean:
    prices124_clean_float.append(float(str_price))

# Adding in between the page 3 prices
fcos_price = prices124_clean_float[:41] + fcos_price3 + prices124_clean_float[41:]

# Putting all the information together in a dictionary
complete_list_dict = {"Productos": clean_products_list,
                      "Presentación": clean_presentations_list,
                      "Precio por Dosis": dosis_price,
                      "Precio": fcos_price}

# Transforming that dict in a Pandas Dataframe so then it can be exported as an Excel file
complete_list_df = pd.DataFrame(complete_list_dict)
complete_list_df.to_excel("Lista de Precios.xlsx")

