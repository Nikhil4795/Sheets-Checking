# Sheets-Checking
Checks whether two sheets are equal or not, if not equal then shows the differences in output sheet.

    Written @ Nikhil

    If you have any queries or suggestions regaring this concept
    feel free to contact me via nikhil.ss4795@gmail.com
    Thank you for spending your time on this.
    
    Description :
    
    Checks whether two sheets are equal or not,
    if not, then shows the differences b/w two input sheets in two output sheets.

    ie.., it shows the data from sheet_1 and data from sheet_2 in seperate cells with
    a unique reference number with respective headers in a single row.

    *  Even though if the sheets are in unordered form (only rows), then also it works fine.
    *  It works fine for large sheets also.

    Input sheet constraints :

    1. Two sheets must be csv
    2. Two sheets must contain a reference column which is common in both in column 0.(Column A)
    3. Two sheets must contain same Header in same order for all columns in each sheet.
    4. Two sheets must conatin same Number of columns.
    

    Output sheet details :

    ** Total two sheets will be generated.
        1. all_errors_seperated_columns :
            *  contains the errors in seperate cells for both the sheets, one row contains
               only one error, so there may be chance of getting duplicate reference numbers
               which has errors in multiple columns.
            *  So that you can have total number of errors in seperate rows.
            
        2. Unique_reference_column_sheet:
            same as above sheet, but it doesn't contains duplicates reference numbers,
            i.e.., it contains all the errors of a particular reference number in the same row only.

    How to run :
    
        Just change the sheet name in "sheet_1_name" and "sheet_2_name" variables after the functions
        code of the two input sheets and hit run.

    Example :

        I will be providing the sample input sheets and thier respective output sheets,
        please check it out if you have any problem.
