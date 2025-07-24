from pathlib import Path
import pandas as pd
import json

def categories_mandril(input_file, output_dir):
    '''
    Convert the .csv to json file (updates index) to seed database
    
    Args:
        input_file: Path for csv file
        output_dir: Output directory for files (categories.json)
        
    Returns:
        void    
    '''
    
    output_dir = Path(output_dir)
    
    df = pd.read_csv(input_file, usecols=lambda x: x != "id")

    # This Line is necessary because index starts in 1 (postgres serial smallint)
    df["parent_id"] = df["parent_id"].apply(lambda x: x + 1)

    df = df.astype({"parent_id": "Int64"}).rename(columns={"parent_id": "parentId"})

    data = df.to_dict(orient="records")

    with open(output_dir / "categories.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
