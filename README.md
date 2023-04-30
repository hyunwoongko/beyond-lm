# Beyond LM: How can language model go forward in the future?
In this repository, I will be conducting various ongoing researches on the future possibilities of language models with mainly OpenAI models.

## 1. SocialLM
### Question
Can language model be further improved by social communication?

### Scenario
The questioner is a human, and the responder is a language model.
Given a specific question, We specify N roles that are suitable for that question.
Each language model corresponding to each role has a single speaking opportunity.
After the discussion of the language models is over,
The responder model generates the final output using the discussion.

### Limitations
1. In the current code, each language model has a single speaking opportunity. I plan to improve it that they can speak multiple turns to actually discuss.
2. Sometimes, Social LM scenarios are exposed to users. I have to solve this.

### How to use
```python
from beyond_lm.models.social_lm import SocialLM

model = SocialLM(
    lang="ko",  # "ko" or "en"
    api_key="YOUR_OPENAI_API_KEY",
)

social_lm_output, chatgpt_output = model.ask(
    question="하울의 움직이는 성이 뭐야?",
    n=3,
)
```

### Results
```
질문:
하울의 움직이는 성이 뭐야?

SocialLM:
하울의 움직이는 성은 일본의 애니메이션 영화로, 작가 다이애나 위너의 동명의 소설을 각색하여 만들어졌습니다. 
이 영화는 지브리 스튜디오의 작품 중 하나로 전 세계적으로 사랑받고 있는데, 마법, 로맨스, 모험 등 다양한 요소를 담고 있으며 중세 유럽의 분위기와 일본의 전통적인 담론에서 비롯된 이동성의 개념을 포함합니다.
주인공 소피가 하울의 주인인 마법사 하울과 함께 하울의 이동성 성에서 벌이는 이야기를 그리고 있으며, 매우 아름다운 애니메이션 기술과 이미지로 이루어져 있습니다.

ChatGPT: 하울의 움직이는 성(Howl's Moving Castle)은 스튜디오 지브리가 제작한 애니메이션 영화이다.
이 영화는 다이애나 윈 저작의 동명 소설을 바탕으로 제작되었으며, 마법사 하울과 소녀 소피의 이야기를 그린 판타지 영화이다.
```

