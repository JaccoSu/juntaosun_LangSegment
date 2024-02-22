import LangSegment


if __name__ == "__main__":
    
    
    # 输入示例：（包含日文，中文，韩语，英文）
    # 入力例:（日本語、中国語、韓国語、英語を含む）
    # 입력 예: (일본어, 중국어, 한국어, 영어 포함)
    # Input example: (including Japanese, Chinese, Korean, English)
    text = "你的名字叫<ja>佐々木？<ja>吗？韩语中的안녕 오빠读什么呢？あなたの体育の先生は誰ですか? 此次发布会带来了四款iPhone 15系列机型和三款Apple Watch等一系列新品，这次的iPad Air采用了LCD屏幕" 
    
    
    # 进行分词：（接入TTS项目仅需一行代码调用）
    # 분할: (TTS 프로젝트에 액세스하려면 코드 한 줄만 필요합니다.)
    # 分かち書きを行う:(TTSプロジェクトにアクセスするには、1行のコード呼び出しだけが必要です)
    # Segmentation: (Only one line of code is required to access the TTS project)
    langlist = LangSegment.getTexts(text)
    print("\n\n===================【打印结果】===================")
    for line in langlist:
        print(line)
    print("==================================================\n")
    
    
    # 分词输出：lang=语言，text=内容。Word output: lang = language, text = content
    # 分かち書き出力: lang=言語、text=内容。단어 출력: 언어 = 언어, 텍스트 = 내용
    # ===================【打印结果】===================
    # {'lang': 'zh', 'text': '你的名字叫'}
    # {'lang': 'ja', 'text': '佐々木？'}
    # {'lang': 'zh', 'text': '吗？韩语中的'}
    # {'lang': 'ko', 'text': '안녕 오빠'}
    # {'lang': 'zh', 'text': '读什么呢？'}
    # {'lang': 'ja', 'text': 'あなたの体育の先生は誰ですか?'}
    # {'lang': 'zh', 'text': ' 此次发布会带来了四款'}
    # {'lang': 'en', 'text': 'i Phone '}
    # {'lang': 'zh', 'text': '15系列机型和三款'}
    # {'lang': 'en', 'text': 'Apple Watch'}
    # {'lang': 'zh', 'text': '等一系列新品，这次的'}
    # {'lang': 'en', 'text': 'i Pad Air'}
    # {'lang': 'zh', 'text': '采用了'}
    # {'lang': 'en', 'text': 'L C D'}
    # {'lang': 'zh', 'text': '屏幕'}
    # ===================【语种统计】===================
    
    # 功能二，语种统计:
    print("\n===================【语种统计】===================")
    # 获取所有语种数组结果，根据内容字数降序排列
    # Get the array results in all languages, sorted in descending order according to the number of content words
    langCounts = LangSegment.getCounts()
    print(langCounts , "\n")
    
    # 根据结果获取内容的主要语种 (语言，字数含标点)
    # Get the main language of content based on the results (language, word count including punctuation)
    lang , count = langCounts[0] 
    print(f"输入内容的主要语言为 = {lang} ，字数 = {count}") # The main language of the input is
    print("==================================================\n")

    # ===================【语种统计】===================
    # [('zh', 51), ('en', 33), ('ja', 19), ('ko', 5)]

    # 输入内容的主要语言为 = zh ，字数 = 51
    # ==================================================
    
    
    
    
    