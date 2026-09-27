import pandas as pd
from config import *

def labelling(vectorizer,model) :
    for c in CONTESTS :
        folder = RAW_PATH / c
        full_tex = folder / "full_tex.json"
        full_html = folder / "full_html.json"
        full = folder / "full.json"
        datas = [full_tex, full_html, full]

        df = pd.read_json(full_tex)
        x = df["problem_statement_tex"].apply(lambda x : x[22:])
        res_tfidf = vectorizer.transform(x)
        res = model.predict(res_tfidf)

        for data in datas :
            df = pd.read_json(data)
            df["topic"] = res
            df["topic"] = df["topic"].map(label2topic)

            folder_output = OUTPUT_PATH / c
            folder_output.mkdir(parents=True,exist_ok=True)
            if data == full_tex :
                output = folder_output / "full_tex.json"
            elif data == full_html :
                output = folder_output / "full_html.json"
            else :
                output = folder_output / "full.json"

            df.to_json(output,orient = 'records',indent = 4)