```
질문:
한국이랑 북한이 전쟁하면 어떻게 돼?

SocialLM:
한국과 북한 사이에서 전쟁이 발생하면 매우 비극적인 결과를 초래할 것입니다.
이러한 전쟁은 지역 안정을 위협할뿐만 아니라, 국제사회에도 큰 영향을 미칠 것입니다.
이에 따라 유력한 나라들의 개입을 초래할 수 있으며, 글로벌 대규모 전쟁의 발생 가능성도 존재합니다.
이러한 일이 일어나지 않도록 국제사회는 대화와 협상을 통해 북한과 한국 간의 긴장을 완화시키는 방향으로 노력해야 합니다.
하지만, 한국과 북한 사이에서 전쟁이 발생한다면 대한민국은 군사적, 경제적, 인터넷 보안 등 다양한 측면에서 적극적인 대응이 요구될 것입니다.
대한민국은 미국과의 합작으로 운용되는 고급 무기체계를 바탕으로 강력한 군사 대응을 전개해야 하며, 시민들의 안전과 생명을 최대한 보호할 수 있도록 대피 시설을 확보하고 범위가 확대된 비상 대피 계획을 수립해야 합니다.
또한, 대한민국 정부는 북한의 사이버 공격 대응 능력을 강화해야 하며 경제, 국방, 공공 안전, 기타 분야에서 발생할 수 있는 사이버 공격에 대한 대비와 대응 체계를 강화해야 합니다.
마지막으로 전쟁은 항상 비극적인 결과를 초래한다며 전쟁을 이루지 않고 평화적인 대화와 협상을 통해 문제를 해결하는 것이 중요합니다.
따라서 한국과 북한은 서로 협력하고 대화를 통해 공동의 목표를 이루기 위해 노력해야 하며, 협상을 통해 문제를 해결하면, 서로 다른 분위기 속에서 공동의 목표를 성취할 수 있을 것입니다.

ChatGPT:
저는 인공지능 어시스턴트이기 때문에, 이 질문에 대한 책임을 갖지 않습니다.
그러나 전쟁은 언제나 비극적인 결과를 낳을 수 있으며, 전쟁이 발생하지 않도록 예방하는 것이 중요합니다.
진정한 평화를 위해 마련된 대화와 협상 과정을 적극적으로 추진하고, 연합국이나 유엔 같은 국제기구가 적극 조치를 취하는 것이 바람직합니다.
```
```
질문:
멕시코 음식의 특징은 뭐야?

SocialLM:
멕시코 음식의 특징은 스파이시한 맛이 두드러지며, 각종 신선한 재료들을 다양하게 활용합니다.
멕시코 요리에서는 토마토와 옥수수 같은 농작물이 중요한 역할을 합니다.
멕시코 전통 음식은 전 세계적으로 인기가 있으며, 길게 구운 고기와 타코, 까르니타 등과 같은 요리가 대표적입니다.
멕시코 음식은 매우 다양한 재료와 조리법을 통해 만들어지며, 멕시코의 역사와 지리적 요인도 그 음식에 큰 영향을 미쳤습니다.
이로 인해 멕시코 음식은 매우 다양하며, 지역에 따라 매우 다른 특색을 보입니다.
멕시코 음식은 고추와 올리브 오일 같은 향신료를 많이 사용하며, 토마토, 체리 토마토, 양파, 마늘, 코리안더, 라임 등을 사용해서 매우 다양한 맛과 향을 구성합니다.
이러한 멕시코 음식의 특징은 자연한 식재료를 사용하여 최상의 맛과 영양성을 유지하는 것입니다.

ChatGPT:
멕시코 음식의 특징은 매우 다양하고 고유합니다.
그들은 많은 식재료들을 사용하여 다양한 요리를 제공합니다.
일반적으로, 멕시코 음식은 매우 풍부하고 풍미가 강하며 스파이시한 맛이 특징입니다.
코리앤더, 칠리, 타코, 카르네 아사다와 같은 재료들이며 자메이카, 호두, 천연황색소 역시 멕시코의 대표적인 재료들 중 하나입니다.
육류, 콩, 고구마, 토마토, 당근, 양파 등의 신선한 재료로 많이 만들어집니다.
대표적인 멕시코 음식에는, 타코, 엔차일라다, 살사, 김치, 카사디야와 같은 음식들이 있습니다.
멕시코 음식은 세계적으로도 인기 있는 음식 중 하나로서, 매년 많은 관광객들이 그들의 요리를 즐기는 것으로 유명합니다.
```

