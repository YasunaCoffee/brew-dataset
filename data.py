import csv

# 質問と回答のペアを定義
qa_pairs = [
    {
        'Label': 'カフェオレ',
        'Question': "カフェオレとは何ですか？",
        'Answer': "カフェオレはドリップコーヒーにミルクを加えた飲み物です。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "カフェオレの淹れ方を教えてください。",
        'Answer': "カフェオレを淹れるためには、コーヒードリッパーを使用し、コーヒーの粉、お湯、牛乳、氷を用意します。具体的な手順はレシピに記載されています。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "このレシピの特徴は何ですか？",
        'Answer': "このレシピはFUKUSUKE COFFEE ROASTERY店舗で提供しているデカフェホンジュラスを使用したカフェインレスオレの淹れ方をベースにしています。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "カフェオレにおすすめなコーヒーは何ですか？",
        'Answer': "カフェオレにおすすめなコーヒーとして、SAKURAI BLEND、Brazil Grama Valley、Decaf Hondurasがあります。それぞれの特徴も紹介されています。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "カフェオレとカフェラテの違いは何ですか？",
        'Answer': "カフェオレはドリップコーヒーにミルクを加えた飲み物であり、カフェラテはエスプレッソにミルクを加えた飲み物です。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "コーヒードリッパーのおすすめの種類は何ですか？",
        'Answer': "コーヒードリッパーとしては、ORIGAMI ドリッパー、ハリオV60、カリタウェーブが特におすすめです。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "コーヒーの粉の量は何ですか？",
        'Answer': "コーヒーの粉の量は13g（中挽き）です。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "お湯の量はどれくらいですか？",
        'Answer': "お湯の量は100gで、お湯の温度は90度前後です。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "牛乳の量はどれくらいですか？",
        'Answer': "牛乳の量は90gです。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "氷の量はどれくらいですか？",
        'Answer': "氷の量は約4個程度です。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "コーヒーの粉をドリッパーに入れる方法は？",
        'Answer': "コーヒーの粉をドリッパーに入れて、25gのお湯を注ぎ、20秒待ちます。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "お湯をどれくらい注ぐべきですか？",
        'Answer': "お湯を注ぐ回数は合計4回に分けて行い、お湯の量を段階的に増やしていきます。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "お湯を注いだ後の待ち時間は？",
        'Answer': "お湯を注いだ後は20秒ずつ待ちます。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "お湯が落ち切るのを待つ理由は何ですか？",
        'Answer': "お湯が落ち切るのを待つことで、コーヒーが均等に抽出され、美味しいカフェオレが作られます。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "コーヒーをかき混ぜる理由は何ですか？",
        'Answer': "コーヒーをかき混ぜることで、下のほうが濃く、上のほうが薄くなっているため、均等に味が混ざり、美味しいカフェオレが楽しめます。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "カフェオレが完成したら何をすべきですか？",
        'Answer': "カフェオレが完成したら、ミルクと氷の入ったグラスに注ぎ、お楽しみください。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "SAKURAI BLENDの味わいは？",
        'Answer': "SAKURAI BLENDは華やかかつマイルドな味わいで、ミルクと合わせると甘みが際立ちます。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "Brazil Grama Valleyの特徴的な味は？",
        'Answer': "Brazil Grama Valleyはマイルドな味わいで、ローストアーモンドやチョコレートの風味があります。"
    },
    {
        'Label': 'カフェオレ',
        'Question': "Decaf Hondurasの特徴は何ですか？",
        'Answer': "Decaf Hondurasはカフェインが99.9%除去されたカフェインレスコーヒーで、ダークチョコレートとオレンジの風味があります。"
    },
    # 他の質問と回答をここに追加してください
]

# 質問と回答のペアをCSVファイルに出力
with open('qna_dataset.csv', 'w', newline='') as csvfile:
    fieldnames = ['Label', 'Question', 'Answer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for qa_pair in qa_pairs:
        writer.writerow(qa_pair)

print('Q&AデータセットをCSVファイルに保存しました。')
