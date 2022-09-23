#!/usr/bin/env python3

"""The user will enter their birthday and their zodiac sign will be displayed with a description"""

# brought in the datetime library to help with formatting, input validation, and date comparison
import datetime
import shutil
import colorama

columns = shutil.get_terminal_size().columns

## create a dictionary containing all info about zodiac signs
# ascii art is from https://asciiart.website/index.php?art=religion/astrology
Zodiac = {
    "Aries" : {
        "ascii" : ["Aries -  The Ram\n",".-.   .-.", "(_  \ /  _)", "|", "|"],
        "description": "Independent and strong‒willed, you are a force to be reckoned with! You love nothing more than an exciting new goal to tackle, and you do your best work when you’re flying solo. Your passion and energy keep the rest of us on our toes!"
    },
     "Taurus": {
        "ascii": ["Taurus -  The Bull\n", ".     .","'.___.'", ".'   `.",  ":       :", ":       :", "`.___.'"],
        "description": "As a Taurus, you’re a wonderful combination of laid‒back and hard‒working. You’re honest and loyal, occasionally to a fault. Your determination and attention to detail will take you far in life. "
    },
     "Gemini": {
        "ascii": ["Gemini -  The Twins\n", "._____.", "| |", "| |", "_|_|_", "'     '"],
        "description": "Your ability to get along with a wide variety of people makes you a bit of a social butterfly, but you’ll take advantage of some alone time when it comes your way. Curious and deeply emotional, you love ritual and celebration."
    },
     "Cancer": {
        "ascii": ["Cancer -  The Crab\n", ".--.", " /   _`.", "(_) ( )", "'.    /  ", "`--' "],
        "description": "Your intuition is downright uncanny! You do your best socializing in small groups and prefer intimate relationships even if it means your social circle is on the smaller side. Your creative spirit will bring joy to all you meet."
    },
     "Leo": {
        "ascii": ["Leo -  The Lion\n", ".--.", "(    )",  "(_)  /  ","    (_," ],
        "description": "It’s no wonder your symbol is a lion. Your personality and presence are impressive to all. This may intimidate some, but your inviting spirit will help you easily make friends. Your confidence will be an asset to you throughout your life."
    },
     "Virgo": {
        "ascii": ["Virgo -  The Virgin\n", "_       ", "' `:--.--.", "     |  |  |_ ", "     |  |  | )", "    |  |  |/", "        (J"],
        "description": "You are the picture of poise and elegance. You love to stay organized and have a strong focus on keeping things aesthetic. But you’re not just beauty. You’ve got brains, too! You’ll continue seeking knowledge and intellectual growth as you age."
    },
     "Libra": {
        "ascii": ["Libra -  The Balance\n", "__", "___.'  '.___", "____________"],
        "description": "You have a large social circle, and your open‒mindedness helps you get along with just about anyone. But don’t get lost in the crowd! A focus on self‒care and personal reflection will help you build your confidence over time."
    },
     "Scorpio": {
        "ascii": ["Scorpius -  The Scorpion\n", "_       ", "' `:--.--.", "    |  |  |", "    |  |  |", "         |  |  |  ..,", "               `---':"],
        "description": "As a Scorpio, you can have a sharp edge, but this isn’t always a negative quality. It gives you an appreciation for authenticity and a strong sense of independence. However, you’re not always as tough as you appear. Once you let people into your life, you’re a bit of a softy."
    },
     "Sagittarius": {
        "ascii": ["Sagittarius -  The Archer\n", "      ...", "      .':", ".'", "`..'     ", ".'`.      "],
        "description": "The road less traveled is your favorite place to be! Your bravery is admirable and will make you a good fit for leadership roles. You also have a bit of an itch in your shoes and will always be ready to take on a new adventure."
    },
     "Aquarius": {
        "ascii": ["Aquarius -  The Water Bearer\n", ".-\"-._.-\"-._.-", ".-\"-._.-\"-._.-"],
        "description": "You may fall on the introvert side of the spectrum, but that doesn’t mean you don’t know how to have fun. You have an enviable combination of intelligence and intuition, and you are able to identify positive opportunities even in dark times."
    },
     "Pisces": {
        "ascii": ["Pisces -  The Fishes\n", "`-.    .-'", ":  :", "--:--:--", ":  :", ".-'    `-."],
        "description": "You wouldn’t hurt a fly! Empathy is your superpower, and you are an asset to any team you join or cause you support. Your gentleness is a virtue. However, be careful to not let your feelings get hurt too easily. Be sure to spend time building your self‒confidence."
    },
     "Capricorn": {
        "ascii": ["Capricorn -  The Goat\n", "        _", "\      /_)", "\    /`.", "  \  /   ;", "   \/ __.'"],
        "description": "Your perfectionism and high standards, though sometimes an obstacle, can be one of your superpowers when handled wisely. You have a strong sense of self, which enables you to make meaningful connections and lead the way."
    }
    
}

