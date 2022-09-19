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
    "Die trying - Van Neistat",
    "The purpose of visualization is insight, not pictures - Ben Shneiderman",
    "We try to solve very complicated problems without letting people know how complicated the problem was - Johnathan Ives",
    "There is no such thing as informational overload, just bad design. If something is cluttered or confusing, fix your design - Edward Tufte",
    "You don't understand anything until you learn it more than one way - Marvin Minsky",
    "Somewhere, something incredible is waiting to be known - Carl Sagan",
    "I am convinced the best learning takes place when the leaner takes charge - Seymour Papert",
    "We must never make experiments to confirm our ideas, but simply to control them - Claude Bernard",
    "If your experiment needs statistics, you ought to have done a better experiment - Ernest Rutherford",
    "Study hard what interests you the most in the most undisciplined, irreverent and original manner possible - Richard Feynman",
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



