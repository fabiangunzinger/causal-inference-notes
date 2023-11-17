import numpy as np
import pandas as pd


def _extract_idx(s, start, end):
    """Returns cleaned up version of s[start:end].

    Useful to read .dat datasets used in ThinkStats.
    """
    return (
        s.str[start:end]
        .replace("^\s*$", np.nan, regex=True)
        .str.strip()
    )


def read_birth_data():
    """Returns cleaned birth data used in ThinkStats.
    
    Data is based on Dunn (1999), A Simple Dataset for Demonstrating 
    Common Distributions.
    
    Columns:
    --------
    time    Time of birth recorded on the 24-hour clock
    sex     Sex of the child (1 = girl, 2 = boy)
    weight  Birth weight in grams
    mam     Number of minutes after midnight of each birth
    """
    fp = './data/babyboom.dat'
    return (
        pd.read_table(fp, header=None, skiprows=59, names=["line"])
        .assign(
            time=lambda df: _extract_idx(df.line, 0, 8).astype(object),
            sex=lambda df: _extract_idx(df.line, 9, 16).astype(int),
            weight=lambda df: _extract_idx(df.line, 17, 24).astype(int),
            mam=lambda df: _extract_idx(df.line, 25, 32).astype(int),
        )
        .drop(columns="line")
    )


def read_pregnancy_data(cleaned=False):
    """Returns cleaned pregnancy data used in ThinkStats.
    
    Data is cycle 6 of the CDC's National Survey of Family Growth (NSFG).
    Cleaning operations based on: https://github.com/AllenDowney/ThinkStats2/blob/
    f9c94d132df8e152ae7f9bca95b5d87122ae5d4a/code/nsfg.py#L54

    Columns:
    --------
    caseid      Respondent id
    babygirl    Indicator for baby sex (0 = boy, 1 = girl)
    birthord    Birth order
    prglength   Duration of complete pregnancy in weeks
    birthwgt    Birthweight in kg
    outcome     Outcome of pregnancy (1 = life birth)
    agepreg     Age at pregnancy outcome
    firstborn   Indicator for firstborn baby
    """
    fp = "./data/2002FemPreg.dat.gz"
    df = (
        pd.read_table(fp, header=None, names=["line"])
        .assign(
            caseid=lambda df: _extract_idx(df.line, 0, 12).astype(int),
            babygirl=lambda df: _extract_idx(df.line, 55, 56).astype(float),
            birthord=lambda df: _extract_idx(df.line, 277, 279).astype(float),
            prglength=lambda df: _extract_idx(df.line, 274, 276).astype(int),
            birthwgt_lb=lambda df: _extract_idx(df.line, 56, 58).astype(float),
            birthwgt_oz=lambda df: _extract_idx(df.line, 59, 61).astype(float),
            birthwgt=lambda df: _extract_idx(df.line, 56, 58).astype(float),
            outcome=lambda df: _extract_idx(df.line, 276, 277).astype(int),
            agepreg=lambda df: _extract_idx(df.line, 283, 285).astype(float),
        )
        .assign(
            firstborn=lambda df: df.birthord.eq(1).astype(int),
            babygirl=lambda df: df.babygirl.replace([7, 9], np.nan).eq(1).astype(float),
            # replace bogus weights and "don't ascertained" (97), "refused" (98), etc.
            birthwgt_lb=lambda df: df.birthwgt_lb.where(df.birthwgt_lb < 20),
            birthwgt_oz=lambda df: df.birthwgt_oz.where(df.birthwgt_lb < 20),
            # create single birthwgt in kg
            birthwgt=lambda df: (df.birthwgt_lb + df.birthwgt_oz / 16) / 2.205,
        )
        .drop(columns=["line", "birthwgt_lb", "birthwgt_oz"])
    )
    if cleaned:
        df = df.loc[
            df.prglength.between(20, 45)
            & df.birthwgt.between(1, 10)
            & df.agepreg.between(16, 50)
            & df.outcome.eq(1)
        ]
        
    return df