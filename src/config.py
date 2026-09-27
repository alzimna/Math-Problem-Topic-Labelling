from pathlib import Path

topic2label = {
    'Algebra':0,
    'Combinatorics':1,
    'Geometry':2,
    'Number Theory':3
}

label2topic = {
    0 : 'Algebra',
    1 : 'Combinatorics',
    2 : 'Geometry',
    3 : 'Number Theory'
}

train_url = "https://github.com/alzimna/Math-Problem-Topic-Labelling/raw/refs/heads/main/data/train.csv"
test_url = "https://github.com/alzimna/Math-Problem-Topic-Labelling/raw/refs/heads/main/data/test.csv"
solution_url = "https://github.com/alzimna/Math-Problem-Topic-Labelling/raw/refs/heads/main/data/solution.csv"

RAW_PATH = Path("../raw")
OUTPUT_PATH = Path("../output")
CONTESTS = ['AHSME', 'AIME', 'AMC_10', 'AMC_12', 'AMC_8', 'USAJMO', 'USAMO']