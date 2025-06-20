from textblob import TextBlob
import spacy 
import requests


class Api:
    
    def __init__(self):
        self.token="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"
    
    def sentiment(self,text):
        text1=text
        response=TextBlob(text1).sentiment
        
        polarity=round(response.polarity,2)
        subjectivity=round(response.subjectivity,2)
        
        result = {
            "polarity_score": polarity,
            "subjectivity_score": subjectivity
        }
        if polarity<0:
            result["polarity"]="Negative"
        elif polarity==0:
            result["polarity"]="Neutral"
        else:
            result["polarity"]="Positive"
            
        if 0 <= subjectivity < 0.3:
            result["subjectivity"] = "Factual"
        elif subjectivity < 0.7:
            result["subjectivity"] = "Mixed"
        else:
            result["subjectivity"] = "Opinion"      
            
        return result
    
    def ner(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        result = {}
        for ent in doc.ents:
            if ent.label_ not in result:                    
                result[ent.label_] = []
            result[ent.label_].append(ent.text)
        return result
    
    def emotion(self, text):

        API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        payload = {"inputs": text}
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code== 200:
            return response.json()
        else:
            return "Error"
        
    def summarizerapi(self, text):
        API_URL="https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers={
            "Authorization": f"Bearer {self.token}"}
        
        payload={"inputs": text}
        respose=requests.post(API_URL, headers=headers,json=payload)
        
        if respose.status_code==200:
            return respose.json()
        else:
            return "Error"
        
   

                        
            
        
        
