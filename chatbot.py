import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

class LegalChatbot:
    def _init_(self, csv_path):
        self.data = pd.read_csv(csv_path)
        self.data.fillna("", inplace=True)
        self.data.columns = self.data.columns.str.strip()
        self.data['search_blob'] = (
            self.data['pet'] + " " +
            self.data['res'] + " " +
            self.data['pet_adv'] + " " +
            self.data['res_adv'] + " " +
            self.data['bench']
        )
        self.vectorizer = TfidfVectorizer()
        self.case_vectors = self.vectorizer.fit_transform(self.data['search_blob'])

        # Load Hugging Face model
        self.gen_model = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

    def get_case_match(self, user_input):
        input_vec = self.vectorizer.transform([user_input])
        similarity = cosine_similarity(input_vec, self.case_vectors)
        best_match_idx = similarity.argmax()
        result = self.data.iloc[best_match_idx]
        return {
            "case_no": result["case_no"],
            "pet": result["pet"],
            "res": result["res"],
            "pet_adv": result["pet_adv"],
            "res_adv": result["res_adv"],
            "bench": result["bench"],
            "judgement_by": result["judgement_by"],
            "judgment_dates": result["judgment_dates"],
            "link": result["temp_link"]
        }

    def get_ai_advice(self, user_query):
        # Modify prompt to consider user situation (e.g., accident)
        prompt = (
            f"A person described the following legal issue: '{user_query}'. "
            "The issue is related to an accident on the road. "
            "Provide a structured legal response for the user that includes the following: "
            "- Legal procedures the person should take. "
            "- Required documentation. "
            "- Sections of the law that apply (e.g., Motor Vehicle Act, Indian Penal Code). "
            "- Penalties and fines that the person who caused the accident may face."
        )

        # Generate advice based on the prompt
        response = self.gen_model(prompt, max_length=300, do_sample=True, temperature=0.7)
        return response[0]["generated_text"]