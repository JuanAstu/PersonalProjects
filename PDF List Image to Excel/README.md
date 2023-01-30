## Intro

Welcome to my first Image to Text Project:

Each month one of the biggest supplier of the company where I work for send us a list with all of their products and prices updated. The problem is that the list comes in images, inserted in a PDF file. The list contains + 75 products with different presentations and prices, and it would be very easy for us to have that information in excel files or SQL tables.

To transcribe manually the data every month is a repetitive and time consuming task so I decided to automate it using Python scripts. Here you will find the [code](https://github.com/astudillojuanm/Personal_Projects/blob/main/PDF%20List%20Image%20to%20Excel/PDF%20Image%20to%20Excel%20File.py) that I wrote to convert the PDF Image into an excel file and [another program](https://github.com/astudillojuanm/Personal_Projects/blob/main/PDF%20List%20Image%20to%20Excel/Coordinates%20App.py) used to find the coordinates where the images had to be cropped.

These were the libraries used in the code:
  - Pandas
  - Pytesseract
  - PIL.Image
  - cv2
  - OS
  - pdf2image
  
  The result was very positive, and now each time our supplier send us the updated list, any of the employees of the Purchasing Department can easily convert it to a manipulable table with just a few clicks.
