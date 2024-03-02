def random_even_odd():
    number = random.randint(1, 100)
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Call the function
random_even_odd()
