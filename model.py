# from transformers import pipeline

# # Load the classifier model
# classifier = pipeline('text-classification', model='bert-base-uncased', tokenizer='bert-base-uncased')

# # Define the text to be classified
# text = "I really enjoyed the movie!"

# # Classify the text using the pre-trained model
# result = classifier(text)

# # Print the predicted class and its associated score
# print(f"The predicted class is {result[0]['label']} with a score of {round(result[0]['score'], 4)}")


# import json
# import requests


# # Text Classification


import config
from flask import Flask, jsonify
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import requests
import json
API_TOKEN = "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"


# API_WRITE_TOKEN = "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"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))
# data = query({"inputs": "I like you. I love you"})
# print(data)

# # Token Classification

# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# API_URL = "https://api-inference.huggingface.co/models/Davlan/distilbert-base-multilingual-cased-ner-hrl"
# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))
# data = query({"inputs": "My name is Wolfgang and I live in Berlin. I like to eat apple."})

# print("\n****** MODEL: distilbert-base-multilingual-cased-ner-hrl ******\n")
# print(data)
# print("\n")

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english"

# # open file in read mode
# file = open('1.txt', 'r')

# # read the entire contents of the file
# LONG_ARTICLE = file.read()

# # close the file
# file.close()

# LONG_ARTICLE = """
# Callius Falk looked around the throne room with thinly veiled disgust in his golden eyes. At the sound of a throat clearing, one of his brothers no doubt, he stilled himself. It wasn’t easy, but he bit back his anger.

# This was no time for pride. Callius knew what he needed to do. He exhaled and dropped soundlessly to his knees. The cold, hard floor seeped through his leather pants, but he barely felt it. His mind was on more important matters.

# He dipped his head low, placing himself at the feet of Dragomir, Chief Dragon of the Blackthorne Clan. His warden these last five centuries. It was symbolic of his subservience to the tyrant.

# True, he was the stronger of the two, but he’d never get the chance to prove it. The Blackthorne Clan had over one hundred Dragons in the hold alone. Each was sworn to defend Dragomir, and each would die at his behest. Regardless of how lowly the man was. Service above all.

# Dragomir’s silver hair was his greatest prize. It hung long, way past his knees when he stood up. Seated, as he was, the glittering braid sat coiled on the embroidered rug that sat just underneath his throne. The swirling patterns of reds and golds was intricate as it was delicate.

# """

# print(LONG_ARTICLE)


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def token_classification(LONG_ARTICLE):

    data = query({"inputs": LONG_ARTICLE})

    print("\n****** MODEL: bert-large-cased-finetuned-conll03-english ******\n")
    print(data)
    print("\n")

# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))
# data = query({"inputs": "My name is Wolfgang and I live in Berlin"})

# print("\n****** MODEL: bert-base-NER ******\n")
# print(data)
# print("\n")


# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# API_URL = "https://api-inference.huggingface.co/models/westbrook/bio_gpt_ner"
# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))
# data = query({"inputs": "My name is Wolfgang and I live in Berlin"})

# print("\n****** MODEL: bio_gpt_ner ******\n")
# print(data)
# print("\n")


# # Summarizing Text

# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))
# data = query(
#     {
#         "inputs": "ChatGPT says we only need a Read token unless/until we try to create our own models. To experiment with preexisting Hugging Face models, it says we can use the Read. If we create our own models, then we can use a Write token, but for now, maybe we can experiment with Read and see how good it is. If we need to train or Few Shot train, then I we can use a Write token.",
#         "parameters": {"do_sample": False},
#     }
# )
# # data = query(
# #     {
# #         "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
# #         "parameters": {"do_sample": False},
# #     }
# # )
# print("\n****** Summarizing Text: bart-large-cnnr ******\n")
# print(data)
# # Response
# # self.assertEqual(
# #     data,
# #     [
# #         {
# #             "summary_text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world.",
# #         },
# #     ],
# # )


# # Text Generation

# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# API_URL = "https://api-inference.huggingface.co/models/gpt2"
# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))
# data = query({"inputs": "The answer to the universe is"})
# print(data)


# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ARTICLE = """
# A fireplace in the British Ministry of Magic’s international floo network flared suddenly to life, and a young woman appeared inside it, a small suitcase in hand. Her large, silver eyes were wide as the green flames died away, and she stepped out of the fireplace, taking in the high, vaulting ceiling of Ministry Atrium before looking into the crowd of wizards and witches bustling through.
# """
# print(summarizer(ARTICLE, max_length=900, min_length=300, do_sample=False))
# # [{'summary_text': 'Liana Barrientos, 39, is charged with two counts of "offering a false instrument for filing in the first degree" In total, she has been married 10 times, with nine of her marriages occurring between 1999 and 2002. She is believed to still be married to four men.'}]


def summarize_text(LONG_ARTICLE):

    # Initialize summarization pipeline0
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

    summary = ""
    
    for i in range(0, len(LONG_ARTICLE), 512):

        # Split long text into chunks of size 512
        chunk = LONG_ARTICLE[i:i+512]

        # Dynamically calculate max_length based on input_length
        input_length = len(chunk)

        # Set max_length as 150% of input_length, with a maximum limit of 1024
        max_length = min(int(input_length * 1.5), 1024)

        result = summarizer(chunk, max_length=max_length,
                            min_length=40, do_sample=False)
        if len(result) > 0:
            summary += result[0]["summary_text"] + " "

        config.progress += 1

    return summary
