import os
from pathlib import Path

import pandas as pd
from flask.globals import _request_ctx_stack

from etas import config

try:
    from flask import _app_ctx_stack
except ImportError:
    _app_ctx_stack = None

app_stack = _app_ctx_stack or _request_ctx_stack




# APP_DIR = os.path.dirname('/')
#
# # define parameters
# base_path = './data/initial/'
#
# # path to files
# # path_old=Path(r'C:\Users\owner\Documents\old.xlsx')
# # path_new=Path(r'C:\Users\owner\Documents\new.xlsx')
#
# jan_path = base_path + 'JAN 2019 NPF Payroll Analysis'
# path_old = base_path + 'JAN 2020 NPF Payroll Analysis/LAGOS STATE COMMAND.xlsx'
# path_new = base_path + 'FEB 2020 NPF Payroll Analysis/LAGOS STATE COMMAND.xlsx'
#
# # list of key column(s)
# key = ['STAFF ID']
# # sheets to read in
# sheet = 'Sheet1'
#
# # Read in the two excel files and fill NA
# old = pd.read_excel(path_old).fillna(0)
# new = pd.read_excel(path_new).fillna(0)
#
# profile_columns = ['EMPLOYEE NAME', 'JOB TITLE', 'BANK NAME', 'ACCOUNT NUMBER', 'GRADE', 'STEP', 'LOCATION',
#                    'DEPARTMENT', 'PFA NAME', 'PIN NO']
# payroll_columns = ['BASIC SALARY', 'TOTAL ALLOWANCE', 'TOTAL GROSS', 'PENSION', 'P.A.Y.E', 'TOTAL DEDUCTION',
#                    'TOTAL NETPAY']
# columns = profile_columns + payroll_columns
#
# # set index
# old = old[columns + key]
# new = new[columns + key]
#
# try:
#     old[columns - key].astype(float)
#     new[columns - key].astype(float)
# except Exception:
#     ''
#
# # set index
# old = old.set_index(key)
# new = new.set_index(key)
#
# # identify dropped rows and added (new) rows
# dropped_rows = set(old.index) - set(new.index)
# added_rows = set(new.index) - set(old.index)
#
# # combine data
# df_all_changes = pd.concat([old, new], axis='columns', keys=['old', 'new'], join='inner')
#
#
# # prepare functio for comparing old values and new values
# def report_diff(x):
#     return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x) \
#         if not isinstance(x[0], float) and not isinstance(x[1], float) else '{} ---> {}'.format(
#         *[str(x[0]), str(x[1])]) + ' = ' + str(x[0] - x[1])
#
#
# def report_diff_modified(x):
#     if x[0] == x[1]:
#         return '{} ---> {}'.format(*x)
#
#     # if isinstance(x[0], int) and isinstance(x[1], int):
#
#
# # swap column indexes
# df_all_changes = df_all_changes.swaplevel(axis='columns')[new.columns[0:]]
#
# # apply the report_diff function
# df_changed = df_all_changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis=1))
#
# # create a list of text columns (int columns do not have '{} ---> {}')
# df_changed_text_columns = df_changed.select_dtypes(include='object')
#
# # convert dataframs columns datatype to string
# df_changed_text_columns = df_changed_text_columns.applymap(str)
# df_diff_columns = df_changed_text_columns[
#     df_changed_text_columns.apply(lambda x: x.str.contains("--->") == True, axis=1)]
# # df_diff_columns = df_diff_columns.replace('~', '', regex=False)
#
# # drop empty columns and create 3 datasets:
# # diff - contains the differences
# # dropped - contains the dropped rows
# # added - contains the added rows
# diff = df_diff_columns.dropna(how='all')
# dropped = old.loc[dropped_rows]
# added = new.loc[added_rows]
#
# # create a name for the output excel file
# full_name = './data/initial/' + '{} vs {}.xlsx'.format(Path(path_old).stem, Path(path_new).stem)
#
# diff_sheet_label = 'Variations'
# added_sheet_label = 'Added Records'
# dropped_sheet_label = 'Dropped Records'
#
# # write dataframe to excel
# writer = pd.ExcelWriter(full_name, engine='xlsxwriter')
# diff.to_excel(writer, sheet_name=diff_sheet_label, index=True)
# added.to_excel(writer, sheet_name=added_sheet_label, index=True)
# dropped.to_excel(writer, sheet_name=dropped_sheet_label, index=True)
#
# # get xlswriter objects
# workbook = writer.book
# worksheet = writer.sheets[diff_sheet_label]
# # worksheet.hide_gridlines(2)
# worksheet.set_default_row(15)
#
# # get number of rows of the df diff
# row_count_str = str(len(diff.index) + 1)
#
# # define and apply formats
# highligt_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color': '#dcdcdc'})
# worksheet.conditional_format('A1:ZZ' + row_count_str, {'type': 'text', 'criteria': 'containing', 'value': '--->',
#                                                        'format': highligt_fmt})
#
# # save the output
# writer.save()
# print('\nDone.\n')


