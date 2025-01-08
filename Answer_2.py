#     Create a non-return type function that takes the details of user like name,age, city, company, and profile and display  the message-
#     "Hello Python, I am name. I am age years old. I am a profile in company"

def intro():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    profile = input('Enter Your profile: ')
    company = input('Enter your company: ')
    print(f"Hello Python, I am {name}. I am {age} years old. I am a {profile} in {company}")

intro()


"""Output:
Enter your name: RAHUL
Enter your age: 35
Enter Your profile: Trainee
Enter your company: Console Flare
Hello Python, I am RAHUL. I am 35 years old. I am a Trainee in Console Flare"""