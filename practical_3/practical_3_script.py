# Provided inputs (use these)
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Globals to observe name masking (same-name local variables hides the global variable so use different variable names inside the function). Do not rename these.
count = 999
summary = "unset"
result = "unset"

#3.1
def add_two_numbers(num_one, num_two):
    number_to_return = num_one + num_two #Funktionen kommer ta första och andra argumentet i () och addera. Retuner säger att det är summan som vi vill få tillbaka
    return number_to_return

my_added_numbers = add_two_numbers(1,1) #ALternativ 1, assignar en funktionen till en variabel som sedan printas
print(my_added_numbers)
print(add_two_numbers(1,1)) #Alternativ 2, printar summan av mina siffror direkt från funktionen
    
#4.1
def count_above(seq,lim):
    count = 0

    for num in seq:
        if num > lim:
            count+=1
    return count

print(count) #Global count - kommer inte ändras av count_above
print(count_above(nums,7)) #Sätter nums som sekvensen som ska tittas igenom och 7 som limit - kommer ge antalet nummer som är över limit (7)
print(count)

#4.2
def summarize_text(s):
    summary = {"digits":0, "letters":0, "other":0}
    digit_count = 0
    letter_count = 0
    other_count = 0

    for char in s:
        if char.isdigit():
            digit_count+=1
            summary["digits"] = digit_count
        elif char.isalpha(): #isalpha() kollar ifall char är en bokstav
            letter_count+=1
            summary["letters"] = letter_count
        else:
            other_count+=1
            summary["other"] = other_count
    return summary

print(text)
print(summarize_text(text))

def aggregate(seq,mode,threshold):
    if mode is "sum":
        result = 0
    elif mode is "count":
        result = 0
    else:
        result = None
    
    for n in seq:
        if n > threshold: #Om nummret i sekvensen är över threshold (4 i detta fall) så ska den fortsätta
            if mode is "sum":
                result += n #Ger summan av alla n
            elif mode is "count":
                result+=1 #Kommer räkna hur många n som är över threshold
            else:
                result = n #Ger det högsta n i sekvensen
    
    return result

print(result)
print(aggregate(nums, "sum", limit))
print(aggregate(nums, "count", limit))
print(aggregate(nums, "max", limit))
print(result)

