from typing import Any

import pandas as pd


def df_to_dict(
    df: pd.DataFrame, key: str = "Key", val: str = "Value"
) -> dict[str, Any]:
    """
    Converts a DataFrame to a dictionary with column names as keys and lists of values as values.
    :param df: DataFrame to convert
    :param key: Column name to use as keys in the dictionary
    :param val: Column name to use as values in the dictionary
    :return: Dictionary representation of the DataFrame
    """
    return dict(zip(df[key], df[val], strict=True))


def decode_data(datacube_path: str) -> dict[str, Any]:
    """
    decodes the detection data to datacubes
    :param datacube_path: detection file path
    :return: decoded datacube
    """
    with open(datacube_path, "rb") as f:
        injection_info_list = []
        chromatogram_data_info_list = []
        signal_parameter_info_list = []
        chromatogram_data_list = []

        section_name = ""
        injection_info = []
        chromatogram_data_info = []
        signal_parameter_info = []
        chromatogram_data = []

        for data_line in f.read().decode("utf-8-sig").split("\n"):
            line = data_line.strip()

            if not line.endswith(":"):
                if section_name == "Injection Information":
                    injection_info.append(line.split("\t"))
                elif section_name == "Chromatogram Data Information":
                    chromatogram_data_info.append(line.split("\t"))
                elif section_name == "Signal Parameter Information":
                    signal_parameter_info.append(line.split("\t"))
                elif section_name == "Chromatogram Data":
                    chromatogram_data.append(line.split("\t"))

            if line == "Injection Information:":
                section_name = "Injection Information"
            elif line == "Chromatogram Data Information:":
                section_name = "Chromatogram Data Information"
            elif line == "Signal Parameter Information:":
                section_name = "Signal Parameter Information"
            elif line == "Chromatogram Data:":
                section_name = "Chromatogram Data"

        df_injection_info = pd.DataFrame(injection_info, columns=["Key", "Value"])
        df_chromatogram_data_info = pd.DataFrame(
            chromatogram_data_info, columns=["Key", "Value"]
        )
        df_signal_parameter_info = pd.DataFrame(
            signal_parameter_info, columns=["Key", "Value"]
        )

        headers = chromatogram_data.pop(0)
        df_chromatogram_data = pd.DataFrame(chromatogram_data, columns=headers)

        injection_info_list.append(df_injection_info)
        chromatogram_data_info_list.append(df_chromatogram_data_info)
        signal_parameter_info_list.append(df_signal_parameter_info)
        chromatogram_data_list.append(df_chromatogram_data)

    df_chromatogram_data_all = pd.concat(chromatogram_data_list)
    df_chromatogram_data_all.dropna(subset=["Time (min)", "Value (EU)"], inplace=True)

    for c in df_chromatogram_data_all.columns:
        if c == "Filename":
            continue
        df_chromatogram_data_all[c] = pd.to_numeric(
            df_chromatogram_data_all[c], errors="coerce"
        )

    df_injection_info_all = pd.concat(injection_info_list)
    df_injection_info_all = df_injection_info_all[
        df_injection_info_all["Key"].str.strip() != ""
    ].copy()
    df_chromatogram_data_info_all = pd.concat(chromatogram_data_info_list)
    df_chromatogram_data_info_all = df_chromatogram_data_info_all[
        df_chromatogram_data_info_all["Key"].str.strip() != ""
    ].copy()
    df_signal_parameter_info_all = pd.concat(signal_parameter_info_list)
    df_signal_parameter_info_all = df_signal_parameter_info_all[
        df_signal_parameter_info_all["Key"].str.strip() != ""
    ].copy()

    datacubes = {
        "injection_info": df_to_dict(df_injection_info_all),
        "chromatogram_data_info": df_to_dict(df_chromatogram_data_info_all),
        "signal_parameter_info": df_to_dict(df_signal_parameter_info_all),
        "chromatogram_data": df_chromatogram_data_all,
    }

    return datacubes
