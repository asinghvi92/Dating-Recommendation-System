from nltk.stem import PorterStemmer
from scipy import spatial


import re
import math
import collections 

pstemmer = PorterStemmer()
#cosine = spatial.distance.cosine()


def featureXYComputation(UserX,UserY):
    featureXY= [0]*17
    featureXY[0]= educationFeature(UserX['education'],UserY['education'])
    featureXY[1]= religionFeature(UserX['religion'],UserY['religion'])
    featureXY[2]= bodyTypeFeature(UserX['bodyType'],UserY['bodyType'])
    featureXY[3]= dietFeature(UserX['diet'],UserY['diet'])
    #featureXY[4]= zodiacSignFeature(UserX['sign'],UserY['sign'])
    featureXY[4]= ageFeature(UserX['age'],UserY['age'])
    featureXY[5]= smokeFeature(UserX['smokes'],UserY['smokes'])
    featureXY[6]= drinkFeature(UserX['drinks'],UserY['drinks'])
    featureXY[7]= essaysFeature(UserX['essay0'], UserY['essay0'])
    featureXY[8]= essaysFeature(UserX['essay1'], UserY['essay1'])
    featureXY[9]= essaysFeature(UserX['essay2'], UserY['essay2'])
    featureXY[10]= essaysFeature(UserX['essay3'], UserY['essay3'])
    featureXY[11]= essaysFeature(UserX['essay4'], UserY['essay4'])
    featureXY[12]= essaysFeature(UserX['essay5'], UserY['essay5'])
    featureXY[13]= essaysFeature(UserX['essay6'], UserY['essay6'])
    featureXY[14]= essaysFeature(UserX['essay7'], UserY['essay7'])
    featureXY[15]= essaysFeature(UserX['essay8'], UserY['essay8'])
    featureXY[16]= essaysFeature(UserX['essay9'], UserY['essay9'])
  
    return featureXY


#TODO: "you will be obselete when Ml comes to power !! "    
def compatibilityScoreCompute(UserX,UserY):
    featureXY= [0]*17
    featureXY[0]= educationFeature(UserX['education'],UserY['education'])
    featureXY[1]= religionFeature(UserX['religion'],UserY['religion'])
    featureXY[2]= bodyTypeFeature(UserX['bodyType'],UserY['bodyType'])
    featureXY[3]= dietFeature(UserX['diet'],UserY['diet'])
    #featureXY[4]= zodiacSignFeature(UserX['sign'],UserY['sign'])
    featureXY[4]= ageFeature(UserX['age'],UserY['age'])
    featureXY[5]= smokeFeature(UserX['smokes'],UserY['smokes'])
    featureXY[6]= drinkFeature(UserX['drinks'],UserY['drinks'])
    featureXY[7]= essaysFeature(UserX['essay0'], UserY['essay0'])
    featureXY[8]= essaysFeature(UserX['essay1'], UserY['essay1'])
    featureXY[9]= essaysFeature(UserX['essay2'], UserY['essay2'])
    featureXY[10]= essaysFeature(UserX['essay3'], UserY['essay3'])
    featureXY[11]= essaysFeature(UserX['essay4'], UserY['essay4'])
    featureXY[12]= essaysFeature(UserX['essay5'], UserY['essay5'])
    featureXY[13]= essaysFeature(UserX['essay6'], UserY['essay6'])
    featureXY[14]= essaysFeature(UserX['essay7'], UserY['essay7'])
    featureXY[15]= essaysFeature(UserX['essay8'], UserY['essay8'])
    featureXY[16]= essaysFeature(UserX['essay9'], UserY['essay9'])
    
    
    score= sum(featureXY)/ float(len(featureXY))
    return score

def stemming(tokens):
    return [pstemmer.stem(token) for token in tokens]

def caseFolding(tokens):
    return [token.lower() for token in tokens]

def ageFeature(x,y):
    weight = 0
    diff = abs(int(x)- int(y))
    if diff < 5:
        weight = 1/float(diff+1)
    return weight

def bodyTypeFeature(x,y):
    num_x= bodyTypeToNum(x)
    num_y= bodyTypeToNum(y)
    return math.log10(num_x*num_y+1)/math.log10(26) #dividing by max to normalize it 
    
def bodyTypeToNum(x):
    x= x.lower()
    if re.search("thin|skinny",x):
        num_x= 3 
    elif re.search("average|fit",x):
        num_x= 4 
    elif re.search("athletic|jacked",x):
        num_x= 5 
    elif re.search("overweight|a little extra|curvy|full figured",x):
        num_x= 3 
    elif re.search("used up",x):
        num_x= 2 
    else:
        num_x= 0 
    
    return num_x

def dietFeature(x,y):
    if x==y:
        #if both have matching response, just return the max, even if both responses are wacky. Eg, both have diet response as "love"
        return 1 
    else:
        num_x= dietToNum(x)
        num_y= dietToNum(y)
        return 1/float(abs(num_x-num_y)+1) if num_x!=0 and num_y!=0 else 0 
    
def dietToNum(x):
    x= x.lower()
    if re.search("vegetarian|vegan",x): 
        num_x= 2 
    elif re.search("kosher",x):
        num_x= 7
    elif re.search("halal",x):
        num_x= 10
    elif x is not None:
        num_x= 5 
    else:
        #no response case 
        num_x= 0
    return num_x    
    

