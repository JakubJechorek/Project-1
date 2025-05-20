#Prompt to gather required info:

recipient_name = input("Enter the recipient's name: ")
year_of_birth = int(input("Enter the recipient's birth year: "))
personal_message = input("Enter a short personalized message: ")
sender_name = input("Enter Senders Name: ")

#calculations to generate response:
current_year = 2025
age = current_year - year_of_birth

print(f"{recipient_name}, let's celebrate your {age} years of awesomeness!\n\nWishing you a day filled with joy and laughter as you turn {age}!\n\n{personal_message}\n\n{sender_name}")