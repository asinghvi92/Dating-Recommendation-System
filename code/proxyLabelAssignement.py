import re 

def proxyLabelAssignement(UserX= None,UserY= None):
    if UserX is None or UserY is None:
        print("Missing arguments, might wanna check. ")
        #print(" \
            #input: UserX, UserY dictionary as created from parser func \n \
            #output: compatibility score \n \
            #function: assign score purely on the basis of pets preference \n \
            #---------------------------Assumption------------------- \n \
            #Orientatin and language based filtering is already done \n \
            #-------------------------------------------------------------")
        return 0
    score1= petscore(UserX['pets'], UserY['pets'])
    score2= zodiacscore(UserX['sign'], UserY['sign'])
    score= (float)(score1/2.0)*0.6 + (float)(score2/7.0)*0.4
    return score

def zodiacscore(UserX, UserY):
    if UserX is None or UserY is None:
        print("Missing arguments, please check. ")
        print(" \
            #input: UserX, UserY dictionary as created from parser func \n \
            #output: compatibility score \n \
            #function: assign score purely on the basis of pets preference \n \
            #---------------------------Assumption------------------- \n \
            #Orientatin and language based filtering is already done \n \
            #-------------------------------------------------------------")
        return 0
        weight = 8 
        
 
    zodiac = {'aquarius': 1, 'pisces': 2, 'aries': 3,
	'taurus': 4, 'gemini': 5, 'cancer': 6, 'leo': 7,
	'virgo': 8, 'libra': 9, 'scorpio': 10, 
	'sagittarius': 11, 'capricorn': 12}	

    zodiacComp = {'aquarius': ['leo', 'sagittarius'], 'pisces': ['virgo', 'taurus'], 'aries': ['libra','leo'],
	'taurus': ['scorpio','cancer'], 'gemini': ['sagittarius','aquarius'], 'cancer': ['capricorn','taurus'], 'leo': ['aquarius','gemini'],
	'virgo': ['pisces','cancer'], 'libra': ['aries','sagittarius'], 'scorpio': ['taurus','cancer'], 
	'sagittarius': ['gemini','aries'], 'capricorn': ['virgo','cancer']}
    x,y= UserX, UserY
    if x not in zodiacComp or y not in zodiacComp:
        return 0
    if y in zodiacComp[x]:
		weight = 1
    else:
		val_x = zodiac[x]
		val_y = zodiac[y]
		weight = min(abs(val_x-val_y), abs(val_y-val_x)+12) + 1 
    return (8-weight)
    #------------- returns between 0 to 7 inclusive [0,7]
    
    
def petscore(UserX= None, UserY= None):
    if UserX is None or UserY is None:
        return 0 
    
    cat_review_X, cat_review_Y, dog_review_X, dog_review_Y= None, None, None, None 
    #---------------------------------------------------------------------------------------
    #extracting review 
    temp_X = UserX.split("and")
    for ele in temp_X:
        if re.search("cat",ele):
            cat_review_X= ele
        elif re.search("dogs",ele):
            dog_review_X= ele 
    
    
    temp_Y = UserY.split("and")
    for ele in temp_Y:
        if re.search("cat",ele):
            cat_review_Y= ele
        elif re.search("dogs",ele):
            dog_review_Y= ele 

    #-----------------------------------------------------------------------------------------
    #finding sentiment from review 
    cat_sentiment_X, cat_sentiment_Y, dog_sentiment_X, dog_sentiment_Y= 0,0,0,0
    #-1: dislike | 0: neutral | 1:like 
    if cat_review_X:
        if re.search("dislike",cat_review_X):
            cat_sentiment_X= -1 
        else:
            cat_sentiment_X= 1 
    if cat_review_Y:
        if re.search("dislike",cat_review_Y):
            cat_sentiment_Y= -1 
        else:
            cat_sentiment_Y= 1 
    if dog_review_X:
        if re.search("dislike",dog_review_X):
            dog_sentiment_X= -1 
        else:
            dog_sentiment_X= 1 
    if dog_review_Y:
        if re.search("dislike",dog_review_Y):
            dog_sentiment_Y= -1 
        else:
            dog_sentiment_Y= 1 
    
    #-----------------------------------------------------------------------------------------       
    #computing cat and dog matching scores  
    #TODO: make it complex: dont give zero score to "unknwon" and "likes cats"
    cat_score= 1 if cat_sentiment_X==cat_sentiment_Y else 0 
    dog_score= 1 if dog_sentiment_X==dog_sentiment_Y else 0
    pet_score =(cat_score + dog_score)
    return pet_score
    #------mine: returns between 0 to 2 inclusive=[0,2]
    
