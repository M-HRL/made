import pandas as pd


def calc_rides_per_path(rides_per_path_df: pd.DataFrame, path_df: pd.DataFrame, total_counts_weight: float) -> tuple[
    list[int], list[int]]:
    rides_per_path_months_sr = pd.to_datetime(rides_per_path_df["start_time"]).map(
        lambda start_time: int(start_time.month))

    month_list = list(range(1, 13))
    avg_rides_per_path_per_month_list = []
    for m in month_list:
        rides_per_path_per_month_df = rides_per_path_df[rides_per_path_months_sr == m]
        num_rides_per_path_per_month_sr = rides_per_path_per_month_df["path_id"].value_counts()

        sum_rides_per_path_per_month = (num_rides_per_path_per_month_sr.sum() * total_counts_weight)
        avg_rides_per_path_per_month = sum_rides_per_path_per_month / len(path_df)

        avg_rides_per_path_per_month_list.append(avg_rides_per_path_per_month)

    return month_list, avg_rides_per_path_per_month_list
