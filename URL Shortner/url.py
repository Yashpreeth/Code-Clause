import pyshorteners

# Taking the user input here

url=input("Enter the URL : ") 

#using the pyshortners library
type_tiny = pyshorteners.Shortener()

url_shortner = type_tiny.tinyurl.short(url)


print("*"* 30)

# printing the final output

print("After Shortened the URL is: " + url_shortner)
