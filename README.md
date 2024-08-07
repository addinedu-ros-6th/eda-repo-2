# eda-repo-2
EDA 프로젝트 2조 저장소. 지역별 인구 변화 원인 분석
### 지역별 인구 변화 원인 분석

1. 제목설정
1-1.주제선정
2008 ~ 2024년까지의 지역별 인구 변화의 원인분석
![tmp](https://github.com/user-attachments/assets/a69627c8-57b3-4de1-9eff-6e20eb1c1385)

1-2. 지역 / 기간 특정
2013년부터 2022년 인구변화 경기도 /  서울
![tmp1](https://github.com/user-attachments/assets/15f93691-7c49-4515-92e5-0bd45a48247c)

![tmp2](https://github.com/user-attachments/assets/418291e7-f3bd-4fc0-94e5-26939396b7e2)

1-3. 지역 / 기간 특정 이유
서울 / 경기 지역의 인구변화가 타 지역의 비해 두드러진 변화를 보임
따라서, 해당 지역을 기준으로 인구 변화의 원인이 무엇인지 가설 설정

![tmp3](https://github.com/user-attachments/assets/2a0f2f82-8d5d-4e03-990c-85d5f81536c9)

![tmp4](https://github.com/user-attachments/assets/7d8f0313-27c4-43df-a68b-143a0c227ce5)

![tmp5](https://github.com/user-attachments/assets/87fe96ed-dfb0-407c-b201-595b846f3c6c)

![tmp6](https://github.com/user-attachments/assets/a4bd43a5-e4f9-4588-b70d-272c10508251)

2. 가설 제시
특정 지역의 인구변화에 영향을 미치는 원인은 무엇이 있을지 가설 설정
각 가설의 유효성을 확인 하기 위해, 개별 데이터 분석 진행

가설 1 - 교육이 지역별 인구 변화의 가장 큰 원인일 것이다
가설 2 - 집값이 지역별 인구 변화의 가장 큰 원인일 것이다
가설 3 - 외국인 유입이 지역별 인구 변화의 가장 큰 원인일 것이다
가설 4 - 총생산 /GDP 수치가 지역별 인구 변화의 가장 큰 원인일 것이다
가설 5 - 복지 요인이 지역별 인구 변화의 가장 큰 원인일 것이다


# 

개별 가설 설명

   


2-6 변화율
상관관계 그래프 서울 2013 ~ 2022(변화율 이용)

서울 인구수 변화
![tmp7](https://github.com/user-attachments/assets/8f82214c-ef35-4648-8561-31a17a96f4c1)

서울 인구수 변화율
![tmp8](https://github.com/user-attachments/assets/c173b3a0-cc1f-46ee-9fe9-acc8fb50c94f)

3. 제목설정
3-1. 결과 분석(서울)
상관관계 그래프 서울 2013 ~ 2022
![tmp9](https://github.com/user-attachments/assets/112d9442-190e-4208-9c27-89520af1c7bf)
![tmp10](https://github.com/user-attachments/assets/84bb08bc-8040-4960-a3f8-6bea25472db0)

3-2. 결과 분석(경기)
상관관걔 그래프 경기 2013 ~ 2022
![tmp11](https://github.com/user-attachments/assets/f44fdfab-cf59-4551-96a7-0ceb2b111e49)
![tmp12](https://github.com/user-attachments/assets/95a9acdc-e3ae-4d8f-a87e-db9015902f41)

5. 제목설정
4-1. 결론(서울)
분석결과, 개인의 경제력은 증가하였지만, 매매가와 전세가가 높아져
거래량이 줄어 든 모습을 보이기 때문에,집값이 올라가서 서울특별시 인구가 줄어들었다고 판단할 수 있다.

![tmp13](https://github.com/user-attachments/assets/ab840f1f-5699-458a-af40-6637d66c4a6a)

4-2. 결론(경기)
분석결과, 우리가 선정한 가설들 말고 또 다른 요인들이 경기도 인구 변화에 더 크게 영향을 준 것으로 판달할 수 있다.
![tmp14](https://github.com/user-attachments/assets/9a7a4694-6517-4903-87cf-ea53bff19cba)

4-3. 고찰
1. 전체 지역의 전 기간 데이터를 활용했다면 전반적인 경향을 파악하기 더 수월했을 것임
   
2. 미처 파악하지 못한, 결과에 더 큰 영향을 주는 요인이 있었을 것임
   
3. 각각의 *독립 변인(가설)과 *종속 변인(인구 변화)의 일대일 상관계수만을 분석의 근거로 사용했기 때문에 여러 요인을 동시에 고려하지 못함. *다중회귀분석 등의 다른 통계적 방법들을 활용했다면 심층적인 분석이 가능했을 것임
   
4. 각각의 가설에서 제시하는 요인이 서로 독립되지 않아 분석 과정에서 비효율을 초래함
   
5. 처음에는 데이터별 절대치로만 상관관계를 파악하려 했으나, *허위 상관 문제를 발견하고 기존의 자료를 *안정 시계열 자료로 변환한 뒤 분석함


