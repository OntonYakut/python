#!/usr/local/bin/python3

def Ask(question):
	response=None
	while response not in ('y', 'n'):
	    response = input(question).lower()
	return response

answer=Ask("\nEnter please 'y' or 'n': ")
print("Thanks for enter", answer)
input("\n\nPress Enter to quit.")


 
