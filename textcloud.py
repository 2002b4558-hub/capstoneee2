# 1. 라이브러리 불러오기
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt # konlpy에서 형태소 분석기(Okt) 가져오기

# --- 중요! ---
# 2. 분석할 파일 경로 설정
# 방금 압축 푼 txt 파일의 '전체 경로'를 복사해서 붙여넣으세요.
# (VS Code에서 파일 오른쪽 클릭 -> 'Copy Path' 또는 '경로 복사' 클릭)
file_path = 'c:\Users\2002b\OneDrive\바탕 화면\상담데이터셋\16.심리상담 데이터\TS_001. 우울증_0001. 1회기\TS_001. 우울증_0001. 1회기\resource_depression_1_check_D002' 
# ----------------

# 3. 텍스트 파일 읽기
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print(f"오류: '{file_path}' 파일을 찾을 수 없습니다. 경로를 다시 확인해주세요!")
    # 여기서 멈춤
    raise

print(f"'{file_path}' 파일 로드 성공!")

# 4. (선택) 폰트 경로 설정 (Windows 기준)
# 텍스트 클라우드에 한글이 깨지지 않게 하려면 폰트 경로가 필요합니다.
# 폰트가 없으면 C:\Windows\Fonts 에서 'Malgun Gothic' (malgun.ttf) 등을 찾아서 설정하세요.
# (macOS의 경우: '/Library/Fonts/AppleGothic.ttf')
font_path = 'c:/Windows/Fonts/malgun.ttf' 

# 5. 한글 명사 추출하기
okt = Okt()
nouns = okt.nouns(text)

# 6. 의미 없는 단어 제거하기 (Stopwords)
# 상담사, 내담자 등 분석에 불필요한 단어를 제거해야 의미있는 결과가 나옵니다.
stop_words = ['상담사', '내담자', '선생님', '부분', '생각', '사람', '경우', '얘기',
              '거', '게', '것', '저', '제', '뭐', '그', '이', '때', '좀', '수']

# 2글자 이상이고, stop_words에 없는 단어만 선택
meaningful_nouns = [n for n in nouns if len(n) > 1 and n not in stop_words]

# 7. 단어 빈도수 세기
word_counts = Counter(meaningful_nouns)

# 8. 텍스트 클라우드 생성
wc = WordCloud(
    font_path=font_path,
    background_color='white',
    width=800,
    height=600,
    max_words=100
).generate_from_frequencies(word_counts)

# 9. 결과 보여주기
print("텍스트 클라우드를 생성합니다...")
plt.figure(figsize=(10, 8))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off') # 축 눈금 숨기기
plt.show()

# 10. (보너스) 가장 많이 나온 단어 20개 출력
print("\n[가장 많이 나온 명사 Top 20]")
print(word_counts.most_common(20))