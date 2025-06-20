from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text =  """
Artificial intelligence (AI) is one of the most transformative technologies of the 21st century. It refers to the simulation of human intelligence in machines that are programmed to think, learn, and make decisions. The field of AI has seen tremendous growth over the past few decades, thanks to advancements in computing power, the availability of large datasets, and breakthroughs in machine learning algorithms. Today, AI is embedded in our daily lives—from virtual assistants like Siri and Alexa to recommendation systems on Netflix and YouTube, and even in self-driving cars.

The applications of AI span across various industries. In healthcare, AI is used for disease diagnosis, drug discovery, and personalized treatment plans. In finance, AI algorithms can detect fraud, automate trading, and provide personalized banking experiences. In the field of education, intelligent tutoring systems adapt to individual student needs and learning styles. Moreover, AI has played a crucial role in addressing global challenges, such as climate modeling, pandemic forecasting, and disaster response.

Despite its benefits, AI also raises ethical and societal concerns. Issues such as data privacy, algorithmic bias, and the potential for job displacement have sparked debates among policymakers, technologists, and the public. It is essential to develop AI responsibly by ensuring transparency, fairness, and accountability in its design and deployment. Governments and organizations worldwide are now working on regulations and ethical guidelines to govern the development and use of AI technologies.

In the future, AI is expected to become even more integrated into our lives, augmenting human capabilities and creating new possibilities. However, the path forward must be paved with careful consideration of both the opportunities and risks associated with this powerful technology.
"""

summary = summarizer(text)
print(summary[0]['summary_text'])











