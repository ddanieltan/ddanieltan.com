import re
import random
from datetime import datetime
random.seed(datetime.now())

quotes = [
    "The reward for good work is more work - Tom Sach",
    "3 things tell a man. His eyes, his friends and his favourite quotes - Immanuel Kant",
    "We are not given a short life but we make it short, we are not ill-supplied but wasteful of it. Life is long if you know how to use it. - Seneca",
    "There are 2 ways of spreading light. Be the candle or the mirror that reflects it - Edith Wharton",
    "The statistician cannot evade the responsibility for understanding the process he applies or recommends - Ronald Fisher",
    "Sucking at something is the 1st step to being sorta good at something - Jake the Dog",
    "Reading furnishes the mind only with materials of knowledge. It is thinking that makes what we read ours - John Locke",
    "Die trying - Van Neistat"
    ]
randomQuote = random.choice(quotes)

with open("_quarto.yml","r") as f:
    pattern = r'page-footer: "(.+?)"'
    contents = f.read()
    contents = re.sub(pattern,f'page-footer: "{randomQuote}"',contents)

with open("_quarto.yml","w") as f:
    f.write(contents)

print(f"""Quote selected:
{randomQuote}
""")



