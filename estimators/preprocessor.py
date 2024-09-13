from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from estimators.LogitOddsEncoder import LogitOddsEncoder
from sklearn.pipeline import Pipeline, FeatureUnion

numerical_features = ['LiveTime', 
                      'StaysInWeekendNights', 
                      'StaysInWeekNights', 
                      'Adults', 
                      'Children', 
                      'Babies', 
                      'ADRThirdQuartileDeviation', 
                      'IsRepeatedGuest', 
                      'PreviousCancellations', 
                      'PreviousBookingsNotCanceled', 
                      'BookingChanges', 
                      'DaysInWaitingList', 
                      'TotalOfSpecialRequests']
categorical_features = ['DepositType', 
                        'DistributionChannel', 
                        'CustomerType', 
                        'Meal', 
                        'MarketSegment', 
                        'Hotel',
                        'Agent', 
                        'Company']

# Preprocessing pipeline for numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features[:-2]),  # treat Agent and Company as logit odds because of high cardinality
        ('logit_odds', LogitOddsEncoder(columns=['Agent', 'Company']), ['Agent', 'Company'])
    ])