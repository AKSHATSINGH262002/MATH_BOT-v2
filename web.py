import wikipedia as wp

def search(text):
    result=wp.summary(text,sentences=2)
    return result