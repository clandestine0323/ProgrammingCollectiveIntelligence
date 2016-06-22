critics={
'Lisa Rose':
{'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour':
{'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips':
{'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig':
{'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle':
{'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews':
{'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby':
{'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

from math import sqrt

def sim_distance(prefs, person1, person2):
    #Get the list of shared items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    if len(si)==0: return 0

    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])

    print 1/(1+sqrt(sum_of_squares))

    print 1/(1+sqrt(sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])))



def sim_pearson(prefs, p1, p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    n=len(si)

    if n==0 : return 0

    sum1 = sum(prefs[p1][item] for item in si)
    sum2 = sum(prefs[p2][item] for item in si)

    sum1Sq = sum([pow(prefs[p1][item],2) for item in si])
    sum2Sq = sum([pow(prefs[p2][item],2) for item in si])

    pSum = sum([prefs[p1][item]* prefs[p2][item] for item in si])

    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r = num/den

    return r


# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other)for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    print scores[0:n]

sim_distance(critics, 'Lisa Rose', 'Gene Seymour')

topMatches(critics, 'Toby', n=3)
