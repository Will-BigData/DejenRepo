'''
1) Create a Python program to output the following basic JSON notation.
Output:
{
"donut_name":"Vanilla Donut",
"quantity_purchased":"10",
"price":2.5
} 
'''
# Solution
json_data = '''{
    "donut_name":"Vanilla Donut",
    "quantity_purchased":"10",
    "price":2.5
}'''
print(json_data)




'''
2)Create a Python program to prompt customers for their name and age. The format for the name and age labels should be in bold. And, the name literal should be underlined.
'''
# Answere
from termcolor import colored
def main():
    name = input("Enter your name: ")
    age = input("enter your age:")
    print(colored(name, attrs=['bold', 'underline']))

    print(colored(age, attrs=['bold']))

if __name__ == "__main__":
    main()



'''
3)Create a Python program to find the 8th character in the String: "http://allaboutscala".
'''
# Solution

str = "http://allaboutscala"
print(str[7])




'''4)Create a Python program to calculate the total cost for a customer who is buying 10 Glazed donuts. You can assume that the price of each Glazed donut item is at $2.50. Notice the format of the $25.00 total cost literal, which is essentially at 2 decimal places
'''
# Solution
quantity = 10
price = 2.5 
total_cost = quantity * price
print(f"${total_cost:.2f}")



'''5)Create a Python program that will ask the following question to a customer: "What is your favorite movie of all times?".
'''
# Solution
movie = input("What is your favorite movie of all times?")
print(movie)


'''6)Create a Python program to output your name and favorite movie.
Output:
First Name: Nadim
Last Name: Bahadoor
Favorite Movie: The Matrix'''


# Solution
FirstName = "Dejen"
LastName = "Tesfa"
FavoriteMovie = "Shooter"
print(f"First Name: {FirstName}")
print(f"Last Name: {LastName}")
print(f"Favorite Movie: {FavoriteMovie}")
