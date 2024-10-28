def extract_domain(email):
    return email.split('@')[1] if '@' in email else None
