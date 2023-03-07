import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

GL = 'gl2018'
#convert txt to csv
txt_path = './data/' + GL+ '/' + GL + '.txt'
csv_path = './data/' + GL+ '/' + GL + '.csv'

with open(txt_path) as f:
    with open(csv_path, 'w') as f1:
        for line in f:
            f1.write(line)



MLB = pd.read_csv(csv_path)
print(MLB.shape)
# add column headers to the dataframe
columns = ['Date','DoubleHeader','Day','VisitingTeam','VisitingLeague','VisitingGameNumber','HomeTeam','HomeLeague',
            'HomeGameNumber','VisitorRunsScored','HomeRunsScore','LengthOuts','DayNight','CompletionInformation',
            'ForfeitInformation','ProtestInformation','ParkID','Attendance','LengthMinutes','VisitorLineScore',
            'HomeLineScore','VisitorAtBats','VisitorHits','VisitorDoubles','VisitorTriples','VisitorHomeruns',
            'VisitorRBI','VisitorSacHits','VisitorSacFlies','VisitorHitByPitch','VisitorWalks','VisitorIntentionalWalks',
            'VisitorStrikeouts','VisitorStolenBases','VisitorCaughtStealing','VisitorGroundedIntoDoublePlay',
            'VisitorFirstCatcherInterference','VisitorLeftOnBase','VisitorPitchersUsed','VisitorIndividualEarnedRuns',
            'VisitorTeamEarnedRuns','VisitorWildPitches','VisitorBalks','VisitorPutouts','VisitorAssists','VisitorErrors',
            'VisitorPassedBalls','VisitorDoublePlays','VisitorTriplePlays','HomeAtBats','HomeHits','HomeDoubles',
            'HomeTriples','HomeHomeruns','HomeRBI','HomeSacHits','HomeSacFlies','HomeHitByPitch','HomeWalks',
            'HomeIntentionalWalks','HomeStrikeouts','HomeStolenBases','HomeCaughtStealing','HomeGroundedIntoDoublePlay',
            'HomeFirstCatcherInterference','HomeLeftOnBase','HomePitchersUsed','HomeIndividualEarnedRuns',
            'HomeTeamEarnedRuns','HomeWildPitches','HomeBalks','HomePutouts','HomeAssists','HomeErrors','HomePassedBalls',
            'HomeDoublePlays','HomeTriplePlays','UmpireHID', 'UmpireHName', 'Umpire1BID', 'Umpire1BName', 'Umpire2BID',
            'Umpire2BName', 'Umpire3BID', 'Umpire3BName', 'UmpireLFID', 'UmpireLFName', 'UmpireRFID', 'UmpireRFName',
            'VisitorManagerID', 'VisitorManagerName', 'HomeManagerID', 'HomeManagerName', 'WinningPitcherID',
            'WinningPitcherName', 'LosingPitcherID', 'LosingPitcherNAme', 'SavingPitcherID', 'SavingPitcherName',
            'GameWinningRBIID', 'GameWinningRBIName', 'VisitorStartingPitcherID', 'VisitorStartingPitcherName',
            'HomeStartingPitcherID', 'HomeStartingPitcherName', 'VisitorBatting1PlayerID', 'VisitorBatting1Name',
            'VisitorBatting1Position', 'VisitorBatting2PlayerID', 'VisitorBatting2Name', 'VisitorBatting2Position',
            'VisitorBatting3PlayerID', 'VisitorBatting3Name', 'VisitorBatting3Position', 'VisitorBatting4PlayerID',
            'VisitorBatting4Name', 'VisitorBatting4Position', 'VisitorBatting5PlayerID', 'VisitorBatting5Name',
            'VisitorBatting5Position', 'VisitorBatting6PlayerID', 'VisitorBatting6Name', 'VisitorBatting6Position',
            'VisitorBatting7PlayerID', 'VisitorBatting7Name', 'VisitorBatting7Position', 'VisitorBatting8PlayerID',
            'VisitorBatting8Name', 'VisitorBatting8Position', 'VisitorBatting9PlayerID', 'VisitorBatting9Name',
            'VisitorBatting9Position', 'HomeBatting1PlayerID', 'HomeBatting1Name', 'HomeBatting1Position',
            'HomeBatting2PlayerID', 'HomeBatting2Name', 'HomeBatting2Position', 'HomeBatting3PlayerID', 'HomeBatting3Name',
            'HomeBatting3Position', 'HomeBatting4PlayerID', 'HomeBatting4Name', 'HomeBatting4Position', 'HomeBatting5PlayerID',
            'HomeBatting5Name', 'HomeBatting5Position', 'HomeBatting6PlayerID', 'HomeBatting6Name', 'HomeBatting6Position',
            'HomeBatting7PlayerID', 'HomeBatting7Name', 'HomeBatting7Position', 'HomeBatting8PlayerID', 'HomeBatting8Name',
            'HomeBatting8Position', 'HomeBatting9PlayerID', 'HomeBatting9Name', 'HomeBatting9Position', 'AdditionalInformation',
            'AcquisitionInformation']
MLB.columns = columns
print(MLB)

print(MLB.columns.tolist())

# print(MLB)


# MLB18 = MLB[['VisitingTeam','HomeTeam','VisitorRunsScored','HomeRunsScore','Date']]
# MLB18 = MLB18.rename(columns={'VisitorRunsScored':'VisR','HomeRunsScore':'HomR'})
# MLB18

# MLB18['hwin']= np.where(MLB18['HomR']>MLB18['VisR'],1,0)
# MLB18['awin']= np.where(MLB18['HomR']<MLB18['VisR'],1,0)
# MLB18['count']=1
# MLB18


# MLBhome = MLB18.groupby('HomeTeam')['hwin','HomR','VisR','count'].sum().reset_index()
# MLBhome = MLBhome.rename(columns={'HomeTeam':'team','VisR':'VisRh','HomR':'HomRh','count':'Gh'})
# print(MLBhome)


# MLBaway = MLB18.groupby('VisitingTeam')['awin','HomR','VisR','count'].sum().reset_index()
# MLBaway = MLBaway.rename(columns={'VisitingTeam':'team','VisR':'VisRa','HomR':'HomRa','count':'Ga'})
# print(MLBaway)



# MLB18 = pd.merge(MLBhome,MLBaway,on='team')
# print(MLB18)




# MLB18['W']=MLB18['hwin']+MLB18['awin']
# MLB18['G']=MLB18['Gh']+MLB18['Ga']
# MLB18['R']=MLB18['HomRh']+MLB18['VisRa']
# MLB18['RA']=MLB18['VisRh']+MLB18['HomRa']
# print(MLB18)



# MLB18['wpc'] = MLB18['W']/MLB18['G']
# MLB18['pyth'] = MLB18['R']**2/(MLB18['R']**2 + MLB18['RA']**2)
# print(MLB18)



# sns.relplot(x="pyth", y="W", data = MLB18)



# pyth_lm = smf.ols(formula = 'wpc ~ pyth', data=MLB18).fit()
# pyth_lm.summary()

# # plot against wpc
# sns.relplot(x="pyth", y="wpc", data = MLB18)
# pyth_lm = smf.ols(formula = 'wpc ~ pyth', data=MLB18).fit()
# pyth_lm.summary()

