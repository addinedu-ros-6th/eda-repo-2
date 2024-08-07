#%% 
import pandas as pd


#%% 년도별 교육청 예산 그래프, 연도별 인구변화 그래프 가져오기

#%%
인구변화표 = pd.read_csv('../data/edumoney_data/지역별인구수변화.csv', encoding='utf-8')

#%%
인구변화표.info()
인구변화표.head()

#%% 월 없애고 6월/12월 기준으로 인구 설정
인구변화표 = 인구변화표[(인구변화표['month'] == 6)]

#%% STEP1
# 인구변화표 컬럼 year 0~20 21~100 예산으로 만들기
인구변화표['0_19'] = 인구변화표['pop_0_9'] + 인구변화표['pop_10_19']
인구변화표['20_100'] = 인구변화표['pop_20_29'] + 인구변화표['pop_30_39'] + 인구변화표['pop_40_49'] + 인구변화표['pop_50_59'] + 인구변화표['pop_60_69'] + 인구변화표['pop_70_79'] + 인구변화표['pop_80_89'] + 인구변화표['pop_90_99'] + 인구변화표['pop_100_']

인구변화표.drop(columns=['month','pop_sum', 'pop_0_9', 'pop_10_19', 'pop_20_29',
       'pop_30_39', 'pop_40_49', 'pop_50_59', 'pop_60_69', 'pop_70_79',
       'pop_80_89', 'pop_90_99', 'pop_100_'], inplace=True)

#%%
인구변화표.drop(인구변화표[인구변화표['city'] == '전국'].index, inplace=True)

#%%
인구변화표.reset_index(drop=True, inplace=True)

#%%
인구변화표 = 인구변화표[(인구변화표['year'] >= 2013) & (인구변화표['year'] <= 2024)]

# %%
인구변화표.columns.unique()
인구변화표.info()
인구변화표.head(30)

# %% 

교육청표 = pd.read_csv('../data/edumoney_data/서울경기인천교육청예산.csv', encoding='utf-8')

교육청표.info()

# %%
서울교육청예산 = 교육청표[교육청표['지역'] == '서울']
서울교육청예산.sort_values('년도', inplace=True)
서울교육청예산.reset_index(drop=True,inplace=True)
서울교육청예산

# %%
경기교육청예산 = 교육청표[교육청표['지역'] == '경기']
경기교육청예산.sort_values('년도', inplace=True)
경기교육청예산.reset_index(drop=True,inplace=True)
경기교육청예산

# %%
인천교육청예산 = 교육청표[교육청표['지역'] == '인천']
인천교육청예산.sort_values('년도', inplace=True)
인천교육청예산.reset_index(drop=True,inplace=True)
인천교육청예산
# %%
서울경기인천예산 = pd.concat([서울교육청예산, 경기교육청예산, 인천교육청예산], axis=1)
# %%
서울경기인천예산.columns = ['지역', '년도', '서울교육청예산','지역', '년도', '경기교육청예산','지역', '년도', '인천교육청예산']
# %%
서울경기인천예산.drop(['지역', '년도'], axis=1, inplace=True)

# %%
인구변화표.reset_index(drop=True,inplace=True)
# %%
인구변화표.head()
서울경기인천예산.head()
# %%
서울인구변화 = 인구변화표[인구변화표['city']=='서울특별시']

서울인구변화.reset_index(drop=True,inplace=True)

서울인구변화.columns = ['city', 'year', '서울0_19', '서울20_100']

서울인구변화.head()
# %%
경기인구변화 = 인구변화표[인구변화표['city']=='경기도']

경기인구변화.reset_index(drop=True,inplace=True)

경기인구변화.columns = ['city', 'year', '경기0_19', '경기20_100']

경기인구변화.head()
#%%
인천인구변화 = 인구변화표[인구변화표['city']=='인천광역시']

인천인구변화.reset_index(drop=True,inplace=True)

인천인구변화.columns = ['city', 'year', '인천0_19', '인천20_100']

인천인구변화.head()
# %%
서울경기인천예산
# %%
서울인구변화
# %%
서울인구변화_결합 = pd.concat([서울인구변화, 서울경기인천예산['서울교육청예산']], axis=1)
서울인구변화_결합
# %%
경기인구변화_결합 = pd.concat([경기인구변화, 서울경기인천예산['경기교육청예산']], axis=1)
경기인구변화_결합
# %%
인천인구변화_결합 = pd.concat([인천인구변화, 서울경기인천예산['인천교육청예산']], axis=1)
인천인구변화_결합
# %%
인구변화결합 = pd.concat([서울인구변화_결합, 경기인구변화_결합, 인천인구변화_결합], axis=1)
인구변화결합
# %%
인구변화결합.drop(['city', 'year'],axis=1, inplace=True)
인구변화결합


#



#%% 데이터프레임 하나로 만들기

# %%
# 상관관계 계산
상관관계_인구변화결합 = 인구변화결합.corr()
상관관계_인구변화결합
# %%
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

# %%
plt.figure(figsize=(8,6))
# sns.heatmap(상관관계_인구변화결합, annot=True,fmt='.2f', cmap='bwr', linewidths=5)
sns.heatmap(상관관계_인구변화결합, annot=True,fmt='.2f', cmap='bwr')
for x in range(3, 상관관계_인구변화결합.shape[1], 3):
    plt.vlines(x, 0, 상관관계_인구변화결합.shape[0], colors='black', linestyles='solid', lw = 5)
    plt.hlines(x, 0, 상관관계_인구변화결합.shape[0], colors='black', linestyles='solid', lw = 5)

plt.title('상관관계_히트맵')
plt.show()
# %%
