import pandas as pd

ipl_matches=pd.read_csv(r'C:\Users\my pc\PycharmProjects\suresh\data analysis\ipl_analysis\ipl_matches_2008_2022.csv')
print(ipl_matches.shape)
ipl_ball_by_ball=pd.read_csv(r'C:\Users\my pc\PycharmProjects\suresh\data analysis\ipl_analysis\ipl_ball_by_ball_2008_2022.csv')
'''
print(ipl_ball_by_ball.shape)
print(ipl_matches.columns)
print(ipl_ball_by_ball.columns)
chennai_matches=ipl_matches.loc[ipl_matches['city']=='Chennai']
#print(chennai_matches.to_string())
chennai_matches.to_csv('chennai_list.csv',index=False,sep='-')
chennai_winning=ipl_matches.loc[(ipl_matches['city']=='Chennai')&(ipl_matches['winning_team']=='Chennai Super Kings')]
print(chennai_winning)
chennai_winning.to_csv('chennai_winning.csv',index=False,sep='|')
mumbai_winning=ipl_matches.loc[(ipl_matches['city']=='Chennai')&(ipl_matches['winning_team']=='Mumbai Indian')]
mumbai_winning.to_csv('mumbai_winning_matches_csk.csv',index=False,sep='|')
First_off=ipl_matches.loc[(ipl_matches['city']=='Chennai')&(ipl_matches['toss_decision']=='bat')&(ipl_matches['winning_team']=='Chennai Super Kings')]
print(First_off)'''
a=[[1,'A',40],[2,'B',30],[3,'C',50],[4,'D''']]
o=pd.DataFrame(a,columns=['No','Name','Dept_id'])
print(o)
d=[[10,'IT'],[20,'CSE'],[80,'AUTO'],[90,'EEE'],[50,'ECE']]
b=pd.DataFrame(d,columns=['Dept_id','Dep_name'])
print(d)
output=pd.merge(o,b,on='Dept_id',how='inner')
print(output)
output1=pd.merge(o,b,on='Dept_id',how='left')
print(output1)
output2=pd.merge(b,o,on='Dept_id',how='inner')
print(output2)

