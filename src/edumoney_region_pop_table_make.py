#%%
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# %%
# MYSQL 서버 연결
remote = mysql.connector.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)
# 커서생성
cursor = remote.cursor()
# 가져올 테이블 이름
table_name = 'population'
# SELECT 쿼리 실행
query = 'SELECT * FROM {}'.format(table_name)
cursor.execute(query)
# 결과 가져오기
result = cursor.fetchall()
# 컬럼 이름 가져오기
columns = [desc[0] for desc in cursor.description]

#%% 
# 결과를 PD df 로 변환
df_pop = pd.DataFrame(result, columns=columns)
# 결과 출력
print(df_pop)

#%% 커서 연결 닫기
cursor.close()
remote.close
# %%
df_pop.info()

# %%
df_pop.head()

# %% 그래프로 그려보기
plt.figure(figsize=(10,6))

#막대그래프생성
seoul_pop = df_pop[df_pop['city'] == '서울특별시']
gyeongi_pop = df_pop[df_pop['city'] == '경기도']
incheon_pop = df_pop[df_pop['city'] == '인천광역시']

# %%
seoul_pop.info()
seoul_pop.head(20)
gyeongi_pop.info()
incheon_pop.info()

# %% 서울 경기 그래프
plt.bar(seoul_pop['year'], seoul_pop['pop_sum'], color = 'blue', label='seoul_pop', alpha = 1.0)
plt.bar(gyeongi_pop['year'], gyeongi_pop['pop_sum'], color='red', label='gyeongi_pop', alpha=0.1)
plt.bar(incheon_pop['year'], incheon_pop['pop_sum'], color='green', label='gyeongi_pop', alpha=1.0)
plt.title('서울 경기 지역 연도별 인구수 변화')
plt.xlabel('년도')
plt.ylabel('지역별 인구수')

plt.xticks(rotation = 90)
plt.legend()

plt.show()
# %%
df_pop.info()
# %%
df_pop.to_csv('지역별인구수변화.csv', index=False, encoding='utf-8-sig')

# %%
plt.bar(incheon_pop['year'], incheon_pop['pop_sum'], color='green', label='incheon_pop', alpha=1.0)
plt.title('서울 경기 지역 연도별 인구수 변화')
plt.xlabel('년도')
plt.ylabel('지역별 인구수')

plt.xticks(rotation = 90)
plt.legend()

plt.show()
# %%
plt.bar(seoul_pop['year'], seoul_pop['pop_sum'], color = 'blue', label='seoul_pop', alpha = 1.0)
plt.title('서울 경기 지역 연도별 인구수 변화')
plt.xlabel('년도')
plt.ylabel('지역별 인구수')

plt.xticks(rotation = 90)
plt.legend()

plt.show()

#%%
plt.bar(gyeongi_pop['year'], gyeongi_pop['pop_sum'], color='red', label='gyeongi_pop', alpha=0.1)
plt.title('서울 경기 지역 연도별 인구수 변화')
plt.xlabel('년도')
plt.ylabel('지역별 인구수')

plt.xticks(rotation = 90)
plt.legend()

plt.show()
# %%
seoul_pop.head(20)
# %%
import matplotlib.animation as animation

# 'year' 열이 숫자형인지 확인
seoul_pop['year'] = seoul_pop['year'].astype(int)
incheon_pop['year'] = incheon_pop['year'].astype(int)
gyeongi_pop['year'] = gyeongi_pop['year'].astype(int)

# 애니메이션 효과를 위한 함수 정의
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.3

years = seoul_pop['year']
n = len(years)

def init():
    ax.set_title('서울 경기 지역 연도별 인구수 변화')
    ax.set_xlabel('년도')
    ax.set_ylabel('지역별 인구수')
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=90)
    ax.set_ylim(0, max(seoul_pop['pop_sum'].max(), incheon_pop['pop_sum'].max(), gyeongi_pop['pop_sum'].max()) * 1.1)
    return []

def animate(i):
    ax.clear()
    init()
    if i < n:
        bar1 = ax.bar(years[:i+1] - bar_width, seoul_pop['pop_sum'][:i+1], width=bar_width, color='blue', label='Seoul', alpha=1.0)
        bar2 = ax.bar(years[:i+1], incheon_pop['pop_sum'][:i+1], width=bar_width, color='green', label='Incheon', alpha=1.0)
        bar3 = ax.bar(years[:i+1] + bar_width, gyeongi_pop['pop_sum'][:i+1], width=bar_width, color='red', label='Gyeonggi', alpha=1.0)
        ax.legend()
        return bar1, bar2, bar3
    else:
        return []

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=n, interval=200, repeat=False)
plt.tight_layout()
plt.show()

# %%
# 'year' 열이 숫자형인지 확인
seoul_pop['year'] = seoul_pop['year'].astype(int)
incheon_pop['year'] = incheon_pop['year'].astype(int)
gyeongi_pop['year'] = gyeongi_pop['year'].astype(int)

# 애니메이션 효과를 위한 함수 정의
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.3

years = seoul_pop['year']
n = len(years)

def init():
    ax.set_title('서울 경기 지역 연도별 인구수 변화')
    ax.set_xlabel('년도')
    ax.set_ylabel('지역별 인구수')
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=90)
    ax.set_ylim(0, max(seoul_pop['pop_sum'].max(), incheon_pop['pop_sum'].max(), gyeongi_pop['pop_sum'].max()) * 1.1)
    return []

def animate(i):
    ax.clear()
    init()
    
    # 모든 데이터를 점진적으로 그리기
    bar1 = ax.bar(years - bar_width, seoul_pop['pop_sum'], width=bar_width, color='blue', label='Seoul', alpha=0.7)
    bar2 = ax.bar(years, incheon_pop['pop_sum'], width=bar_width, color='green', label='Incheon', alpha=0.7)
    bar3 = ax.bar(years + bar_width, gyeongi_pop['pop_sum'], width=bar_width, color='red', label='Gyeonggi', alpha=0.7)

    # 현재 프레임의 인덱스까지 강조 표시
    if i < n:
        ax.bar(years[:i+1] - bar_width, seoul_pop['pop_sum'][:i+1], width=bar_width, color='blue', alpha=1.0)
        ax.bar(years[:i+1], incheon_pop['pop_sum'][:i+1], width=bar_width, color='green', alpha=1.0)
        ax.bar(years[:i+1] + bar_width, gyeongi_pop['pop_sum'][:i+1], width=bar_width, color='red', alpha=1.0)

    ax.legend()
    return bar1, bar2, bar3

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=n, interval=500, repeat=False)

plt.tight_layout()
plt.show()

# %%
