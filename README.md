# 온톨로지 엔지니어링, 처음 시작하기

피트니스 센터 관리 서비스를 소재로 한 공개용 미니 실습입니다.
센터·회원·결제·환불은 모두 합성 데이터이며, 금액 단위는 원입니다.
네임스페이스는 예제용 `https://example.org/fitness#`입니다.

## 설치·실행: 3줄

Python 3.10 이상과 pip가 필요합니다. 저장소 폴더에서 실행하세요(macOS/Linux).

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python check.py
```

정상 예제는 통과하고 초과 환불 예제는 거절됩니다. **둘 다 예상대로면 종료 코드 0**입니다.
각 데이터 파일에 온톨로지를 따로 합쳐 검사하므로 예제끼리 섞이지 않습니다.

## 파일 안내

| 파일 | 역할 |
| --- | --- |
| `questions.md` | 모델로 답하고 싶은 질문 3개 |
| `ontology.ttl` | 클래스 4개와 관계·금액 속성 5개 |
| `shapes.ttl` | 원래 결제 정확히 1개, 환불 합계 ≤ 결제 금액 규칙 |
| `data/ok.ttl` | 1,000원 결제와 300원 환불 |
| `data/over.ttl` | 1,000원 결제와 1,100원 환불 |
| `check.py` | SHACL 검증과 결과 메시지 출력 |
| `requirements.txt` | 실제 검증한 라이브러리 버전 |
| `LICENSE` | MIT 라이선스, Mason Kim |

온톨로지는 의미를 설명하고 SHACL은 입력 데이터를 검사합니다.
`rdfs:domain`·`rdfs:range` 자체는 입력 거절 규칙이 아닙니다.
이 실습은 두 규칙에 집중합니다. 금액 누락·음수·자료형 등 전체 입력 검증은 생략했습니다.

## 시청자 과제

1. 예제 사본에서 환불액을 1,000원으로 바꿔 경계값이 통과하는지 확인하세요.
2. 환불을 두 건으로 나누고 **합계**가 1,000원을 넘을 때 거절되는지 확인하세요.
3. `refundOf`를 없애거나 두 개로 만들어 첫 번째 규칙을 확인하세요.
4. “환불의 센터가 결제의 센터와 다르면 거절”하도록 센터 관계와 규칙을 설계하세요.
   `shapes.ttl` 끝의 주석이 시작점입니다. 이 규칙은 아직 구현하지 않았습니다.

사본 하나만 검사하려면 `check.py`의 `check(Path("사본 경로"))`를 Python에서 호출하세요.
기본 실행은 원본 두 예제의 기대 결과를 검사합니다.

---

# Getting started with ontology engineering

A public mini exercise for a synthetic fitness center management service.
All centers, members, payments, and refunds are fictional. Amounts are integer KRW.
The example namespace is `https://example.org/fitness#`.

## Install and run: three lines

Use Python 3.10+ with pip. Run from this directory on macOS/Linux.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python check.py
```

The valid example passes; the excessive refund is rejected. Exit code **0 means both
results match expectations**. Each dataset is validated independently with the ontology.

## Files

| File | Purpose |
| --- | --- |
| `questions.md` | Three competency questions |
| `ontology.ttl` | Four classes and five relationship/amount properties |
| `shapes.ttl` | Exactly one original payment; refund total ≤ payment amount |
| `data/ok.ttl` | Payment of 1,000 and refund of 300 |
| `data/over.ttl` | Payment of 1,000 and refund of 1,100 |
| `check.py` | SHACL validation and messages from the validation report |
| `requirements.txt` | Library versions used for verification |
| `LICENSE` | MIT license, Mason Kim |

The ontology describes meaning; SHACL validates data. RDFS domain and range declarations
are not rejection rules. This exercise implements only two rules; missing, negative,
or incorrectly typed amounts need additional validation.

## Exercises

1. Copy a dataset and set the refund to 1,000: equality should pass.
2. Split the refund into two records and verify that their **sum** is checked.
3. Remove `refundOf` or supply two payments to exercise the first rule.
4. Model center relationships and reject a refund when its center differs from the
   payment's center. The comment at the end of `shapes.ttl` is an unimplemented exercise.

To validate one copy, call `check(Path("path/to/copy.ttl"))` from `check.py` in Python.
The default script checks the expected outcomes of the two original examples.
