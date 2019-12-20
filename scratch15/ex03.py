import graphviz
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz
# data bring in !
iris = load_iris()
X = iris.data  # 2 차원 리스트 (행렬 형태)
y = iris.target

# 의사결정나무모델(알고리즘 구현) 객체 생성
decision_tree = DecisionTreeClassifier()
# 데이터를 모델에 fitting(훈련, 학습)
decision_tree.fit(X, y)
# 예측 건너뛰기, (과제)

# 트리 만들기
text_result = export_text(decision_tree, iris.feature_names)
# export_text() : 글로 트리 만들기
print(text_result)

# 트리 그래프를 만들기
graph_data = export_graphviz(decision_tree,
                             feature_names=iris.feature_names,
                             class_names=iris.target_names,
                             filled=True,
                             special_characters=True)  # graph 그릴 수 있는 data 만듬
# 훈련이 끝난 decision tree 넣어준다
graph = graphviz.Source(graph_data)  # graphviz 라는 패키지 안 Source 라는 메소드에 graph_data 넣어줌
graph.render('iris')  # 그래프 객체를 파일로 작성(pdf)
# render 동작방식 -> ?

