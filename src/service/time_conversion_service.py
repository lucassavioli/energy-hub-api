from datetime import datetime


def iso_format_to_unix_time(iso_format_string):
    return __unix_time_of(datetime.fromisoformat(iso_format_string))


def __unix_time_of(dt):
    return int((dt - datetime(1970, 1, 1)).total_seconds())


def time_elapsed_in_hours(earliest_unix_timestamp, latest_unix_timestamp):
    return (latest_unix_timestamp - earliest_unix_timestamp) / 3600


def calculate_time_elapsed(readings):
    min_time = min(map(lambda r: r.time, readings))
    max_time = max(map(lambda r: r.time, readings))
    return time_elapsed_in_hours(min_time, max_time)