# def payroll_compare():
#     APP_DIR = os.path.dirname('/')
#
#     # define parameters
#     base_path = './data/initial/'
#
#     # path to files
#     # path_old=Path(r'C:\Users\owner\Documents\old.xlsx')
#     # path_new=Path(r'C:\Users\owner\Documents\new.xlsx')
#
#     jan_path = base_path + 'JAN 2019 NPF Payroll Analysis'
#     path_old = base_path + 'JAN 2020 NPF Payroll Analysis/LAGOS STATE COMMAND.xlsx'
#     path_new = base_path + 'FEB 2020 NPF Payroll Analysis/LAGOS STATE COMMAND.xlsx'
#
#     # list of key column(s)
#     key = ['STAFF ID']
#     # sheets to read in
#     sheet = 'Sheet1'
#
#     # Read in the two excel files and fill NA
#     old = pd.read_excel(path_old).fillna(0)
#     new = pd.read_excel(path_new).fillna(0)
#
#     profile_columns = ['EMPLOYEE NAME', 'JOB TITLE', 'BANK NAME', 'ACCOUNT NUMBER', 'GRADE', 'STEP', 'LOCATION',
#                        'DEPARTMENT', 'PFA NAME', 'PIN NO']
#     payroll_columns = ['BASIC SALARY', 'TOTAL ALLOWANCE', 'TOTAL GROSS', 'PENSION', 'P.A.Y.E', 'TOTAL DEDUCTION',
#                        'TOTAL NETPAY']
#     columns = profile_columns + payroll_columns
#
#     # set index
#     old = old[columns + key]
#     new = new[columns + key]
#
#     try:
#         old[columns - key].astype(float)
#         new[columns - key].astype(float)
#     except Exception:
#         ''
#
#     # set index
#     old = old.set_index(key)
#     new = new.set_index(key)
#
#     # identify dropped rows and added (new) rows
#     dropped_rows = set(old.index) - set(new.index)
#     added_rows = set(new.index) - set(old.index)
#
#     # combine data
#     df_all_changes = pd.concat([old, new], axis='columns', keys=['old', 'new'], join='inner')
#
#     # prepare functio for comparing old values and new values
#     def report_diff(x):
#         return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x) \
#             if not isinstance(x[0], float) and not isinstance(x[1], float) else '{} ---> {}'.format(
#             *[str(x[0]), str(x[1])]) + ' = ' + str(x[0] - x[1])
#
#     def report_diff_modified(x):
#         if x[0] == x[1]:
#             return '{} ---> {}'.format(*x)
#
#         # if isinstance(x[0], int) and isinstance(x[1], int):
#
#     # swap column indexes
#     df_all_changes = df_all_changes.swaplevel(axis='columns')[new.columns[0:]]
#
#     # apply the report_diff function
#     df_changed = df_all_changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis=1))
#
#     # create a list of text columns (int columns do not have '{} ---> {}')
#     df_changed_text_columns = df_changed.select_dtypes(include='object')
#
#     # convert dataframs columns datatype to string
#     df_changed_text_columns = df_changed_text_columns.applymap(str)
#     df_diff_columns = df_changed_text_columns[
#         df_changed_text_columns.apply(lambda x: x.str.contains("--->") == True, axis=1)]
#     # df_diff_columns = df_diff_columns.replace('~', '', regex=False)
#
#     # drop empty columns and create 3 datasets:
#     # diff - contains the differences
#     # dropped - contains the dropped rows
#     # added - contains the added rows
#     diff = df_diff_columns.dropna(how='all')
#     dropped = old.loc[dropped_rows]
#     added = new.loc[added_rows]
#
#     # create a name for the output excel file
#     full_name = './data/initial/' + '{} vs {}.xlsx'.format(Path(path_old).stem, Path(path_new).stem)
#
#     diff_sheet_label = 'Variations'
#     added_sheet_label = 'Added Records'
#     dropped_sheet_label = 'Dropped Records'
#
#     # write dataframe to excel
#     writer = pd.ExcelWriter(full_name, engine='xlsxwriter')
#     diff.to_excel(writer, sheet_name=diff_sheet_label, index=True)
#     added.to_excel(writer, sheet_name=added_sheet_label, index=True)
#     dropped.to_excel(writer, sheet_name=dropped_sheet_label, index=True)
#
#     # get xlswriter objects
#     workbook = writer.book
#     worksheet = writer.sheets[diff_sheet_label]
#     # worksheet.hide_gridlines(2)
#     worksheet.set_default_row(15)
#
#     # get number of rows of the df diff
#     row_count_str = str(len(diff.index) + 1)
#
#     # define and apply formats
#     highligt_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color': '#dcdcdc'})
#     worksheet.conditional_format('A1:ZZ' + row_count_str, {'type': 'text', 'criteria': 'containing', 'value': '--->',
#                                                            'format': highligt_fmt})
#
#     # save the output
#     writer.save()
#     print('\nDone.\n')


