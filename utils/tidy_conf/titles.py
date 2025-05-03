import re

from tidy_conf.yaml import load_title_mappings
from tqdm import tqdm


def tidy_titles(data):
    """Tidy up conference titles by replacing misspellings and alternative names."""
    spellings, alt_names = load_title_mappings()
    for i, q in tqdm(enumerate(data.copy()), total=len(data)):
        if "conference" in q:
            low_conf = q["conference"].lower().strip()
            # Replace common misspellings
            for spelling in spellings:
                if spelling.lower() in low_conf:
                    # Find the index in the lower case string and replace it in the original string
                    index = low_conf.index(spelling.lower())
                    q["conference"] = q["conference"][:index] + spelling + q["conference"][index + len(spelling) :]

            for key, values in alt_names.items():
                global_name = values.get("global")
                variations = values.get("variations", [])
                regexes = values.get("regexes", [])

                # Match global name
                if global_name and global_name.lower().strip() == low_conf:
                    if "alt_name" not in q:
                        q["alt_name"] = global_name.strip()
                    continue

                # Match variations
                for variation in variations:
                    if (
                        (variation.lower().strip() == low_conf)
                        or (variation.lower().strip().replace(" ", "") == low_conf)
                        or (variation.lower().strip().replace("Conference", "") == low_conf)
                    ):
                        if "alt_name" not in q and q["conference"].strip() != key:
                            q["alt_name"] = q["conference"].strip()
                        q["conference"] = key.strip()
                        break

                # Match regex patterns
                for regex in regexes:
                    if re.match(regex, low_conf):
                        if "alt_name" not in q and q["conference"].strip() != key:
                            q["alt_name"] = q["conference"].strip()
                        q["conference"] = key.strip()
                        break

            data[i] = q
    return data


def tidy_df_names(df):
    """Tidy up the conference names in a consistent way."""
    # Load known title mappings
    _, known_mappings = load_title_mappings(reverse=True)

    # Define regex patterns for matching years and conference names
    regex_year = re.compile(r"\b\s+(19|20)\d{2}\s*\b")
    regex_py = re.compile(r"\b(Python|PyCon)\b")

    # Harmonize conference titles using known mappings and regex
    series = df["conference"]

    # Remove years from conference names
    series = series.str.replace(regex_year, "", regex=True)

    # Add a space after Python or PyCon
    series = series.str.replace(regex_py, r" \1 ", regex=True)

    # Replace non-word characters
    series = series.str.replace(r"[\+]", " ", regex=True)

    # Replace the word Conference
    series = series.str.replace(r"\bConf \b", "Conference ", regex=True)

    # Remove extra spaces
    series = series.str.replace(r"\s+", " ", regex=True)

    # Replace known mappings
    series = series.replace(known_mappings)

    # Remove leading and trailing whitespace
    series = series.str.strip()

    df.loc[:, "conference"] = series

    return df
