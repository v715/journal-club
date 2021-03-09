# %%
import pickle
from pybtex.database import parse_file
from utils import parse_entry

# %%
BIB_FILE = "references.bib"
bib = parse_file(BIB_FILE, "bibtex")

QUEUE_FILE = "queue.txt"
with open(QUEUE_FILE, "rb") as fp:
    queue = pickle.load(fp)

# %%
with open("README.md", "a") as f:
    for entry in bib.entries.values():

        if entry.key not in queue:
            queue.append(entry.key)
            md_str = parse_entry(entry)
            f.write(md_str + "\n" + "\n")

# %%
with open(QUEUE_FILE, "wb") as fp:
    pickle.dump(queue, fp)