class PayrollCompare:
    key = []
    columns = []
    sheet = ''
    old = ''
    new = ''
    path_old = ''
    path_new = ''
    base_path = ''

    def __init__(self, old_file='', new_file='', columns=[], key='', sheet='Sheet1'):
        self.set_key(key)
        self.set_sheet(sheet)
        self.get_file(old_file, new_file).to_data_frame().to_data_frame()
        self.set_columns(columns)
        self.set_index()

    def get_file(self, old_file, new_file):
        self.base_path = config.UPLOAD_FOLDER

        self.path_old = self.base_path + old_file
        self.path_new = self.base_path + new_file
        return self

    def set_key(self, value):
        self.key = [value]

    def set_sheet(self, value):
        self.sheet = value

    def to_data_frame(self):
        try:
            # Read in the two excel files and fill NA
            self.old = pd.read_excel(self.path_old).fillna(0)
            self.new = pd.read_excel(self.path_new).fillna(0)
        except Exception:
            # Read in the two excel files and fill NA
            self.old = pd.read_csv(self.path_old).fillna(0)
            self.new = pd.read_csv(self.path_new).fillna(0)
        return self

    def compare(self):

        self.identify_dropped_rows()

        # combine data
        df_all_changes = pd.concat([self.old, self.new], axis='columns', keys=['old', 'new'], join='inner')

        # swap column indexes
        df_all_changes = df_all_changes.swaplevel(axis='columns')[self.new.columns[0:]]

        # apply the report_diff function
        self.df_changed = df_all_changes.groupby(level=0, axis=1).apply(
            lambda frame: frame.apply(self.report_diff, axis=1))

        # create a list of text columns (int columns do not have '{} ---> {}')
        df_changed_text_columns = self.df_changed.select_dtypes(include='object')

        # convert dataframes columns datatype to string
        df_changed_text_columns = df_changed_text_columns.applymap(str)
        df_diff_columns = df_changed_text_columns[
            df_changed_text_columns.apply(lambda x: x.str.contains("--->") == True, axis=1)]

        # drop empty columns and create 3 datasets:
        # diff - contains the differences
        # dropped - contains the dropped rows
        # added - contains the added rows
        self.diff = df_diff_columns.dropna(how='all')
        self.dropped = self.old.loc[self.dropped_rows]
        self.added = self.new.loc[self.added_rows]

        # create a name for the output excel file
        full_name = self.base_path + '{} vs {}.xlsx'.format(Path(self.path_old).stem, Path(self.path_new).stem)

        diff_sheet_label = 'Variations'
        added_sheet_label = 'Added Records'
        dropped_sheet_label = 'Dropped Records'

        # write dataframe to excel
        writer = pd.ExcelWriter(full_name, engine='xlsxwriter')
        self.diff.to_excel(writer, sheet_name=diff_sheet_label, index=True)
        self.added.to_excel(writer, sheet_name=added_sheet_label, index=True)
        self.dropped.to_excel(writer, sheet_name=dropped_sheet_label, index=True)

        # get xlswriter objects
        workbook = writer.book
        worksheet = writer.sheets[diff_sheet_label]
        # worksheet.hide_gridlines(2)
        worksheet.set_default_row(15)

        # get number of rows of the df diff
        row_count_str = str(len(self.diff.index) + 1)

        # define and apply formats
        highligt_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color': '#dcdcdc'})
        worksheet.conditional_format('A1:ZZ' + row_count_str,
                                     {'type': 'text', 'criteria': 'containing', 'value': '--->',
                                      'format': highligt_fmt})

        # save the output
        writer.save()
        print('\nDone.\n')

    # prepare functio for comparing old values and new values
    def report_diff(self, x):
        return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x) \
            if not isinstance(x[0], float) and not isinstance(x[1], float) else '{} ---> {}'.format(
            *[str(x[0]), str(x[1])]) + ' = ' + str(x[0] - x[1])

    def set_index(self):
        # set index
        self.old = self.old.set_index(self.key)
        self.new = self.new.set_index(self.key)
        return self

    def identify_dropped_rows(self):
        # identify dropped rows and added (new) rows
        self.dropped_rows = set(self.old.index) - set(self.new.index)
        self.added_rows = set(self.new.index) - set(self.old.index)
        return self

    def set_columns(self, columns):
        # set columns
        self.columns = columns
        new_columns = self.columns + self.key
        self.old = self.old[new_columns]
        self.new = self.new[new_columns]

        # convert to float
        # TODO: please check this to avoid errors
        try:
            self.old[self.columns - self.key].astype(float)
            self.new[self.columns - self.key].astype(float)
        except Exception:
            ''
        return self


# key_name = 'STAFF ID'
# file1 = 'JAN 2020 NPF Payroll Analysis/KADUNA STATE COMMAND.xlsx'
# file2 = 'FEB 2020 NPF Payroll Analysis/KADUNA STATE COMMAND.xlsx'
# sheet_name = 'Sheet1'
# profile_columns = ['EMPLOYEE NAME', 'JOB TITLE', 'BANK NAME', 'ACCOUNT NUMBER', 'GRADE', 'STEP', 'LOCATION',
#                    'DEPARTMENT', 'PFA NAME', 'PIN NO']
# payroll_columns = ['BASIC SALARY', 'TOTAL ALLOWANCE', 'TOTAL GROSS', 'PENSION', 'P.A.Y.E', 'TOTAL DEDUCTION',
#                    'TOTAL NETPAY']
# columns = profile_columns + payroll_columns
# PayrollCompare(old_file=file1, new_file=file2, key=key_name, sheet=sheet_name, columns=columns).compare()
