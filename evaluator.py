import re

def evaluate_answer(answer):
    """
    Evaluate the structure and content of an interview answer.
    Returns score, feedback summary, and improvement tips.
    """
    if not answer.strip():
        return 0.0, "No answer provided.", ["Please provide an answer."]

    score = 5.0
    tips = []
    feedback = []

    word_count = len(answer.split())

    # 🟠 Short answers (<20 words)
    if word_count < 15:
        score = 3.0
        feedback.append("Answer is too short.")
        tips.append("Provide more detail and context.")
    # 🟠 Long answers (>100 words)
    elif word_count > 40:
        score = 6.0
        feedback.append("Answer is too long and may lose focus.")
        tips.append("Be more concise and focused.")

    # 🟥 Filler word penalty
    filler_words = ["like", "um", "you know", "actually", "basically"]
    if any(fw in answer.lower() for fw in filler_words):
        score -= 1
        feedback.append("Uses filler words.")
        tips.append("Avoid using filler words for clarity.")

    # ✅ Reward confident keywords
    confident_words = ["confident", "skilled", "experienced", "capable", "driven"]
    if any(cw in answer.lower() for cw in confident_words):
        score += 1
        feedback.append("Shows confidence.")
    
    # ✅ Reward real-world examples
    if re.search(r"(project|internship|experience|team|client|developed)", answer, re.IGNORECASE):
        score += 1
        feedback.append("Includes real-world example.")

    # Clamp score between 0 and 10
    score = max(0, min(10, score))

    if not feedback:
        feedback.append("Answer is structured but could be more impactful.")
        tips.extend(["Use strong examples", "Demonstrate your value", "Be specific"])

    return round(score, 1), ". ".join(feedback), tips