## check if the user entered a number, keeps asking for a new input until the input is a number
def check_valid_num(input_string):
    # ask for a new input whenever the input is not a digit
    while not input_string.isdigit():
        print(f"\n-----{input_string} is not a number. Please try again.-----")
        input_string = input("\t\t ---> \t")

    # turn the string to a number
    return int(input_string)


# asks the user to input their birth year month and day and checks the validity with check_valid_num and try except
def get_birthdate():
    # give instructions and get inputs for birthdate
    print("\n\nAnswer the following questions using NUMBERS ONLY: ")
    print("\n\t> What year were you born?")
    year = input("\t\t YEAR:\t")
    # check if the user entered a number
    year = check_valid_num(year)

    print("\n\t> What month were you born?")
    month = input("\t\t MONTH:\t")
    month = check_valid_num(month)

    print("\n\t> What day were you born?")
    day = input("\t\t DAY:\t")
    day = check_valid_num(day)

    # using a try/except for if the datetime.date returns an error
    try:
        date = datetime.date(year, month, day)
    # if datetime returns this particular error, notify the user and run entire function again for a  new date
    except ValueError:
        print("\n-----Invalid date format, try again.-----")
        date = get_birthdate()

    # return the formatted date for use in the main() function
    return date

## this function takes the users birthdate and compares them to date ranges to find the corresponding zodiac sign
#  zodiac information from: https://www.tenthousandvillages.com/mosaic/your-guide-to-the-12-zodiac-dates-traits/
def get_zodiac(date):
    year = date.year

    # conditional for which zodiac sign the user's birthday falls into
    # use function date_in_range to return a boolean checking if the birthdate is within the zodiac date range
    # display the zodiac sign and a description
    if date_in_range(datetime.date(year, 3, 21), datetime.date(year, 4, 19), date):
        zodiac_sign = "Aries"
        
    elif date_in_range(datetime.date(year, 4, 20), datetime.date(year, 5, 20), date):
        zodiac_sign = "Taurus"

    elif date_in_range(datetime.date(year, 5, 21), datetime.date(year, 6, 20), date):
        zodiac_sign = "Gemini"

    elif date_in_range(datetime.date(year, 6, 21), datetime.date(year, 7, 22), date):
        zodiac_sign = "Cancer"
       
    elif date_in_range(datetime.date(year, 7, 23), datetime.date(year, 8, 22), date):
        zodiac_sign = "Leo"

    elif date_in_range(datetime.date(year, 8, 23), datetime.date(year, 9, 22), date):
        zodiac_sign = "Virgo"
        
    elif date_in_range(datetime.date(year, 9, 23), datetime.date(year, 10, 22), date):
        zodiac_sign = "Libra"
        
    elif date_in_range(datetime.date(year, 10, 23), datetime.date(year, 11, 21), date):
        zodiac_sign = "Scorpio"
        
    elif date_in_range(datetime.date(year, 11, 22), datetime.date(year, 12, 21), date):
        zodiac_sign = "Sagittarius"
        
    elif date_in_range(datetime.date(year, 1, 20), datetime.date(year, 2, 18), date):
        zodiac_sign = "Aquarius"
        
    elif date_in_range(datetime.date(year, 2, 19), datetime.date(year, 3, 20), date):
        zodiac_sign = "Pisces"
        
    elif date_in_range(datetime.date(year, 1, 1), datetime.date(year, 1, 19), date) or date_in_range(datetime.date(year, 12, 22), datetime.date(year, 12, 31), date):
        zodiac_sign = "Capricorn"
    
    else:
        print("\n-----Hmmm... Something went wrong. Lets try this again!-----")
        main()
    zodiac_description = Zodiac[zodiac_sign]["description"]
    for ascii in Zodiac[zodiac_sign]["ascii"]:
        print(f"{ascii}".center(columns))

    # display the user's birthday
    print(f"\n\tYour birthday is {date.strftime('%B %d, %Y')}\n")
    print(f"\n\tYou’re a(n) {zodiac_sign}!\n")
    print(f"~ {zodiac_description} ~")


## function that checks if the birthdate entered is within a given range
def date_in_range(start, end, birthdate):
    return start <= birthdate <= end


## function for the main component in program
def main():
    # ask the user if they know what their zodiac sign is. store the response
    print("\nWould you like to learn about your Zodiac sign?")
    response = input("\t(Yes/No) ---> ")

    # check validity of the input ( did the user answer yes or no ) if no then run it again
    while response.lower() not in ["yes", "no"]:
        print(f"{response} is not a valid input. Please try again.")
        response = input("\t(Yes/No) ---> ")

    # if the user says no make a comment and end the program,
    if response.lower() == "no":
        print("\nOkay cool! Carry on with your day :)")
    else:
        # other wise ask the user for their birthdate and find their zodiac sign
        date = get_birthdate()
        get_zodiac(date)
    
    # signals the end of the program
    print("\n\nGoodbye!  UwU\n\n")


# run the main function
if __name__ == "__main__":
    main()