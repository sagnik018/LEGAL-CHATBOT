def generate_response(user_input):
    if "accident" in user_input.lower():
        return (
            "📝 *Steps to File a Case:*\n"
            "1. File an FIR at the nearest police station.\n"
            "2. Collect all evidence, including medical reports and witness statements.\n"
            "3. Contact a lawyer to draft a case.\n"
            "4. Submit the case to the court.\n\n"
            "📜 *Applicable Sections:*\n"
            "1. Section 279 - Rash driving or riding on a public way.\n"
            "2. Section 338 - Causing grievous hurt by act endangering life or personal safety.\n"
            "3. Section 304A - Causing death by negligence (if applicable).\n\n"
            "💰 *Possible Fines:*\n"
            "1. Fine up to ₹1,000 - ₹5,000 or imprisonment for 6 months (Section 279).\n"
            "2. Fine up to ₹1,000 or imprisonment for 2 years (Section 338).\n"
            "3. Fine up to ₹2,000 or imprisonment for 2 years (Section 304A).\n\n"
            "⚖ *Predicted Outcome:*\n"
            "The outcome depends on the evidence, severity of injuries, and court proceedings. "
            "You may receive compensation for damages if proven in court."
        )
    else:
        return "⚖ I can assist you with accident cases, fines, and legal guidance. Please be more specific with your question."