name = input("ENTER YOUR NAME HERE USER , LETS CHECK WHETHER YOU ARE A BEAST OR NOT : ")

print("WELCOME TO THE BEAST CHECKER," , '"'+ name + '"' , ", HERE THE REAL TEST BEGINS.")

age = int(input("ENTER YOUR AGE HERE : "))

if age>=18 and age<100:
    print("OK YOUNG MAN, SO YOU ARE " , '"' + str(age) + '"' , "YEARS OLD , NOW GET READY FOR THE REAL TESTS")
    
    gym = input("TELL ME WHETHER YOU HIT THE GYM OR YOU ARE SKINNY(YES/NO) : ")
    if gym == "YES":
        print("OHH I SEE , YOU HIT THE GYM , SO YOU MUST BE SHREDDED")

    
    
       
        protein_intake = int(input("OK, \"" + name + "\" , AS YOU HIT THE GYM , YOU MUST BE TAKING PROTEIN, TELL ME WHAT IS THE AMOUNT(in grams) : "))
        if protein_intake >150 and protein_intake<300:
            print("BROTHER , YOU ARE TRAINING TO BECOME A MONSTER , AND SOO YOU WILL BECOME AS YOUR PROTEIN INTAKE IS WHOPPING," , '"' + str(protein_intake) + '"' , "grams, KEEP IT UP")
        elif protein_intake >=120 and protein_intake<=150:
            print("THIS IS FINE TO MAINTAIN A FIT BODY BROTHER , KEEP GOING AND YOU CAN ALSO INCREASE AS YOUR PROTEIN IS IN GOOD RANGE")
        elif protein_intake <120 and protein_intake>=100:
            print("THIS IS BELOW AVERAGE BROTHER , TRY TO INCREASE IT BY 20 TO 30 GRAMS , IF POSSIBLE")
        elif protein_intake <100 and protein_intake>=70:
            print("THIS WILL NOT TAKE YOU ANYWHERE , TRY TO EAT MORE PROTEIN, YOU GOT THIS")
        else:
            print("GO WATCH CARTOONS, THIS PROTEIN GAME IS NOT FOR YOU AT ALL")
       
    else:
      print("GO HIT SOME GYM FIRST.")
elif age>=100:
    print("TOO OLD TO HIT GYM , AS YOU ARE," , '"' + str(age) + '"' ", YEARS OLD")
      
else:
    print("TOO YOUNG BOY , JUST WAIT FOR," , 18-age , "YEAR")
      
      
      
       

     
     
     
   