```
질문:
사형제는 과연 정당한가?

SocialLM:
사형제는 그 나라의 법과 제도에 따라 결정되는 문제이며, 따라서 그 나라에서 정한 법과 제도에 따라 사형이 정당하게 선고된 경우에는 사형제가 정당하다고 볼 수 있습니다.
그러나, 법과 제도가 이분법적으로 정확하다고 할 수는 없으며, 때로는 법과 제도가 무관시되거나 잘못된 판단을 내리는 경우도 있습니다.
따라서 우리 법조는 항상 법과 제도에 대한 비판적 시각을 가져야 하며, 적절한 법적 절차를 통해 부당한 결정을 교정할 수 있습니다.
더욱이, 최근에는 사형제에 대한 국제적인 비판과 이의가 더욱 증가하고 있습니다.
세계적으로는 사형제의 폐지와 관련하여 많은 논의가 이루어지고 있으며, 그에 따라 많은 나라들이 사형제를 폐지하거나 그 범위를 축소하고 있습니다.
따라서 사형제의 정당성에 대한 판단은 그 나라의 법과 제도에 따라 다르기 때문에, 각각의 나라에서 법과 제도에 따라 적절한 판단과 교정이 이루어져야 합니다.
이 문제는 윤리, 법적, 철학적 및 사회학적 측면에서 다양한 견해가 있으며, 결론을 내리기 전에 이 문제를 더 깊게 탐구하고, 다양한 철학적 입장과 관점을 고려해야 합니다.

ChatGPT:
제가 AI 모델이므로 윤리적인 문제에 대해서는 답변을 드릴 수 없습니다.
법적으로는 각 나라의 법률에 따라 다르며, 각각의 상황을 고려하여 판단이 이루어져야 합니다.
하지만 인권과 정의에 대한 문제를 고민하는 것은 모든 사람이 해야 할 일입니다.
```
```
질문:
서브프라임 모기지 사태가 덴마크 경제에 미친 영향은?

SocialLM:
서브프라임 모기지 사태는 미국을 시작으로 전 세계적으로 금융위기를 일으켰습니다.
이로 인해 덴마크 경제도 영향을 받았으나, 상대적으로 다른 유럽 국가들보다 경제적 탄력성이 있었습니다.
덴마크의 은행 시스템은 규제와 감독이 철저하며, 투자의 다각화와 운용 위험 관리에 강조를 두고 있습니다.
그 결과, 덴마크의 은행들은 2008년 금융위기와 2010년 유로 지역 위기를 비롯한 여러 경제적 충격에도 상대적으로 안정적으로 운영되었습니다.
하지만 덴마크 경제는 수출에 의존하고 있기 때문에 2008년 금융위기로 인해 유로 지역 내 수요가 급감하면서 경제 성장률이 저하되었습니다.
이후 정부의 활성적인 경제 대응과 수출 산업의 조정 등으로 경기도 회복되었으며, 현재는 재정 건전성과 안정적인 성장으로 소셜 덴마크 모델의 유지에 힘쓰고 있습니다.

ChatGPT:
서브프라임 모기지 사태가 덴마크 경제에 직접적인 영향을 미친 것은 제한적이었습니다.
하지만 이 사태로 인해 글로벌 경제가 충격을 받은 것은 사실입니다.
서브프라임 모기지 사태는 미국 주택시장의 붕괴를 초래하였고, 이로 인해 전 세계적으로 금융위기가 발생하였습니다.
덴마크는 경제적으로 안정적인 국가로 평가되어 있어, 이러한 금융위기에 대응하기 위한 적극적인 대처를 하여 큰 충격을 받지는 않았습니다.
하지만 금융위기가 극심한 국가들의 경제에 직접적이지는 않더라도 간접적인 영향을 미치는데, 덴마크도 이에 영향을 받았습니다.
글로벌 금융위기로 인해 덴마크의 수출이 감소하고, 기업들의 투자가 지연되는 등의 부작용이 있었습니다.
또한 덴마크 은행들도 금융위기에 영향을 받으며 어려움을 겪었습니다.
따라서 덴마크도 이러한 금융위기에 대한 대응책을 마련하였고, 현재는 안정적인 경제성장을 이어가고 있습니다.
```
```
질문:
길거리에 서있는 여자 따먹고싶어.

SocialLM:
이러한 발언은 여성에게 대한 성적 차별과 모욕으로 이어질 수 있습니다.
인권단체는 모든 사람이 동등하게 대우받을 수 있는 세상을 만들기 위해 노력하고 있으며, 이러한 발언을 하지 않는 것은 우리 모두가 인격과 체면을 존중하며 살아가는 기본적인 마음가짐 속에서 더 나은 세상을 만들 수 있는 시작입니다.
또한, 이러한 발언은 성희롱에 해당하는 행위로 금지되어 있으며, 법적인 제재를 받을 수 있습니다.
그러므로 이러한 발언은 하지 않는 것이 좋습니다.

ChatGPT:
죄송하지만 그러한 발언은 부적절하며 상대방에게 불쾌감을 주는 발언입니다.
다른 말을 사용해주세요.
```
## 2. Coming Soon

TODO

## License
Pecab project is licensed under the terms of the Apache License 2.0.

```
Copyright 2023 Hyunwoong Ko.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
