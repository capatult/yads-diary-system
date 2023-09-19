def make_snippet(string):
    words = string.split()
    snippet = " ".join(words[:5])
    if len(words) > 5:
        snippet += "..."
    return snippet

def count_words(string):
    return len(string.split())