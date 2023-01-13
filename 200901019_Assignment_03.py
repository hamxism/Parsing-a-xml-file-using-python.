#200901019
#Muhammad Hamza Farooq
import csv    # couldn't figure out how to import library of xlsx. so I used csv instead.
import xml.etree.ElementTree as ET

tree = ET.parse('compiler.xml')
root = tree.getroot()

try:
    with open('200901019_Assignment_03.csv', 'w', newline='') as csvfile: #this will create the csv file in the folder with all the data of xml file.
        writer = csv.writer(csvfile)
        writer.writerow(['Book_Id', 'Author_Name', 'Title', 'Genre', 'Price', 'Publish_Date', 'Description'])

        for book in tree.findall('book'):
            Book_Id = book.get('id')
            Author_Name = book.find('author').text
            Title = book.find('title').text
            Genre = book.find('genre').text
            Price = book.find('price').text
            Publish_Date = book.find('publish_date').text
            Description = book.find('description').text
            writer.writerow([Book_Id, Author_Name, Title, Genre, Price, Publish_Date, Description])
except:
    print("Error! Please Try Again.")