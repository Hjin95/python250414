import re

# 이메일 유효성 검사 함수
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# 샘플 이메일 리스트 (유효한 것과 유효하지 않은 것 섞어서)
sample_emails = [
    "example@example.com",         # valid
    "user.name123@gmail.com",      # valid
    "username@sub.domain.co",      # valid
    "user-name+filter@domain.org", # valid
    "user@domain",                 # invalid (도메인 형식 아님)
    "user@.com",                   # invalid (도메인 앞 없음)
    "@domain.com",                 # invalid (아이디 없음)
    "user name@domain.com",        # invalid (공백 포함)
    "user@domain.c",               # valid (단일 문자 도메인도 RFC 상 유효함)
    "user@domain..com"             # invalid (.. 연속 점)
]

# 검사 실행
for email in sample_emails:
    result = is_valid_email(email)
    print(f"{email:30} --> {'✅ 유효함' if result else '❌ 유효하지 않음'}")

import re

# 이메일 유효성 검사 함수
def is_valid_email(email):
    # 정규표현식 설명:
    # ^                         : 문자열의 시작
    # [a-zA-Z0-9_.+-]+          : 이메일 아이디 부분 (알파벳 대소문자, 숫자, 언더바, 점, 플러스, 빼기 허용) / 1글자 이상
    # @                         : 반드시 포함되어야 하는 @ 기호
    # [a-zA-Z0-9-]+             : 도메인 이름 (알파벳 대소문자, 숫자, 빼기 허용) / 1글자 이상
    # \.                        : 점(.) 문자 (도메인과 확장자 사이에 필요)
    # [a-zA-Z0-9-.]+            : 도메인 확장자 (알파벳 대소문자, 숫자, 점, 빼기 허용) / 1글자 이상
    # $                         : 문자열의 끝

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# 샘플 이메일 리스트 (유효한 것과 유효하지 않은 것 섞어서)
sample_emails = [
    "example@example.com",         # ✅ 유효
    "user.name123@gmail.com",      # ✅ 유효
    "username@sub.domain.co",      # ✅ 유효
    "user-name+filter@domain.org", # ✅ 유효
    "user@domain",                 # ❌ 도메인에 점(.) 없음
    "user@.com",                   # ❌ 도메인 이름이 없음
    "@domain.com",                 # ❌ 아이디 부분이 없음
    "user name@domain.com",        # ❌ 공백 포함
    "user@domain.c",               # ✅ 유효 (짧은 확장자도 허용됨)
    "user@domain..com"             # ❌ 점이 두 번 연속
]

# 검사 실행
for email in sample_emails:
    result = is_valid_email(email)
    print(f"{email:30} --> {'✅ 유효함' if result else '❌ 유효하지 않음'}")
