import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration

def summarize(
        text:str,
        demo:bool=False
    ) -> str:
    tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
    model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')

    if demo:
        with open('component/KoBART-summarization/target.txt', 'r', encoding="UTF-8") as f:
            text = f.readlines()
            text = ''.join(text)

    text = text.replace('\n', ' ')

    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

    summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=4,  max_length=512,  eos_token_id=1)
    result = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
    print(f"\n\n{'='*50} 요약결과 {'='*50}")
    print(result)

    return result

summarize("""(서울=연합인포맥스) 김지연 기자 = 중국 대형 부동산 개발업체 비구이위안의 디폴트(채무불이행)우려가 커지는 가운데 조만간 채무재조정(리스트럭처링)에 나설 것이란 전망이 나왔다.



11일(현지시간) 비즈니스인사이더에 따르면 칼 챈 JP모건 중국 부동산 주식 리서치 헤드는 최근 보고서를 통해 "비구이위안의 예상 손실 규모보다 경영진이 회사가 심각한 어려움에 처해있다는 점을 인정하는 것이 더욱 중요하다"며 "회사가 최종적인 크레디트 이벤트를 앞두고 있으며, 이미 채무재조정을 준비 중일 수 있다"고 진단했다.

JP모건의 보고서는 현지 매체에서 비구이위안이 채무 재조정을 위해 국유기업 CICC(China International Capital Corporation)을 고용했다는 소식 이후에 나왔다.

JP모건은 비구이위안이 올해 9월에 만기가 돌아오는 채무가 78억위안에 달한다고 추산했다. 지난해 말 기준 부채 규모는 1조4천억위안 수준이다.

다른 애널리스트들도 비구이위안이 디폴트 한 후 채무 재조정에 나설 가능성이 크다고 예상했다.

니콜라스 챈 크레디트인사이트의 애널리스트도 인터뷰를 통해 "비구이위안은 올해 남은 기간 달러화 쿠폰 이자를 매달 지급해야 한다"며 유동성이 매우 부족한 상태라고 진단했다.

그는 비구이위안이 자산을 매각하고, 주주자금을 추가 투입할 것으로 보이지만 이것만으로는 충분하지 않을 것이라며 "비구이위안이 디폴트한 후 포괄적인 채무 재조정에 나설 수 있다"고 내다봤다.

노무라의 아이리스 챈 애널리스트는 중국 정부가 위기의 확산을 막기 위해 민간 기업과 국유기업 간에 명확한 선을 정립할 것이라며 "민간기업은 정부의 도움을 받지 못할 가능성이 크며, 민간 기업의 생존 여부는 남은 채권의 만기에 달려있다"고 예상했다.

비구이위안은 지난 10일 올해 상반기 순손실 규모가 450억~550억위원 수준이 될 것이라고 경고한 바 있다. 비구이위안은 지난해 61억위안의 순손실을 기록한 바 있다. 이는 2007년 홍콩 상장 이후 연간 기준 처음으로 순손실을 낸 것이다.

출처 : 연합인포맥스(https://news.einfomax.co.kr)""")