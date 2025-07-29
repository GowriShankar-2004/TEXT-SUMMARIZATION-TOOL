from transformers import pipeline

def summarize(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=60, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    input_text = (
        "Natural Language Processing is a critical field in modern artificial intelligence. "
        "It enables machines to understand, interpret, and generate human language, bridging the gap between humans and computers. "
        "Over the years, advancements such as transformer architectures have significantly improved the accuracy and capability of NLP models. "
        "Summarization is one of the most impactful applications of NLP, providing concise representations of lengthy documents, news, and research articles. "
        "Such tools help users quickly grasp the main ideas without reading the entire text."
    )
    print("Input Text:\n", input_text)
    print("\nSummary:\n", summarize(input_text))
