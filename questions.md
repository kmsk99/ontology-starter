# 답하고 싶은 질문 / Competency questions

1. 환불은 어떤 결제에 딸려 있나? / Which payment does a refund belong to?
   - `Refund → refundOf → Payment`
2. 환불 합계가 결제 금액을 넘나? / Does the total refund exceed the payment amount?
   - 결제별 `refundAmount` 합계와 `amount`를 비교합니다.
   - Compare the sum of `refundAmount` per payment with its `amount`.
3. 회원은 어느 센터 소속인가? / Which center does a member belong to?
   - `Member → memberOf → Center`
