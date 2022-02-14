import os
import json
import shutil
import pandas as pd

# Unpack outputs
print("Unpacking outputs...")
shutil.unpack_archive("outputs.zip", "outputs/")
print("...done!\nArchive unpacked to: outputs/\n")

# make list of all json files from all subdirs in folder output/
json_dir = "outputs/"
output_files_li = []
for (dirpath, dirnames, filenames) in os.walk(json_dir):
    output_files_li += [os.path.join(dirpath, file) for file in filenames]

json_files_li = [
    file_path for file_path in output_files_li if file_path.endswith('.json')]

# Read in Json Files, save to pandas dataframe and combine them all together
print("Reading in json files and saving to dataframe...")

dfs_li = []

for json_file in json_files_li:
    with open(json_file, encoding='utf-8') as f:
        json_data = pd.json_normalize(json.loads(f.read()))
        # Drop unneccessary comlumns here
        json_data.drop(["settings.label", "context_report", "encoded.authors_note", "encoded.memory",
                        "encoded.prompt", "encoded.requests"], axis=1, inplace=True)
    dfs_li.append(json_data)
df = pd.concat(dfs_li, sort=False)

print("...done!\n")

print("Now doing some minor data wrangling...")

# The "settings." prefix is not really needed for columns names -> rename columns
old_col_names = df.columns
new_col_names = old_col_names.str.replace("settings.", "", regex=False)
df.columns = new_col_names


# Label the 4 different prompt/memory pairs
mask_fan = df["memory"].str.contains("High Fantasy")
mask_hor = df["memory"].str.contains("Horror")
mask_rom = df["memory"].str.contains("Historical Romance")
mask_sf = df["memory"].str.contains("Hard Sci-fi")
df.loc[mask_fan, "prompt_label"] = "High Fantasy"
df.loc[mask_hor, "prompt_label"] = "Horror"
df.loc[mask_rom, "prompt_label"] = "Historical Romance"
df.loc[mask_sf, "prompt_label"] = "Hard Sci-fi"

# Label the different presets
# Temperature is enough to identify each prest so just use that
preset_temp_dict = {"Basic Coherence (14/02/2022)": 0.585, "All-Nighter (14/02/2022)": 1.33,
                    "Genesis (14/02/2022)": 0.63, "Fandango (14/02/2022)": 0.86,
                    "Low Rider (14/02/2022)": 0.94, "Ouroboros (14/02/2022)": 1.07,
                    "Morpho (14/02/2022)": 0.6889, "Ace of Spade (14/02/2022)": 1.15}

for preset in preset_temp_dict:
    mask = df["temperature"] == preset_temp_dict[preset]
    df.loc[mask, "preset_label"] = preset

# Most people will be interested in prompt_label, preset_label and result
# Let's move those to front

priority_cols = ["prompt_label", "preset_label", "result"]

i = 0
for col in priority_cols:
    df.insert(i, col, df.pop(col))
    i += 1

print("...done!\n\nCount of story genres:")
print(df["prompt_label"].value_counts())
print("\nCount of generation presets:")
print(df["preset_label"].value_counts())
print("\n")

# Save data to file
print("saving data to /dataset...")

if not os.path.exists("dataset"):
    os.mkdir("dataset")

df.to_csv("dataset/NAI_story_data.csv")
print("...done writing csv-file...")
print("...now writing excel-file...")
df.to_excel("dataset/NAI_story_data.xlsx")
print("...done!\n")
print("ALL DONE!")

