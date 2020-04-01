print("Hello there! Welcome to COVID-19 checker. I would like to ask you some questions before assessing your risk level. Let's begin")

print("Enter 1 for YES and 0 for NO")

cough = int(input("Do you have cough? ")) * 1
colds = int(input("Do you have colds? ")) * 1
diarrhea = int(input("Do you have diarrhea? ")) * 1
sore_throat = int(input("Do you have sore throat? ")) * 1
body_ache = int(input("Are you experiencing body ache? ")) * 1
headache = int(input("Do you have headache? ")) * 1
temperature_38 = int(input("Is your temperature above 37.8 C? ")) * 1
difficulty_breathing = int(input("Are you having difficulty breathing? ")) * 2
fatigue = int(input("Are you experiencing fatigue? ")) * 2 

print(difficulty_breathing)

total_score = cough + colds + diarrhea + sore_throat + body_ache + headache + difficulty_breathing + fatigue + temperature_38
print(total_score)

risk = abs(total_score - 1)/10
print(risk)
if(risk <= 0.3):
    print("You may have stress related issue. It would be better to observe and wait")
elif(risk <= 0.6):
    print("There is a chance you have dehydration. It would be advisable to hydrate properly and in case conditoins worsen, do seek consultation with a doctor")
elif(risk <= 0.8):
    print("It's advisable to consult a doctor asap")
else:
    print("Do a covid-19 check at a facility immediately")
