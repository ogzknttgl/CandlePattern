import pandas as pd

BEGIN_TIMESTAMP = 1535932800000

def calculate_ratio(pattern, timestamp, data_file='candle_30m_new.csv'):
    """Calculate pattern statistics from candle data.

    Parameters
    ----------
    pattern : sequence of int
        Sequence describing the candle pattern (e.g. [1, 0, 1]).
    timestamp : int
        Unix timestamp in milliseconds corresponding to the last candle in
        the pattern.
    data_file : str, optional
        Path to the CSV file containing the candle data.

    Returns
    -------
    dict
        Dictionary with pattern occurrences and red/green ratios.
    """
    pattern = [int(i) for i in pattern]
    data = pd.read_csv(data_file)

    count = 0
    g = 0
    r = 0

    current_time = int(((timestamp - BEGIN_TIMESTAMP) / 18) / 100000)
    length_pattern = len(pattern)

    for i in range(0, current_time):
        try:
            if length_pattern == 4:
                if (
                    data['number'][i] == pattern[0] and
                    data['number'][i + 1] == pattern[1] and
                    data['number'][i + 2] == pattern[2] and
                    data['number'][i + 3] == pattern[3]
                ):
                    count += 1
                    if data['number'][i + 4] == 1:
                        g += 1
                    else:
                        r += 1
            elif length_pattern == 5:
                if (
                    data['number'][i] == pattern[0] and
                    data['number'][i + 1] == pattern[1] and
                    data['number'][i + 2] == pattern[2] and
                    data['number'][i + 3] == pattern[3] and
                    data['number'][i + 4] == pattern[4]
                ):
                    count += 1
                    if data['number'][i + 5] == 1:
                        g += 1
                    else:
                        r += 1
            elif length_pattern == 6:
                if (
                    data['number'][i] == pattern[0] and
                    data['number'][i + 1] == pattern[1] and
                    data['number'][i + 2] == pattern[2] and
                    data['number'][i + 3] == pattern[3] and
                    data['number'][i + 4] == pattern[4] and
                    data['number'][i + 5] == pattern[5]
                ):
                    count += 1
                    if data['number'][i + 6] == 1:
                        g += 1
                    else:
                        r += 1
            elif length_pattern == 7:
                if (
                    data['number'][i] == pattern[0] and
                    data['number'][i + 1] == pattern[1] and
                    data['number'][i + 2] == pattern[2] and
                    data['number'][i + 3] == pattern[3] and
                    data['number'][i + 4] == pattern[4] and
                    data['number'][i + 5] == pattern[5] and
                    data['number'][i + 6] == pattern[6]
                ):
                    count += 1
                    if data['number'][i + 7] == 1:
                        g += 1
                    else:
                        r += 1
        except KeyError:
            break
        except IndexError:
            break

    total = r + g
    ratio_green = (g / total) * 100 if total else 0
    ratio_red = (r / total) * 100 if total else 0

    return {
        'pattern_saw': count,
        'green_num': g,
        'red_num': r,
        'ratio_green': ratio_green,
        'ratio_red': ratio_red,
    }
