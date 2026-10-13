"""두 예제를 따로 검사합니다. 기대한 통과·거절이면 종료 코드가 0입니다."""
from pathlib import Path

from pyshacl import validate
from rdflib import Graph
from rdflib.namespace import SH

ROOT = Path(__file__).resolve().parent


def check(path):
    # 매번 새 그래프를 만들어 서로 다른 예제의 금액이 섞이지 않게 합니다.
    graph = Graph().parse(ROOT / "ontology.ttl", format="turtle")
    graph.parse(path, format="turtle")
    conforms, report, _ = validate(
        graph, shacl_graph=str(ROOT / "shapes.ttl"), inference="none"
    )
    # SHACL 결과의 한국어 메시지를 사용합니다. 비교식을 다시 계산하지 않습니다.
    messages = list(report.objects(None, SH.resultMessage))
    # 값이 치환된 메시지는 언어 태그가 사라질 수 있어 한글도 확인합니다.
    korean = [str(m) for m in messages
              if m.language == "ko" or any("가" <= c <= "힣" for c in str(m))]
    return conforms, sorted(set(korean or map(str, messages)))


def main():
    expected_results = []
    for name, expected in [("ok", True), ("over", False)]:
        path = f"data/{name}.ttl"
        conforms, messages = check(ROOT / path)
        result = "✅ 통과 (conforms: True)" if conforms else "❌ 거절 — " + "; ".join(messages)
        print(f"{path:<13} {result}")
        expected_results.append(conforms == expected)
    return 0 if all(expected_results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
