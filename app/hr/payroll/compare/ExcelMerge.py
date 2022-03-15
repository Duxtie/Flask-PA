import os

import pandas as pd


class ExcelCompare:

    def __init__(self, files=[], columns=[], files_dir='', save_dir='', seperate_duplicates=True):
        self.files = files
        self.desired_columns = columns
        self.df_total = pd.DataFrame(columns=self.desired_columns)
        self.save_dir = save_dir

        self.make_save_dir(save_dir)

        if files_dir is not '':
            self.get_dir_files(files_dir)

    # make file save directory
    def make_save_dir(self, save_path):
        if not os.path.exists(save_path):
            os.makedirs(save_path, exist_ok=True)

    # read directory and get files
    def get_dir_files(self, files_dir):
        self.files = os.listdir(files_dir)

    def merge_files(self):
        desired_columns = self.desired_columns
        for file in self.files:
            try:
                df_file = pd.read_excel(file)
            except Exception:
                df_file = pd.read_csv(file)

            for column in desired_columns:
                if column not in df_file.columns:
                    df_file[column] = ''

            df_file['file'] = file
            if set(desired_columns).issubset(df_file.columns):
                selected_columns = df_file.loc[:, desired_columns]
                self.df_total = pd.concat([selected_columns, self.df_total], ignore_index=True)
            else:
                print(file)
