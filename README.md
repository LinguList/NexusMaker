# NexusMaker

## Simply Generate Nexus Files

```
from nexusmaker import NexusMaker, Record


data = [
    Record(language="A", word="eye", item="", cognate="1"),
    Record(language="A", word="leg", item="", cognate="1"),
    Record(language="A", word="arm", item="", cognate="1"),
    
    Record(language="B", word="eye", item="", cognate="1"),
    Record(language="B", word="leg", item="", cognate="2"),
    Record(language="B", word="arm", item="", cognate="2"),
    
    Record(language="C", word="eye", item="", cognate="1"),
    # No Record for C 'leg'
    Record(language="C", word="arm", item="", cognate="3"),

    Record(language="D", word="eye", item="", cognate="1", loan=True),
    Record(language="D", word="leg", item="", cognate="1"),
    Record(language="D", word="leg", item="", cognate="2"),
    Record(language="D", word="arm", item="", cognate="2,3"),
]

maker = NexusMaker(data)

maker = NexusMakerAscertained(data)  # adds Ascertainment bias character

maker = NexusMakerAscertainedWords(data)  # adds Ascertainment character per word

maker.write(nex, filename="output.nex")


```
