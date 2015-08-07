import recommendation_system
from pandas import DataFrame
from pandas import Series

critics = {
'Lisa Rose': { 'Lady in the water':2.5, 'Snakes on a plane':3.5,
    'Just My Luck': 3.0, 'Superman return': 3.5, 'You, Me and Dupree':2.5,
    'The Night Listener':3.0 },

'Gene Seymour': { 'Lady in the water':3.0, 'Snakes on a plane':3.5,
    'Just My Luck': 1.5, 'Superman return': 5.0, 'You, Me and Dupree':3.5,
    'The Night Listener':3.0 },

'Michael Phillips': { 'Lady in the water':2.5, 'Snakes on a plane':3.0,
    'Just My Luck': 3.0, 'Superman return': 3.5,
    'The Night Listener':4.0 },

'Claudia Puig': { 'Snakes on a plane':3.5,
    'Just My Luck': 3.0, 'Superman return': 4.0, 'You, Me and Dupree':2.5,
    'The Night Listener':4.5 },

'Mick LaSalle': { 'Lady in the water':3.0, 'Snakes on a plane':4.0,
    'Just My Luck': 2.0, 'Superman return': 3.0, 'You, Me and Dupree':2.0,
    'The Night Listener':3.0 },

'Jack Matthews': { 'Lady in the water':3.0, 'Snakes on a plane':4.0,
    'Superman return': 5.0, 'You, Me and Dupree':3.5,
    'The Night Listener':3.0 },
'Toby': {  'Snakes on a plane':3.5,
    'Superman return': 3.5, 'You, Me and Dupree':2.5,
    }
}

data = DataFrame( critics )
recommender =  recommendation_system.Recommendation()
recommends = recommender.getRecommendation( data, "Toby", 5, "item_based" )
print recommends
