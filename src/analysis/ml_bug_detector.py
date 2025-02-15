from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

class MLBugDetector:
    """
    Detects bugs in Python code using a pre-trained CodeBERT model.
    """

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "microsoft/codebert-base", num_labels=2  # Binary classification: Buggy or Not
        )

    def predict_buggy_code(self, code: str):
        """Predicts whether the given code snippet has potential bugs."""
        inputs = self.tokenizer(code, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        confidence_buggy = probs[0][1].item()
        return f"⚠️ Bug Detected! Confidence: {confidence_buggy:.2f}" if confidence_buggy > 0.5 else "✅ Code Looks Good!"

# Example 
if __name__ == "__main__":
    sample_code = """
def add_numbers(a, b):
    return a + c  # Intentional bug: 'c' undefined
"""
    ml_detector = MLBugDetector()
    print("Bug Prediction:\n", ml_detector.predict_buggy_code(sample_code))
