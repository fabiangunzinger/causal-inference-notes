import os

import numpy as np
import pandas as pd
import pandas_gbq



def _query_data(
        query,
        project_id="just-data-expenab-dev",
        cache_path=None,
        convert_dates=None,
        ):
    """Query data from GBC or read from disk (for testing).

    Arguments:
    ----------
    query : string
        A valid BigQuery query.
    project_id : string, default "just-data-bq-users"
        Project ID to be used for query.
    cache_path: string, filepath of parquet file, default None
        Filepath to write query to (if file doesn't exist)
        or read query from (if file does exist).
    convert_dates : list of strings, default None
        List of columns to convert to datetime.
    """
    if cache_path is not None:
        if not cache_path.endswith('.parquet'):
            raise ValueError("Filepath must end with '.parquet'.")
        if os.path.isfile(cache_path):
            print("Reading data from cache...")
            result = pd.read_parquet(cache_path)
            return result
        
    print("Querying data from BigQuery...")
    result = pd.read_gbq(query, project_id=project_id)
    if cache_path is not None:
        print("Writing data to cache...")
        if convert_dates is not None:
            # Convert dates to datetime so that they can be written to parquet
            result[convert_dates] = result[convert_dates].apply(pd.to_datetime)
        result.to_parquet(cache_path, index=False)

    return result


def read_ie_data():
    query = open("sql/ie_data.sql").read()
    filepath = "/Users/fabian.gunzinger/tmp/oneweb-ie.parquet"
    df = (
        _query_data(query, cache_path=filepath, convert_dates=['date'])
        .assign(date=lambda df: pd.to_datetime(df['date']))
        .assign(conversion=lambda df: df['order_price'] > 0)
        .set_index('date', drop=False)
    )

    # Check data
    assert df.user_id.isna().sum() == 0
    assert df.date.isna().sum() == 0
    assert df.visit_key.isna().sum() == 0
    assert set(df.platform) == {'android', 'ios', 'web'}
    assert df.order_price.lt(0).sum() == 0

    return df


def add_pre_metric_value(df, metric='order_price'):
    """Add pre-period metric value for CUPED adjustment."""
    pre_period = '1 Jan 2023', '31 May 2023'
    post_period ='1 Jun 2023', ' 31 Aug 2023'
    post = (
        df.loc[slice(*post_period)]
        .groupby("user_id")
        [metric].mean()
        .astype('float32')
        .rename(f"{metric}")
        .reset_index()
    )
    pre = (
        df.loc[slice(*pre_period)]
        .groupby("user_id")
        [metric].mean()
        .astype('float32')
        .rename(f"{metric}_pre")
        .reset_index()
    )
    result = pd.merge(post, pre, how="left").dropna()
    return result

def clean_data(df):
    pass

def add_treat_effect(df, effect=1.1):
    treated = df.user_id.sample(frac=0.5, random_state=2312)
    is_treated = df.user_id.isin(treated)
    effect_map = {True: effect, False: 1}
    df["t"] = is_treated.astype(int)
    df["order_price"] = is_treated.map(effect_map) * df["order_price"]
    return df


