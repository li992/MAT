# MAT
Multi-dimensional Analysis Tool is a Python program for analyzing the language structure of the text and conducting a five-dimensional assessment based on Douglas Bieber's [theory](https://www.uni-bamberg.de/fileadmin/eng-ling/fs/Chapter_21/Index.html?Dimensionscores.html)

## Installation
The program needs to run in the [Python3](https://www.python.org/downloads/) environment

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [stanza](https://stanfordnlp.github.io/stanza/) and [selenium](https://selenium-python.readthedocs.io/installation.html) packages

```bash
pip install stanza
pip install selenium
```

## Usage
To run tagger-algo.py program, you should first create a MergedFiles folder under the same directory and copy the text files to MergedFiles folder.

For Windows user:

```bash
C:\Users\User\Desktop\MAT> py tagger-algo.py
```

tagger-algo.py will create two parsed files (one file with stanford tagger tags and one file with modified tags) and store them into Results\StanfordTags and Results\ModifiedTags

Once tagger-algo.py finishes its job, you can use tagger-count to create field scores and dimension scores

```bash
C:\Users\User\Desktop\MAT> py tagger-count.py
```

The output will also be stored in Results folder.

## Field Abbreviation
| Abbreviation | Full |
| --- | --- |
| AMP | Amplifiers |
| ANDC | Independent clause coordination |
| AWL | Word length |
| CAUS | Causative adverbial subordinators |
| CONC | Concessive adverbial subordinators |
| COND | Conditional adverbial subordinators |
| CONJ | Conjuncts |
| DEMO | Demonstratives |
| DEMP | Demonstrative pronouns |
| DPAR | Discourse particles |
| DWNT | Downtoners |
| EMPH | Emphatics |
| EX | Existential there |
| FPP1 | First person pronouns |
| GER | Gerunds |
| HDG | Hedges |
| INPR | Indefinite pronouns |
| JJ | Attributive adjectives |
| NEMD | Necessity modals |
| NN | Total other nouns |
| NOMZ | Nominalization |
| OSUB | Other adverbial subordinators |
| PHC | Phrasal coordination |
| PIN | Total prepositional phrases |
| PIT | Pronoun it |
| PLACE | Place adverbials |
| POMD | Possibility modals |
| PRED | Predicative adjectives |
| PRMD | Predictive modals |
| RB | Total adverbs |
| SPP2 | Second person pronouns |
| SYNE | Sunthetic negation |
| THAC | That adjective complements |
| THVC | That verb complements |
| TIME | Time adverbials |
| TO | Infinitives |
| TOBJ | That relative clauses on object position |
| TPP3 | Third person pronouns |
| TSUB | That relative clauses on subject position |
| TTR | Type-token ratio |
| VBD | Past tense |
| VPRT | Present tense |
| XX0 | Analytic negation |
| BEMA | Be as main verb |
| BYPA | By-passives |
| CONT | Contractions |
| PASS | Agentless passives |
| PASTP | Past participial clauses |
| PEAS | Prefect aspect |
| PIRE | Pied-piping relative clauses |
| PRESP | Present participial clauses |
| PRIV | Private verbs |
| PROD | Pro-verb do |
| PUBV | Public verbs |
| SERE | Sentence relatives |
| SMP | Seem / appear |
| SPAU | Split auxiliaries |
| SPIN | Split infinitives |
| STPR | Stranded preposition |
| SUAV | Suasive verbs |
| THATD | Subordinator that deletion |
| WHCL | WH-clauses |
| WHOBJ | WH relative clauses on object position |
| WHQU | Direct WH-questions |
| WHSUB | WH relative clauses on subject position |
| WZPAST | Past participial WHIZ deletion relatives |
| WZPRES | Present participial WHIZ deletion relatives |

## License
[Apache License](https://www.apache.org/licenses/LICENSE-2.0.html)