def drinkFeature(x,y):
    if x==y:
        return 1 
    else:
        num_x= drinkToNum(x)
        num_y= drinkToNum(y)
        return 1/float(abs(num_x-num_y)+1) if num_x!=0 and num_y!=0 else 0

def drinkToNum(x):
    x=x.lower()
    if re.search("often|desperate|playmate|present",x):
        num_x= 1 
    elif re.search("social",x):
        num_x= 2 
    elif re.search("rare",x):
        num_x= 3 
    elif re.search("no|never",x):
        num_x= 4 
    else:
        num_x= 0 
    return num_x
    
    
#TODO: ignored this for now as not parsed in input vectors, might consider it later 
def drugFeature(x,y):
    if x==y:
        return 1 
    else:
        num_x= drugToNum(x)
        num_y= drugToNum(y)
        return 1/float(abs(num_x-num_y)+1) if num_x!=0 and num_y!=0 else 0

def drugToNum(x):
    x= x.lower()
    if re.search("often|smiling",x):
        num_x= 1 
    elif re.search("sometime",x):
        num_x= 2 
    elif re.search("no|never",x):
        num_x= 3
    else:
        num_x= 0 
    return num_x
        
        
def educationFeature(x,y):
    #premise: similar educational qualification people should prefer each other 
    if x==y:
        return 1 
    else:
        num_x= educationToNum(x)
        num_y= educationToNum(y)
        return 1/float(abs(num_x-num_y)+1) if num_x!=0 and num_y!=0 else 0

def educationToNum(x):
    x= x.lower()
    if re.search("space|high school",x):
        num_x= 1 
    elif re.search("college",x):
        num_x= 2 
    elif re.search("univ|master",x):
        num_x= 3
    elif re.search("law|med|ph",x):
        num_x= 4 
    else:
        num_x= 0 
    return num_x
                

#petFeature will be made the proxy label as a part of "grand scheme of things"                 
"""
def petFeature(x,y):
    weight = 0
    if x == y:
        weight = 5
    return weight
    #diff = abs(x-y)
    #weight = 1
    #if diff == 0:
    #    weight = 5
    #return weight
"""

def religionFeature(x,y):
    if x == y:
        weight = 1
    elif x != 'atheism' and y != 'atheism':
        weight = 0.5
    elif (x == 'atheism' and y != 'atheism') or (y == 'atheism' and x != 'atheism'):
        weight = 1/10
    else:
        weight = 0
    return weight

"""    
def zodiacSignFeature(x,y):
    weight = 0 
    if x == 'aquarius' and (y == 'leo' or y == 'sagittarius'):
        weight= 1 
    elif x == 'pisces'   and (y == 'virgo' or y == 'taurus'):
        weight= 1
    elif x == 'aries'    and (y == 'libra' or y == 'leo'):
        weight= 1 
    elif x == 'taurus'   and (y == 'scorpio' or y == 'cancer'):
        weight= 1 
    elif x == 'gemini'   and (y == 'sagittarius' or y == 'aquarius'):
        weight= 1 
    elif x == 'cancer'   and (y == 'capricorn' or y == 'taurus'):
        weight= 1 
    elif x == 'leo'      and (y == 'aquarius' or y == 'gemini'):
        weight= 1 
    elif x == 'virgo'    and (y == 'pisces' or y == 'cancer'):
        weight= 1 
    elif x == 'libra'    and (y == 'aries' or y == 'sagittarius'):
        weight= 1 
    elif x == 'scorpio'  and (y == 'taurus' or y == 'cancer'):
        weight= 1 
    elif x == 'sagittarius' and (y == 'gemini' or y == 'aries'):
        weight= 1 
    elif x == 'capricorn' and (y == 'taurus' or y == 'cancer'):
        weight= 1
    elif x is not None and y is not None:
        weight= 1/10
    else:
        weight= 0 
    return weight
"""
    
def smokeFeature(x,y):
    if x==y:
        return 1 
    else:
        num_x= smokeToNum(x)
        num_y= smokeToNum(y)
        return 1/float(abs(num_x-num_y)+1) if num_x!=0 and num_y!=0 else 0

def smokeToNum(x):
    x= x.lower()
    if re.search("yes",x):
        num_x= 1 
    elif re.search("sometime|drinking|trying to quit",x):
        num_x= 2 
    elif re.search("no|never",x):
        num_x= 3
    else:
        num_x= 0 
    return num_x


def essaysFeature(x,y):
    #TODO: experiment with TF-IDF, manhattan and pearson distance 
    #TF score- cosine formula for now 
    x= stemming(x)
    x= caseFolding(x)
    y= stemming(y)
    y= caseFolding(y)
    dict_x= collections.defaultdict(int)
    dict_y= collections.defaultdict(int)
    
    for token in x:
        dict_x[token]+=1 
    for token in y:
        dict_y[token]+=1 
    mag_x= sum([value**2 for value in dict_x.values()])
    mag_y= sum([value**2 for value in dict_y.values()])
    set_tokens = set(dict_x.keys())| set(dict_y.keys())
    cosine_score= 0.0
    
    for token in set_tokens:
        cosine_score+= float(dict_x[token]*dict_y[token])
    cosine_score= cosine_score/float(mag_x*mag_y) if mag_x!=0 and mag_y!=0 else 0 
    return cosine_score
