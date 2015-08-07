import pandas as pd
from pandas import DataFrame
from pandas import Series

class Recommendation:
    def __init__( self ):
        pass

    #def __init__( self, resource ):
    #    self.item_correclation_score = DataFrame()

    def getRecommendation( self, data, user, n = 5, metric = "user_based" ):
        if metric == "user_based":
            return self.userBasedRecommendation( data, user, n )
        else:
            return self.itemBasedRecommendation( data, user, n )

    def userBasedRecommendation( self, data, user, n = 5 ):
        #first, compute the similarity score between users
        user_sim_scores = data.corrwith( data[user] ).dropna().drop( user )
        #data[ data[user].isnull() ] returns the movie records haven't been scored by given user
        #which means the recommended candidates
        candidates = data[ data[user].isnull() ]
        #sum_scores is used for normalization
        sum_scores = candidates.notnull().mul( user_sim_scores ).sum( axis=1 )
        recommendation_scores = data[ data[user].isnull() ].mul( user_sim_scores ).sum( axis = 1 ).div( sum_scores.abs() ).order( ascending=False )
        if recommendation_scores.size <= n:
            return [(item,score) for item, score in recommendation_scores.iteritems() ]
        else:
            return [ (item, scores) for item, score in recommendation_scores.head(n).iteritems() ]

    def itemBasedRecommendation( self, data, user, n ):
        user_ratings = data.ix[data[user].notnull(), user ]
        data_T = data.T
        item_similarity_matrix = data_T.corr()
        sum_scores = item_similarity_matrix.ix[data[user].isnull(), data[user].notnull()].sum( axis = 1 )
        recommendation_scores = item_similarity_matrix.ix[data[user].isnull(), data[user].notnull()].mul( user_ratings ).sum( axis = 1 ).div( sum_scores.abs() ).order( ascending = False )
        if recommendation_scores.size <= n:
            return [(item,score) for item, score in recommendation_scores.iteritems() ]
        else:
            return [ (item, scores) for item, score in recommendation_scores.head(n).iteritems() ]


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
recommender =  Recommendation()
recommends = recommender.getRecommendation( data, "Toby", 5, "item_based" )
print recommends
