# path : test2.py
# module : test2
# konlpy 모듈에서 메소드 매개변수 사용 테스트 : Okt 클래스 사용

from konlpy.tag import Okt              # class
from konlpy.utils import read_txt       # function

# 형태소 분석 태깅 : pos(), morphs(), nouns()등에 사용하는 매개변수들
# norm : 형태소를 깔끔하게 만들어 주고, 불필요한 데이터 지움
# stem : 형태소의 원형을 찾아서 반환해 줌
okt = Okt()

# 텍스트 파일(*.txt) 의 데이터를 읽어와서 분석하기
text = read_txt('./data/sample.txt',u'utf-8')

#문구 원형 : 게임을 통해 디지털 트렌스포메이션의 자본적 수혜자가 일반 대중으로 확산되고 있고, 소비자에 머물렀던 일반 대중이 디지털 생산자로 변화하고 있다며 일부 인플루언서에 그치지 않고 일반 대중으로 확산될 것이며 디지털 컨텐츠는 대중이 접근하기 쉬운 아르바이트, 투잡이 투잡이 될 것이다.
print('norm=True, stem=True--------------------------------')
mal_list = okt.pos(text,norm=True,stem=True)
print(mal_list)
# [('게임', 'Noun'), ('을', 'Josa'), ('통해', 'Noun'), ('디지털', 'Noun'), ('트', 'Noun'), ('렌스', 'Noun'), ('포', 'Noun'), ('메이', 'Noun'), ('션', 'Noun'), ('의', 'Josa'), ('자본', 'Noun'), ('적', 'Suffix'), ('수혜자', 'Noun'), ('가', 'Josa'), ('일반', 'Noun'), ('대중', 'Noun'), ('으로', 'Josa'), ('확산', 'Noun'), ('되다', 'Verb'), ('있다', 'Adjective'), (',', 'Punctuation'), ('소비자', 'Noun'), ('에', 'Josa'), ('머무르다', 'Verb'), ('일반', 'Noun'), ('대중', 'Noun'), ('이', 'Josa'), ('디지털', 'Noun'), ('생산자', 'Noun'), ('로', 'Josa'), ('변화', 'Noun'), ('하고', 'Josa'), ('있다', 'Adjective'), ('일부', 'Noun'), ('인', 'Noun'), ('플루', 'Noun'), ('언', 'Modifier'), ('서', 'Modifier'), ('에', 'Noun'), ('그치다', 'Verb'), ('않다', 'Verb'), ('일반', 'Noun'), ('대중', 'Noun'), ('으로', 'Josa'), ('확산', 'Noun'), ('되다', 'Verb'), ('것', 'Noun'), ('이며', 'Josa'), ('디지털', 'Noun'), ('컨텐츠', 'Noun'), ('는', 'Josa'), ('대중', 'Noun'), ('이', 'Josa'), ('접근', 'Noun'), ('하다', 'Verb'), ('쉽다', 'Adjective'), ('아르바이트', 'Noun'), (',', 'Punctuation'), ('투잡', 'Noun'), ('이', 'Josa'), ('투잡', 'Noun'), ('이', 'Josa'), ('되다', 'Verb'), ('것', 'Noun'), ('이다', 'Josa'), ('.', 'Punctuation')]

print('norm=False, stem=False--------------------------------')
mal_list = okt.pos(text,norm=False,stem=False)
print(mal_list)
# [('게임', 'Noun'), ('을', 'Josa'), ('통해', 'Noun'), ('디지털', 'Noun'), ('트', 'Noun'), ('렌스', 'Noun'), ('포', 'Noun'), ('메이', 'Noun'), ('션', 'Noun'), ('의', 'Josa'), ('자본', 'Noun'), ('적', 'Suffix'), ('수혜자', 'Noun'), ('가', 'Josa'), ('일반', 'Noun'), ('대중', 'Noun'), ('으로', 'Josa'), ('확산', 'Noun'), ('되고', 'Verb'), ('있고', 'Adjective'), (',', 'Punctuation'), ('소비자', 'Noun'), ('에', 'Josa'), ('머물렀던', 'Verb'), ('일반', 'Noun'), ('대중', 'Noun'), ('이', 'Josa'), ('디지털', 'Noun'), ('생산자', 'Noun'), ('로', 'Josa'), ('변화', 'Noun'), ('하고', 'Josa'), ('있다며', 'Adjective'), ('일부', 'Noun'), ('인', 'Noun'), ('플루', 'Noun'), ('언', 'Modifier'), ('서', 'Modifier'), ('에', 'Noun'), ('그치지', 'Verb'), ('않고', 'Verb'), ('일반', 'Noun'), ('대중', 'Noun'), ('으로', 'Josa'), ('확산', 'Noun'), ('될', 'Verb'), ('것', 'Noun'), ('이며', 'Josa'), ('디지털', 'Noun'), ('컨텐츠', 'Noun'), ('는', 'Josa'), ('대중', 'Noun'), ('이', 'Josa'), ('접근', 'Noun'), ('하기', 'Verb'), ('쉬운', 'Adjective'), ('아르바이트', 'Noun'), (',', 'Punctuation'), ('투잡', 'Noun'), ('이', 'Josa'), ('투잡', 'Noun'), ('이', 'Josa'), ('될', 'Verb'), ('것', 'Noun'), ('이다', 'Josa'), ('.', 'Punctuation')]
