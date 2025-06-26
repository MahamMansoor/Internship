# Task: Working with Lists, Split/Join, and Tuples

#  Take sentence input from the user
sentence = input("Hi ! Enter a sentence: ")

# Split the sentence into a list of words
words_list = sentence.split()
print("List of words:", words_list)

# Join the list back into a sentence using ' - ' separator
joined_sentence = ' - '.join(words_list)
print("Joined the sentence with dashes:", joined_sentence)

#  Store first and last name in a tuple
name = ("Maham", "Mansoor")  
print("First Name:", name[0])
print("Last Name:", name[1])
