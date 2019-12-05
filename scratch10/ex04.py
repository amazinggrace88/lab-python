import pandas as pd
from lab_python.scratch10.ex02 import peak_to_peak

if __name__ == '__main__':
    # tips.csv 파일 읽어서 데이터 프레임 생성
    df = pd.read_csv('tips.csv')

    # 앞 5 개 데이터 출력
    # print(df.head())
    print(df.iloc[0:5])
    # 목적: 컬럼 이름이 잘 들어갔는지 확인! -- header(컬럼)가 없으면 컬럼 이름이 데이터와 유사하다. *****

    # DF에 tip_pct 컬럼 추가: 팁금액/총금액
    df['tip_pct'] = df['tip'] / df['total_bill']
    print(df.head())
    # 목적 : 상관관계를 위해서 컬럼 추가
    
    # day, smoker 별 그룹지어 tip_pct 의 평균을 출력 (요일별 평균차이, 흡연 여부에 따른 평균 차이)
    df_day = df.groupby(['day', 'smoker'])
    result_day = df_day['tip_pct']
    print(result_day.agg('mean'))
    print(result_day.agg('mean').unstack())

    # day, smoker 별 그룹지어 tip_pct 의 평균, 표준편차, 최대최소 차이를 출력 (함수 만들기/만들어져 있는 함수 사용)
    print(result_day.agg(['mean', 'std', peak_to_peak]))
    # day, smoker 별 그룹지어 tip_pct, total_bill 의 평균, 표준편차, 최대최소 차이를 출력 (함수 만들기/만들어져 있는 함수 사용)
    result_day_2 = df_day[['tip_pct', 'total_bill']]
    print(result_day_2.agg(['mean', 'std', peak_to_peak]))  # 두 단계의 인덱스 출력 : 두단계는 keyword argument 사용하면 error! 이유는 모름 (?)
    print(result_day_2.agg([('average', 'mean'), ('stddev', 'std'), ('range', peak_to_peak)]))  # .agg()쓰는 방법 3) 리스트 안에 튜플 형식으로 쓰는 방법
    # or
    functions = [('average', 'mean'), ('stddev', 'std'), ('range', peak_to_peak)]
    result = result_day_2.agg({
        'tip_pct': functions,
        'total_bill': functions
    })
    print(result)

    # GroupBy 객체 컬럼들마다 서로 다른 함수를 aggregate 로 적용할 때
    # agg({'Groupby 객체에 있는 col_name':[functions1, functions2, ], ... })
    # grouping 된 데이터 프레임의 tip 컬럼에는 max() 함수를 aggregate 하고, size 컬럼에는 sum() 함수를 aggregate함.
    # 주의! key1, key2가 같으면 안된다.
    # 같은 함수는 와도 상관없다.  ex_ result = df_day.agg({'tip': 'max', 'size': 'max'})
    result = df_day.agg({'tip': 'max', 'size': 'sum'})
    print(result)  # tip 은 최댓값만, size 는 합만 출력

    # grouping 컬럼들이 aggregate 결과에서 (최종 결과에서) 인덱스로 사용하지 않고자 할 때,
    df_day = df.groupby(['day', 'smoker'], as_index=False)
    print(df_day['tip'].mean())  # day, smoker, tip이 각각 하나의 컬럼이 된다.
