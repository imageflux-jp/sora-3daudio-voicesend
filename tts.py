"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# export GOOGLE_APPLICATION_CREDENTIALS=something_google_app.json

voice_texts = {
# "wagahaiwa_nekodearu":"吾輩は猫である。名前はまだ無い。どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番｜獰悪な種族であったそうだ。この書生というのは時々我々を捕えて煮て食うという話である。しかしその当時は何という考もなかったから別段恐しいとも思わなかった。ただ彼の掌に載せられてスーと持ち上げられた時何だかフワフワした感じがあったばかりである。掌の上で少し落ちついて書生の顔を見たのがいわゆる人間というものの見始であろう。この時妙なものだと思った感じが今でも残っている。第一毛をもって装飾されべきはずの顔がつるつるしてまるで薬缶だ。その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。のみならず顔の真中があまりに突起している。そうしてその穴の中から時々ぷうぷうと煙を吹く。どうも咽せぽくて実に弱った。これが人間の飲む煙草というものである事はようやくこの頃知った。",
# "kaijin_nijumenso":"そのころ、東京中の町という町、家という家では、ふたり以上の人が顔をあわせさえすれば、まるでお天気のあいさつでもするように、怪人「二十面相」のうわさをしていました。「二十面相」というのは、毎日毎日、新聞記事をにぎわしている、ふしぎな盗賊のあだ名です。その賊は二十のまったくちがった顔を持っているといわれていました。つまり、変装がとびきりじょうずなのです。どんなに明るい場所で、どんなに近よってながめても、少しも変装とはわからない、まるでちがった人に見えるのだそうです。老人にも若者にも、富豪にも乞食にも、学者にも無頼漢にも、いや、女にさえも、まったくその人になりきってしまうことができるといいます。では、その賊のほんとうの年はいくつで、どんな顔をしているのかというと、それは、だれひとり見たことがありません。二十種もの顔を持っているけれど、そのうちの、どれがほんとうの顔なのだか、だれも知らない。いや、賊自身でも、ほんとうの顔をわすれてしまっているのかもしれません。それほど、たえずちがった顔、ちがった姿で、人の前にあらわれるのです。そういう変装の天才みたいな賊だものですから、警察でもこまってしまいました。いったい、どの顔を目あてに捜索したらいいのか、まるで見当がつかないからです。",
# "shunkin_sho":"春琴、ほんとうの名は鵙屋琴、大阪｜道修町の薬種商の生れで歿年は明治十九年十月十四日、墓は市内下寺町の浄土宗の某寺にある。せんだって通りかかりにお墓参りをする気になり立ち寄って案内を乞うと「鵙屋さんの墓所はこちらでございます」といって寺男が本堂のうしろの方へ連れて行った。見るとひと叢の椿の木かげに鵙屋家代々の墓が数基ならんでいるのであったが琴女の墓らしいものはそのあたりには見あたらなかった。むかし鵙屋家の娘にしかじかの人があったはずですがその人のはというとしばらく考えていて「それならあれにありますのがそれかも分りませぬ」と東側の急な坂路になっている段々の上へ連れて行く。知っての通り下寺町の東側のうしろには生国魂神社のある高台が聳えているので今いう急な坂路は寺の境内からその高台へつづく斜面なのであるが、そこは大阪にはちょっと珍しい樹木の繁った場所であって琴女の墓はその斜面の中腹を平らにしたささやかな空地に建っていた。",
# "ningen_shikkaku":"私は、その男の写真を三葉、見たことがある。一葉は、その男の、幼年時代、とでも言うべきであろうか、十歳前後かと推定される頃の写真であって、その子供が大勢の女のひとに取りかこまれ、（それは、その子供の姉たち、妹たち、それから、従姉妹たちかと想像される）庭園の池のほとりに、荒い縞の袴をはいて立ち、首を三十度ほど左に傾け、醜く笑っている写真である。醜く？けれども、鈍い人たち（つまり、美醜などに関心を持たぬ人たち）は、面白くも何とも無いような顔をして、「可愛い坊ちゃんですね」といい加減なお世辞を言っても、まんざら空お世辞に聞えないくらいの、謂わば通俗の「可愛らしさ」みたいな影もその子供の笑顔に無いわけではないのだが、しかし、いささかでも、美醜に就いての訓練を経て来たひとなら、ひとめ見てすぐ、「なんて、いやな子供だ」と頗る不快そうに呟き、毛虫でも払いのける時のような手つきで、その写真をほうり投げるかも知れない。"
"red_watashi":"私は赤よ。",
"red_warawa":"わらわは赤です。",
"red_boku":"僕は赤です。",
"red_ore":"オレは赤だ。",
"green_watashi":"私は緑よ。",
"green_warawa":"わらわは緑です。",
"green_boku":"僕は緑です。",
"green_ore":"オレは緑だ。",
"blue_watashi":"私は青よ。",
"blue_warawa":"わらわは青です。",
"blue_boku":"僕は青です。",
"blue_ore":"オレは青だ。",
}


voice_names = [
# "ja-JP-Standard-A",
# "ja-JP-Standard-B",
# "ja-JP-Standard-C",
# "ja-JP-Standard-D",
"ja-JP-Wavenet-A",
"ja-JP-Wavenet-B",
"ja-JP-Wavenet-C",
"ja-JP-Wavenet-D",
]

def outputmp3(voice_text_key, voice_text, voice_name):
  output_file_name = voice_text_key+"_"+voice_name + ".mp3"
  print(output_file_name)

  # Instantiates a client
  client = texttospeech.TextToSpeechClient()

  # Set the text input to be synthesized
  synthesis_input = texttospeech.SynthesisInput(text=voice_text)

  # Build the voice request, select the language code ("en-US") and the ssml
  # voice gender ("neutral")
  voice = texttospeech.VoiceSelectionParams(
      # language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    language_code="ja-JP", name = voice_name
  )

  # Select the type of audio file you want returned
  audio_config = texttospeech.AudioConfig(
      audio_encoding=texttospeech.AudioEncoding.MP3
  )

  # Perform the text-to-speech request on the text input with the selected
  # voice parameters and audio file type
  response = client.synthesize_speech(
      input=synthesis_input, voice=voice, audio_config=audio_config
  )

  # The response's audio_content is binary.
  with open(output_file_name, "wb") as out:
      # Write the response to the output file.
      out.write(response.audio_content)
      print('Audio content written to file "', output_file_name, '"')

# voice_text_index = 3
# voice_text = list(voice_texts.values())[voice_text_index]
# voice_text_key = list(voice_texts.keys())[voice_text_index]
# for voice_name in voice_names:
#   outputmp3(voice_text_key, voice_text, voice_name)

voice_text_index = 0
for voice_text_key, voice_text in voice_texts.items():
  voice_name=voice_names[voice_text_index%4]
  outputmp3(voice_text_key, voice_text, voice_name)
  voice_text_index += 1


exit()
