from random import choice
my_dict={
'Andhra Pradesh':'Amaravati'
,'Arunachal Pradesh':'Itanagar'
,'Assam':'Dispur'
,'Bihar':'Patna'
,'Chhattisgarh'	:'Raipur'
,'Goa':	'Panaji'
,'Gujarat':'Gandhinagar'
,'Haryana':'Chandigarh'
,'Himachal Pradesh':	'Shimla'
,'Jharkhand':'Ranchi'
,'Karnataka':'Bengaluru'
,'Kerala':'Thiruvananthapuram'
,'Madhya Pradesh':	'Bhopal'
,'Maharashtra':	'Mumbai'
,'Manipur':'Imphal'
,'Meghalaya':	'Shillong'
,'Mizoram':'Aizawl'
,'Nagaland':'Kohima'
,'Odisha':'Bhubaneswar'
,'Punjab':'Chandigarh'
,'Rajasthan':'Jaipur'
,'Sikkim':'Gangtok'
,'Tamil Nadu':'Chennai'
,'Telangana':'Hyderabad'
,'Tripura':'Agartala'
,'Uttar Pradesh':'Lucknow'
,'Uttarakhand':'Dehradun'
,'West Bengal':'Kolkata' 
,'Andaman and Nicobar Islands':'Port Blair'
,'Chandigarh':'Chandigarh'
,'Dadra & Nagar Haveli and Daman & Diu':'Daman'
,'Delhi':'New Delhi'
,'Jammu and Kashmir':'Srinagar'
,'Lakshadweep':'Kavaratti'
,'Puducherry':'Pondicherry'
,'Ladakh':'Leh',
}


states=list(my_dict.keys())
while True:            #using while to play n number of times
	state=choice(states)
	capital=my_dict[state]
	capital_guess=input(f'what is the capital of { state} ?\n To quit ,type quit ')

	if capital_guess.lower()=='quit':
		break

	elif capital_guess == capital:
		print("Your answer is correct")
	else:
		print(f'your answer is wrong,\nthe capital of {state} is {capital}')
	
print("Quiz Completed\n \t Thank You for participating")