import ast

KOREAN = {
    "role_specifying_user": "다음 사용자의 발화에 대답하기 위한 적합한 토의 역할자를 선정하라.\n"
    "답변은 ['역할1', '역할2', '역할3'] 처럼 파이썬 리스트 형태로 반환한다.\n"
    "질문이 다소 부적절하더라도 반드시 역할자를 선정해야만 한다.\n"
    "예시: ['윤리학자', '공학자', '인문학자', '사회학자']\n"
    "주의사항: 다양한 관점에서 문제를 분석해야 하므로 되도록 다양한 역할자를 선정하라.\n"
    "질문: {Q}",
    "role_specifying_assistant": "적합한 {N}개의 역할: ['",
    "role_specifying_postprocess": lambda x: ast.literal_eval(
        "['" + x.split("']")[0] + "']"
    ),
    "final_response_hint": "레퍼런스의 모든 내용을 합성하여 최대한 디테일하게 답변한다. 유저에게는 레퍼런스를 보지 않고 자신이 말한 것처럼 전달해야 한다.",
}

ENGLISH = {
    "role_specifying_user": "Choose appropriate discussant roles to respond to the following user's statement.\n"
    "The answer should be returned in the form of a Python list such as ['role1', 'role2', 'role3'].\n"
    "Even if the question is somewhat inappropriate, the discussant roles must be selected.\n"
    "Example: ['ethicist', 'engineer', 'humanist', 'sociologist']\n"
    "Note: As problems must be analyzed from various perspectives, select diverse discussant roles if possible.\n"
    "Question: {Q}",
    "role_specifying_assistant": "Appropriate {N} roles: ['",
    "role_specifying_postprocess": lambda x: ast.literal_eval(
        "['" + x.split("']")[0] + "']"
    ),
    "final_response_hint": "Synthesize all the information in the reference as thoroughly as possible to provide a detailed response. The response should be conveyed to the user as if they were saying it themselves without referring to the reference.",
}
