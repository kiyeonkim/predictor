# -*- coding: utf-8 -*- 
from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()
# pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
pprint(kkma.nouns(u'이 기사는 현재 관심사에 대해서 부정적인 의미를 내포하고있다.'))
# if __name__ == '__main__':
