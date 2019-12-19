from prediction_util import PredictionUtil

evn = PredictionUtil()

evn.read("worldevn.csv") # 파일 읽기
#evn.show() # 데이터 형태 보기
evn.ignore_warning()

#evn.lmplot("rain_mean_annual", "wind","Country")
#evn.myhist()

#evn.myviolinplot("temp_annual_range", "isothermality") # isothermality에 따른 바오올린플롯 그리기
#evn.heatmap(["rain_mean_annual","temp_annual_range","isothermality","wind","cloudiness"]) # 각 컬럼이 서로 얼마나 관계가 깊은지 확인하는 히트맵 그리고
#evn.boxplot("cloudiness", "temp_annual_range") # temp_annual_range에 따른 cloudiness 상태 보기, 바이올린플롯과 모양이 다름
#evn.plot_3d("wind", "rain_mean_annual", "isothermality") # 컬럼의 데이터 분포를 3d로 시각화
#
# # 서프트벡터머신(Support Vector Machine), 논리회귀(Logistic Regression), KNN(K Nearest Neighbors),
# #   의사결정트리(Desicion Tree)의 4가지 머신러닝 알고리즘을 이용한 분류
# gildong.run(["date", "time", "sleep_time"], ["sleep"], 1)
evn.run_all(["cloudiness","temp_annual_range"], ["rain_mean_annual"])