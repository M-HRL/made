import pandas as pd


def calc_share_paths_per_ride(num_paths_per_ride_df: pd.DataFrame, num_edges_per_ride_df: pd.DataFrame,
                              ride_df: pd.DataFrame) -> tuple[list[int], list[float]]:
    num_paths_months_sr = pd.to_datetime(num_paths_per_ride_df["start_time"]).map(
        lambda start_time: int(start_time.month))
    num_edges_months_sr = pd.to_datetime(num_edges_per_ride_df["start_time"]).map(
        lambda start_time: int(start_time.month))
    ride_months_sr = pd.to_datetime(ride_df["start_time"]).map(lambda start_time: int(start_time.month))

    month_list = list(range(1, 13))
    avg_share_paths_per_ride_per_month_list = []
    for m in month_list:
        num_paths_per_month_df = num_paths_per_ride_df[num_paths_months_sr == m]
        num_edges_per_month_df = num_edges_per_ride_df[num_edges_months_sr == m]
        rides_per_month_df = ride_df[ride_months_sr == m]

        num_edges_per_month_sub_df = num_edges_per_month_df.loc[num_paths_per_month_df.index]

        num_paths_per_month_df = num_paths_per_month_df[num_edges_per_month_sub_df["num_edges"] != 0]
        num_edges_per_month_sub_df = num_edges_per_month_sub_df[num_edges_per_month_sub_df["num_edges"] != 0]

        ride_share_paths_per_ride_per_month_sr = (
                num_paths_per_month_df["num_paths"] / num_edges_per_month_sub_df["num_edges"])
        avg_share_paths_per_ride_per_month = ride_share_paths_per_ride_per_month_sr.sum() / len(rides_per_month_df)

        avg_share_paths_per_ride_per_month_list.append(avg_share_paths_per_ride_per_month * 100)

    return month_list, avg_share_paths_per_ride_per_month_list
